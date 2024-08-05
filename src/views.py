import csv
import json
import logging
import os
import re
from collections import Counter
from datetime import datetime as dt
from typing import Any

import numpy as np
import pandas as pd
import requests
from dotenv import load_dotenv

from src.utils import start_month, greetings, cards_info

load_dotenv(".env")

API_KEY_RATES = os.getenv("API_KEY_RATES")
API_KEY_STOCKS = os.getenv("API_KEY_STOCKS")


# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_log_file_path = os.path.join(current_dir, "../logs/views.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)

# Создаем путь до файла user_settings.json относительно текущей директории.
# В файл храниться словарь с требуемыми валютами и акциями
rel_json_path = os.path.join(current_dir, "../data/user_settings.json")
abs_json_path = os.path.abspath(rel_json_path)

# Создаем путь до файла operations.xlsx относительно текущей директории
rel_xlsx_path = os.path.join(current_dir, "../data/operations.xlsx")
abs_xlsx_path = os.path.abspath(rel_xlsx_path)

# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("views")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Импортируем DataFrame из xlsx-файла


def input_from_excel(input_xlsx_file: str) -> list[Any]:
    """Функция принимает на вход путь до файла xlsx и возвращает список словарей"""

    dataframe = pd.read_excel(input_xlsx_file)

    try:
        logger.info("DataFrame создан")

        return dataframe
    except Exception:
        logger.warning("Импортируемый список пуст или отсутствует.")
        return []


df = input_from_excel(abs_xlsx_path)

# Входящая дата
input_datetime = "2018-02-16 12:01:58"


def home_page(input_df: Any) -> Any:
    """Функция принимает на вход DataFrame и возвращает json-файл"""

    # Формируем приветствие
    logger.info("Приветствие сформировано")
    greetings_output = greetings(input_datetime)
    # print(greetings_output)

    # Получаем начало месяца
    begin_month = start_month(input_datetime)
    # print(begin_month)

    # Отфильтровываем DataFrame по лимиту дат
    logger.info("Входной DataFrame отфильтрован по лимиту дат")
    df_date = pd.to_datetime(df["Дата операции"], format="%d.%m.%Y %H:%M:%S")
    filtered_df_to_date = df[(begin_month <= df_date) & (df_date <= input_datetime)]
    # print(filtered_df_to_date)

    # Получаем требуемую информацию по картам (номер карты, общая сумма расходов, кэшбэк)
    logger.info("Информация по банковским картам получена: последние 4 цифры карты, общая сумма расходов, кэшбэк")
    cards_description = cards_info(filtered_df_to_date)
    print(cards_description)


home_page(df)
