import csv
import json
import logging
import os
import re
from collections import Counter
from datetime import datetime as dt, timedelta
from typing import Any
from src.utils import df
import numpy as np
import pandas as pd
import requests
from dotenv import load_dotenv
from pandas.tseries.offsets import DateOffset
from dateutil.relativedelta import relativedelta as rdt

load_dotenv(".env")

API_KEY_RATES = os.getenv("API_KEY_RATES")
API_KEY_STOCKS = os.getenv("API_KEY_STOCKS")


# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_log_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)

# Создаем путь до файла user_settings.json относительно текущей директории.
# В файл храниться словарь с требуемыми валютами и акциями
rel_json_path = os.path.join(current_dir, "../data/user_settings.json")
abs_json_path = os.path.abspath(rel_json_path)

# Создаем путь до файла operations.xlsx относительно текущей директории
rel_xlsx_path = os.path.join(current_dir, "../data/operations.xlsx")
abs_xlsx_path = os.path.abspath(rel_xlsx_path)

# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# input_datetime = "2018-02-16 12:01:58"

input_datetime = dt.now().strftime("%Y-%m-%d %H:%M:%S")
date_update = dt.strptime(input_datetime, "%Y-%m-%d %H:%M:%S")
previous_month_date = date_update + rdt(months=-48)


df["Дата операции"] = pd.to_datetime(df["Дата операции"], format="%d.%m.%Y %H:%M:%S")


filtered_df = df[(previous_month_date <= df["Дата операции"]) & (df["Дата операции"] <= input_datetime)]
filtered_df_cl = filtered_df.dropna()
filtered_df_cl_gr = filtered_df_cl[filtered_df_cl["Категория"] == "Транспорт"]

df_output = filtered_df_cl_gr.to_dict("records")

print(df_output)
