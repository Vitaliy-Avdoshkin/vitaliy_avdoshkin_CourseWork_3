import csv
import json
import logging
import os
import re
from collections import Counter
from typing import Any
import pandas as pd

import os

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

# Создаем json-файл со списком акций и валют

currencies_stocks_dict = {"user_currencies": ["USD", "EUR"], "user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]}

with open(abs_json_path, "w") as file:
    json.dump(currencies_stocks_dict, file)


def input_from_excel(input_xlsx_file: str) -> list[Any]:
    """Функция принимает на вход путь до файла xlsx и возвращает список словарей"""

    input_xlsx_file = pd.read_excel(abs_xlsx_path)

    try:
        logger.info("Путь до файла xlsx верный")

        # Преобразуем DataFrame в список словарей
        df_dict = input_xlsx_file.to_dict("records")
        output_list_dicts = []
        for i in df_dict:
            output_list_dicts.append(i)
        return output_list_dicts
    except Exception:
        logger.warning("Импортируемый список пуст или отсутствует.")
        return []


# print(input_from_excel(abs_xlsx_path))


def get_currency_rates(json_file):
    """Функция принимает на вход json-файл и возвращает список словарей с курсами требуемых валют.
    Курс валюты функция импортирует через API"""

    with open(json_file, "r", encoding="utf-8") as file:

        currencies_stocks_list = json.load(file)
        currency_rates_list_dicts = []

        for i in currencies_stocks_list["user_currencies"]:

            url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={i}"

            headers = {"apikey": API_KEY_RATES}

            response = requests.get(url, headers=headers)

            result = response.json()
            currency_rates_dict = {"currency": i, "rate": result["rates"].get("RUB")}
            currency_rates_list_dicts.append(currency_rates_dict)

        return currency_rates_list_dicts


print(get_currency_rates(abs_json_path))
