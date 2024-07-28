import csv
import json
import logging
import os
import re
from collections import Counter
from datetime import datetime
from typing import Any

import numpy as np
import pandas as pd
import requests
from dotenv import load_dotenv

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


# input_xlsx_file = pd.read_excel(abs_xlsx_path)
# df_dict = input_xlsx_file.to_dict("records")
# patter = re.compile(r'\D\d\d\d')
# dict_test = {}
# for i in df_dict:
#     i['Номер карты'] = str(i['Номер карты'])
#     match = patter.search(i['Номер карты'])
#     if match:
#         dict_test['last_digits'] = i['Номер карты'][1:]
#     else:
#         dict_test['last_digits'] = 'Номер карты не указан'
#     print(dict_test)


# now = datetime.now()
# print(now)


def greetings(input_datetime: str) -> str:
    date_update = datetime.strptime(input_datetime, "%d.%m.%Y %H:%M:%S")
    time = date_update.strftime("%H:%M:%S")

    if time >= "05:00:00" and time <= "12:00:00":
        return "Доброе утро"
    if time > "12:00:00" and time <= "18:00:00":
        return "Добрый день"
    if time > "18:00:00" and time <= "23:00:00":
        return "Добрый вечер"
    if time > "23:00:00" and time < "05:00:00":
        return "Доброй ночи"


print(greetings("01.01.2018 12:49:53"))


