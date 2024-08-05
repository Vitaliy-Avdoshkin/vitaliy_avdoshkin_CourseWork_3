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


def input_from_excel(input_xlsx_file: str) -> list[Any]:
    """Функция принимает на вход путь до файла xlsx и возвращает список словарей"""

    input_xlsx_file = pd.read_excel(abs_xlsx_path)

    try:
        logger.info("Данные из файла xlsx импортированы")

        # Преобразуем DataFrame в список словарей
        df_dict = input_xlsx_file.to_dict("records")
        output_list_dicts = []
        for i in df_dict:
            output_list_dicts.append(i)
        return output_list_dicts
    except Exception:
        logger.warning("Импортируемый список пуст или отсутствует.")
        return []


input_df = input_from_excel(abs_xlsx_path)
# print(input_df)


# def cards_info(input_xlsx_file: str) -> list[dict[str, Any]]:
#     """Функция принимает на вход путь до файла xlsx и возвращает DataFrame"""
#
#     input_xlsx_file = pd.read_excel(abs_xlsx_path)
#     df_output = []
#     try:
#         logger.info("Данные из файла xlsx импортированы")
#
#         cards = input_xlsx_file.groupby('Номер карты')
#         cards_prices = cards['Сумма операции с округлением'].sum()
#         df_test = cards_prices.to_dict()
#
#         for cards, sum in df_test.items():
#             df_result = {}
#             #print(cards)
#             #print(f'{cards} = {sum}')
#             df_result['last_digits'] = cards
#             df_result['total_spent'] = sum
#             df_result['cashback'] = round(sum / 100, 2)
#             df_output.append(df_result)
#         return df_output
#     except Exception:
#         logger.warning("Импортируемый список пуст или отсутствует.")
#         return "Импортируемый список пуст или отсутствует."
#
#
# cards_info = cards_info(abs_xlsx_path)
# print(cards_info)


def get_data(input_datetime) -> str:
    """Функция преобразования даты"""

    date_update = dt.strptime(input_datetime, "%Y-%m-%d %H:%M:%S")
    return date_update.strftime("%d.%m.%Y %H:%M:%S")


# print(get_data("2018-02-16 12:01:58"))


def greetings(input_datetime: str) -> str:
    date_update = dt.strptime(input_datetime, "%d.%m.%Y %H:%M:%S")
    time = date_update.strftime("%H:%M:%S")

    if time > "05:00:00" and time <= "12:00:00":
        return "Доброе утро"
    if time > "12:00:00" and time <= "18:00:00":
        return "Добрый день"
    if time > "18:00:00" and time <= "23:00:00":
        return "Добрый вечер"
    else:
        return "Доброй ночи"


# print(greetings(get_data("2018-02-16 12:01:58")))


# def print_i(input_src: list[Any]) -> list[Any]:
#     for i in input_src:
#         print(i)

# print(print_i(input_df))


# def start_month(input_datetime):
#     date_update = dt.strptime(input_datetime, "%d.%m.%Y %H:%M:%S")
#     start = date_update.replace(day=1, hour=0, minute=0, second=0)
#     start_update = start.strftime("%d.%m.%Y %H:%M:%S")
#
#     return start_update
# print(start_month(get_data("2018-02-16 12:01:58")))


# def df_filter(input_xlsx_file: str) -> list[dict[str, Any]]:
#     """Функция принимает на вход dataframe и возвращает отфильтрованный dataframe по лимиты дат"""
#
#
#
#
#
# print(cards_info)


def df_filter(input_datetime):

    date_update = dt.strptime(input_datetime, "%d.%m.%Y %H:%M:%S")
    start = date_update.replace(day=1, hour=0, minute=0, second=0)
    start_update = start.strftime("%d.%m.%Y %H:%M:%S")

    return start_update
print(df_filter(get_data("2018-02-16 12:01:58")))