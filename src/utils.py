import csv
import json
import logging
import os
import re
from collections import Counter
from datetime import datetime as dt
from typing import Any

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

# Создаем json-файл со списком акций и валют

currencies_stocks_dict = {"user_currencies": ["USD", "EUR"], "user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]}

with open(abs_json_path, "w") as file:
    json.dump(currencies_stocks_dict, file)


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


# print(input_from_excel(abs_xlsx_path))


def get_currency_rates(json_file: str) -> list[Any]:
    """Функция принимает на вход json-файл и возвращает список словарей с курсами требуемых валют.
    Курс валюты функция импортирует через API"""
    logger.info("Курсы валют получены")
    with open(json_file, "r", encoding="utf-8") as file:

        currencies_stocks_list = json.load(file)
        currency_rates_list_dicts = []

        for i in currencies_stocks_list["user_currencies"]:

            url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={i}"

            headers = {"apikey": API_KEY_RATES}

            response = requests.get(url, headers=headers)

            result = response.json()
            # print(result)
            currency_rates_dict = {"currency": i, "rate": result["rates"].get("RUB")}
            currency_rates_list_dicts.append(currency_rates_dict)

        return currency_rates_list_dicts


# print(get_currency_rates(abs_json_path))


def get_stock_prices(json_file: str) -> list[Any]:
    """Функция принимает на вход json-файл и возвращает список словарей с курсами требуемых акций.
    Стоимости акций функция импортирует через API"""
    logger.info("Стоимости акций получены")
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


# print(get_stock_prices(abs_json_path))

input_datetime = "2019-01-01 23:01:00"


def get_data(input_datetime) -> str:
    """Функция преобразования даты"""

    date_update = dt.strptime(input_datetime, "%Y-%m-%d %H:%M:%S")
    return date_update.strftime("%d.%m.%Y %H:%M:%S")

#print(get_data("2018-02-16 12:01:58"))



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

#print(greetings(get_data("2018-02-16 12:01:58")))


def start_month(input_datetime):
    date_update = dt.strptime(input_datetime, "%d.%m.%Y %H:%M:%S")
    start = date_update.replace(day=1, hour=0, minute=0, second=0)
    start_update = start.strftime("%d.%m.%Y %H:%M:%S")

    return start_update

#print(start_month(get_data("2018-02-16 12:01:58")))
