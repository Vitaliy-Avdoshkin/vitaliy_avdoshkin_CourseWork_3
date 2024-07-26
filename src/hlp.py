import csv
import json
import logging
import os
import re
from collections import Counter
from typing import Any

import pandas as pd


# # Получаем абсолютный путь до текущей директории
# current_dir = os.path.dirname(os.path.abspath(__file__))
#
# # Создаем путь до файла логов относительно текущей директории
# rel_log_file_path = os.path.join(current_dir, "../logs/utils.log")
# abs_log_file_path = os.path.abspath(rel_log_file_path)
#
# # Создаем путь до файла xlsx относительно текущей директории
# rel_xlsx_path = os.path.join(current_dir, "../data/operations.xlsx")
# abs_xlsx_path = os.path.abspath(rel_xlsx_path)


def input_from_excel(input_xlsx_file: str) -> list[Any]:
    """Функция принимает на вход путь до файла xlsx и возвращает список словарей"""

    df = pd.read_excel(input_xlsx_file)
    df_dict = df.to_dict("records")
    return  df_dict


#print(input_from_excel('..\\data\\operations.xlsx'))


def iterone(input_list):

    for i in input_list:
        if i['Валюта платежа'] != 'RUB':
            print(i)

print(iterone(input_from_excel('..\\data\\operations.xlsx')))
