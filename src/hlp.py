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


# def input_from_excel(input_xlsx_file: str) -> list[Any]:
#     """Функция принимает на вход путь до файла xlsx и возвращает список словарей"""
#
#     input_xlsx_file = pd.read_excel(abs_xlsx_path)
#
#     try:
#         logger.info("Данные из файла xlsx импортированы")
#
#         # Преобразуем DataFrame в список словарей
#         df_dict = input_xlsx_file.to_dict("records")
#         output_list_dicts = []
#         for i in df_dict:
#             output_list_dicts.append(i)
#         return output_list_dicts
#     except Exception:
#         logger.warning("Импортируемый список пуст или отсутствует.")
#         return []
#
#
# input_df = input_from_excel(abs_xlsx_path)
#
# input_xlsx_file = pd.read_excel(abs_xlsx_path)
# print(input_xlsx_file)
# print(input_from_excel(abs_xlsx_path))


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


# def greetings(input_datetime: str) -> str:
#     date_update = dt.strptime(input_datetime, "%d.%m.%Y %H:%M:%S")
#     time = date_update.strftime("%H:%M:%S")
#
#     if time >= "05:00:00" and time <= "12:00:00":
#         return "Доброе утро"
#     if time > "12:00:00" and time <= "18:00:00":
#         return "Добрый день"
#     if time > "18:00:00" and time <= "23:00:00":
#         return "Добрый вечер"
#     if time > "23:00:00" and time < "05:00:00":
#         return "Доброй ночи"


# print(greetings("01.01.2018 12:49:53"))

#
# input_xlsx_file = pd.read_excel(abs_xlsx_path)
# df_dict = input_xlsx_file.to_dict("records")
#
# def sort_by_date(input_list: list[Any], descending=True) -> Any:
#     """Функция сортировки операций по дате"""
#
#     sorted_list = sorted(input_list, key=lambda x: x.get("Дата операции"), reverse=descending)
#
#     for i in sorted_list:
#         print(i)
#
# print(sort_by_date(df_dict))

# def cards():
#     input_date = str(input(
# """Добрый день! Пожалуйста введите интересующую дату в диапозоне от 01.01.2018 12:49:53 до 14.02.2020 21:32:38 включительно в формате: YYYY-MM-DD HH:MM:SS"""))
#     pattern = re.compile(r'\d{4}-\d{2}-\d{2}\s\d{2}-\d{2}-\d{2}')
#     match = pattern.search(input_date)
#     if match:
#
#         print("match")
#     else:
#         print('dddw1w')
#
#
# cards()

input_datetime = "2018-02-16 12:01:58"
#
#
def get_data(input_datetime) -> str:
    """Функция преобразования даты"""

    date_update = dt.strptime(input_datetime, "%Y-%m-%d %H:%M:%S")
    return date_update.strftime("%d.%m.%Y %H:%M:%S")
get_dt = get_data(input_datetime)
print(f'get_data {get_dt}')


#
#
# def greetings(input_datetime: str) -> str:
#     date_update = dt.strptime(input_datetime, "%d.%m.%Y %H:%M:%S")
#     time = date_update.strftime("%H:%M:%S")
#
#     if time > "05:00:00" and time <= "12:00:00":
#         return "Доброе утро"
#     if time > "12:00:00" and time <= "18:00:00":
#         return "Добрый день"
#     if time > "18:00:00" and time <= "23:00:00":
#         return "Добрый вечер"
#     else:
#         return "Доброй ночи"
#
# greetings_output = greetings(get_dt)




# def print_i(input_src: list[Any]) -> list[Any]:
#     for i in input_src:
#         print(i)
#
#
#
# print(print_i(input_df))


# def data_update(file):
#
#
#     df_date = pd.to_datetime(file['Дата операции'], format="%d.%m.%Y %H:%M:%S")
#
#     return df_date
#
# print(data_update(input_xlsx_file,"2018-02-16 00:00:00" ))


# def from_excel(file):
#     df = pd.read_excel(file)
#     df_date = pd.to_datetime(df['Дата операции'], format="%d.%m.%Y %H:%M:%S")
#     return df_date
#
# print(from_excel(abs_xlsx_path))
#
# # input_xlsx_file = pd.read_excel(abs_xlsx_path)
# # df_date = pd.to_datetime(input_xlsx_file['Дата операции'], format="%d.%m.%Y %H:%M:%S")
# # print(df_date)
# # #print(input_xlsx_file)

# def filter(file, datin):
#     st = datin.replace(day=1, hour=0, minute=0, second=0)
#     df = pd.read_excel(file)
#     df_date = pd.to_datetime(df['Дата операции'], format='%d.%m.%Y %H:%M:%S')
#     df = df[(st <= df_date) & (df_date <= datin)]
#     return df
# print(filter(abs_xlsx_path, '16-02-2018 00:00:00'))


def filter(datin):
    date_update = dt.strptime(datin, "%d.%m.%Y %H:%M:%S")
    st = date_update.replace(day=1, hour=0, minute=0, second=0)
    du = st.strftime("%d.%m.%Y %H:%M:%S")

    return du
print(filter(get_dt))



