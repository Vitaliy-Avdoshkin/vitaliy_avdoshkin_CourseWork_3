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


input_datetime = "2018-02-16 12:01:58"


def greetings(input_datetime: str) -> str:
    date_update = dt.strptime(input_datetime, "%Y-%m-%d %H:%M:%S")
    time = date_update.strftime("%H:%M:%S")

    if time > "05:00:00" and time <= "12:00:00":
        return "Доброе утро"
    if time > "12:00:00" and time <= "18:00:00":
        return "Добрый день"
    if time > "18:00:00" and time <= "23:00:00":
        return "Добрый вечер"
    else:
        return "Доброй ночи"


# print(greetings(input_time))


def start_month(input_datetime):
    date_update = dt.strptime(input_datetime, "%Y-%m-%d %H:%M:%S")
    start = date_update.replace(day=1, hour=0, minute=0, second=0)
    return start


begin_month = start_month(input_datetime)
# print(start_month(input_time))


def filter_date(df_test):
    df = pd.read_excel(df_test)
    df_date = pd.to_datetime(df["Дата операции"], format="%d.%m.%Y %H:%M:%S")
    filtered_df_to_date = df[(begin_month <= df_date) & (df_date <= input_datetime)]
    return filtered_df_to_date


filtered_to_date = filter_date(abs_xlsx_path)
# print(filter_date(abs_xlsx_path))


def cards_info(input_df: str) -> list[dict[str, Any]]:
    """Функция принимает на вход путь до файла xlsx и возвращает DataFrame"""

    df_input = input_df
    df_output = []
    try:
        logger.info("Данные из файла xlsx импортированы")

        cards = df_input.groupby("Номер карты")
        cards_prices = cards["Сумма операции с округлением"].sum()
        df_test = cards_prices.to_dict()

        for cards, sum in df_test.items():
            df_result = {}
            df_result["last_digits"] = cards
            df_result["total_spent"] = sum
            df_result["cashback"] = round(sum / 100, 2)
            df_output.append(df_result)
        return df_output
    except Exception:
        logger.warning("Импортируемый список пуст или отсутствует.")
        return "Импортируемый список пуст или отсутствует."


# print(cards_info(filtered_to_date))


def top_transactions(input_df):
    df_input_sort = input_df
    df_output_sort = []
    try:
        logger.info("Данные из файла xlsx импортированы")

        sorted_df = df_input_sort.sort_values("Сумма платежа", ascending=False)
        sort_five = sorted_df.iloc[0:5]

        df_sort_dict = sort_five.to_dict("records")
        for i in df_sort_dict:
            df_sort_result = {}
            df_sort_result["date"] = i["Дата платежа"]
            df_sort_result["amount"] = i["Сумма платежа"]
            df_sort_result["category"] = i["Категория"]
            df_sort_result["description"] = i["Описание"]
            df_output_sort.append(df_sort_result)
        return df_output_sort
    except Exception:
        logger.warning("Импортируемый список пуст или отсутствует.")
        return "Импортируемый список пуст или отсутствует."


# print(top_transactions(filtered_to_date))


# def input_from_excel(input_xlsx_file: str) -> list[dict[str, Any]]:
#     """Функция принимает на вход путь до файла xlsx и возвращает список словарей"""
#
#     dataframe = pd.read_excel(input_xlsx_file)
#
#     try:
#         logger.info("DataFrame создан")
#         transactions = dataframe[['Дата операции', 'Сумма операции']].copy
#         #df_date = pd.to_datetime(transactions["Дата операции"], format="%d.%m.%Y %H:%M:%S")
#         #return df_date
#         return transactions
#     except Exception:
#         logger.warning("Импортируемый список пуст или отсутствует.")
#         return []
#
#
# df = input_from_excel(abs_xlsx_path)
#
#
# def fed(deg):
#
#     df_date = pd.to_datetime(deg["Дата операции"], format="%d.%m.%Y %H:%M:%S")
#     return df_date
#
# print(fed(df))
# def get_transactions_info(input_df: pd.DataFrame) -> list[dict[str, Any]]:
#     dataframe = pd.read_excel(input_df)
#     dataframe["Дата операции"] = pd.to_datetime(dataframe["Дата операции"], format="%d.%m.%Y %H:%M:%S")
#     transactions = dataframe[['Дата операции', 'Сумма платежа']]
#
#
#
#     #return transactions
#
#
#
# # transactions = get_transactions_info(abs_xlsx_path)
# # print(transactions)
#
#
# def get_transactions_info(input_xlsx_file: str) -> list[dict[str, Any]]:
#     """Функция принимает на вход путь до файла xlsx и возвращает список словарей"""
#
#     input_df = pd.read_excel(input_xlsx_file)
#
#     try:
#         logger.info("Данные из файла xlsx импортированы")
#
#         #input_df["Дата операции"] = pd.to_datetime(input_df["Дата операции"], format="%d.%m.%Y %H:%M:%S")
#         transactions_df = input_df[['Дата операции', 'Сумма платежа']]
#         # Преобразуем DataFrame в список словарей
#         transactions = transactions_df.to_dict("records")
#         output_list_dicts = []
#         for i in transactions:
#             output_list_dicts.append(i)
#
#         return output_list_dicts
#     except Exception:
#         logger.warning("Импортируемый список пуст или отсутствует.")
#         return []
#
#
# print(get_transactions_info(abs_xlsx_path))


def format_date(input_datetime: str) -> str:
    date_update = dt.strptime(input_datetime, "%d.%m.%Y")
    return date_update.strftime("%Y-%m-%d")


# print(format_date('12.01.2018'))


df = pd.read_excel(abs_xlsx_path)
df_draft = df[["Дата платежа", "Сумма платежа"]].copy(deep=True)
df_clean = df_draft.dropna()
df_output = df_clean.to_dict("records")
transactions = []
for i in df_output:
    output_dict = {}
    output_dict["Дата платежа"] = format_date(i["Дата платежа"])
    output_dict["Сумма платежа"] = i["Сумма платежа"]
    transactions.append(output_dict)


# print(transactions)


# def from_excel_to_list(input_xlsx_file: str) -> list[dict[str, Any]]:
#     """Функция принимает на вход путь до файла xlsx и возвращает список словарей"""
#
#     input_df = pd.read_excel(input_xlsx_file)
#     output_list_dicts = []
#     try:
#         logger.info("Данные из файла xlsx импортированы")
#
#         # Преобразуем DataFrame в список словарей
#         df_dict = input_df.to_dict("records")
#         output_list_dicts = []
#         for i in df_dict:
#             output_dict = {}
#             output_dict['Дата операции'] = i['Дата операции']
#             output_dict['Сумма платежа'] = abs(i['Сумма платежа'])
#             output_list_dicts.append(output_dict)
#
#         return output_list_dicts
#     except Exception:
#         logger.warning("Импортируемый список пуст или отсутствует.")
#         return []
#
#
# print(from_excel_to_list(abs_xlsx_path))
