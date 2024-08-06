import json
import logging
import os
from typing import Any

import pandas as pd
from dotenv import load_dotenv

from src.utils import format_date

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_log_file_path = os.path.join(current_dir, "../logs/views.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)


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


# Формируем список словарей, содержащий информацию о транзакциях - transactions
df = pd.read_excel(abs_xlsx_path)
df_draft = df[["Дата платежа", 'Сумма платежа']].copy(deep=True)
df_clean = df_draft.dropna()
df_output = df_clean.to_dict("records")
transactions = []
for i in df_output:
    output_dict = {}
    output_dict['Дата платежа'] = format_date(i['Дата платежа'])
    output_dict['Сумма платежа'] = abs(float(i['Сумма платежа']))
    transactions.append(output_dict)

#print(transactions)

month = '2021-12'
limit = 10
for i in transactions:
    if month in i['Дата платежа']:
        print(i)


#def investment_bank(month: str, transactions: list[Dict[str, Any]], limit: int) -> float:
    """Функция принимает на вход аналищируемый месяц, список словарей с транзакциями, предел оуркгления
    и возвращает анализ инвестиционных накоплений в виде json-ответа"""






def home_page(input_df: pd.DataFrame) -> Any:
    """Функция принимает на вход DataFrame и возвращает json-файл"""

    # Формируем приветствие
    logger.info("Приветствие сформировано")
    greetings_output = greetings(input_datetime)

    # Получаем начало месяца
    begin_month = start_month(input_datetime)

    # Отфильтровываем DataFrame по лимиту дат
    logger.info("Входной DataFrame отфильтрован по лимиту дат")
    df_date = pd.to_datetime(input_df["Дата операции"], format="%d.%m.%Y %H:%M:%S")
    filtered_df_to_date = input_df[(begin_month <= df_date) & (df_date <= input_datetime)]

    # Получаем требуемую информацию по картам (номер карты, общая сумма расходов, кэшбэк)
    logger.info("Информация по банковским картам получена: последние 4 цифры карты, общая сумма расходов, кэшбэк")
    cards_description = cards_info(filtered_df_to_date)

    # Получаем информацию по ТОП-5 транзакциям по сумме платежа
    logger.info("Информация по ТОП-5 транзакциям по сумме платежа получена")
    top_five_transactions = top_transactions(filtered_df_to_date)

    # Получаем информацию по курсам валют: USD, EUR
    logger.info("Информация по курсам валют получена: USD, EUR")
    currency_rates = get_currency_rates(abs_json_path)

    # Получаем информацию по стоимости акций
    logger.info("Информация по по стоимости акций получена")
    stock_prices = get_stock_prices(abs_json_path)

    # Формируем список словарей с результатами
    result_list_dicts = {
        "greeting": greetings_output,
        "cards": cards_description,
        "top_transactions": top_five_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
    }

    # Формируем json-ответ
    logger.info("json-ответ создан успешно")
    json_output = json.dumps(result_list_dicts, ensure_ascii=False, indent=4)
    return json_output


#print(home_page(df))
