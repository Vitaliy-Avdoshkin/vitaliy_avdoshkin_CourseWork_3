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


# url = f"https://financialmodelingprep.com/api/v3/quote/AAPL?apikey={API_KEY_STOCKS}"
#
# response = requests.get(url)
#
# result = response.json()


def get_stock_prices(json_file):
    """Функция принимает на вход json-файл и возвращает список словарей с курсами требуемых акций.
    Стоимости акций функция импортирует через API"""

    with open(json_file, "r", encoding="utf-8") as file:

        currencies_stocks_list = json.load(file)
        stock_prices_list_dicts = []
        # print(transactions_info)
        for i in currencies_stocks_list["user_stocks"]:

            url = f"https://financialmodelingprep.com/api/v3/quote/{i}?apikey={API_KEY_STOCKS}"

            response = requests.get(url)

            result = response.json()
            stock_prices_dicts = {"stock": i, "price": result[0].get("priceAvg200")}
            stock_prices_list_dicts.append(stock_prices_dicts)

        return stock_prices_list_dicts


print(get_stock_prices(abs_json_path))
