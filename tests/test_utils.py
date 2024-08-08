import os
from typing import Any
from unittest.mock import patch

import pytest

from src.utils import format_date, get_currency_rates, get_stock_prices, greetings, start_month

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла user_settings.json относительно текущей директории.
# В файл храниться словарь с требуемыми валютами и акциями
rel_json_path = os.path.join(current_dir, "../data/user_settings.json")
abs_json_path = os.path.abspath(rel_json_path)


@patch("requests.get")
def test_get_currency_rates(mock_get: Any) -> Any:
    """Фуекция тестирует составление списка словарей с валютами. Курсы валюты импортируются по API"""

    mock_get.return_value.json.return_value = {"base": "USD", "date": "2024-08-06", "rates": {"RUB": 85.674637}}

    assert get_currency_rates(abs_json_path) == [
        {"currency": "USD", "rate": 85.674637},
        {"currency": "EUR", "rate": 85.674637},
    ]


@patch("requests.get")
def test_get_stock_prices(mock_get: Any) -> Any:
    """Фуекция тестирует составление списка словарей с акциями. Стоимости акций импортируются по API"""

    mock_get.return_value.json.return_value = [{"symbol": "AAPL", "priceAvg200": 189.68214}]

    assert get_stock_prices(abs_json_path) == [
        {"stock": "AAPL", "price": 189.68214},
        {"stock": "AMZN", "price": 189.68214},
        {"stock": "GOOGL", "price": 189.68214},
        {"stock": "MSFT", "price": 189.68214},
        {"stock": "TSLA", "price": 189.68214},
    ]


@pytest.mark.parametrize(
    "date, greetings_output",
    [
        ("2018-02-16 11:01:58", "Доброе утро"),
        ("2018-02-16 12:01:58", "Добрый день"),
        ("2018-02-16 21:01:58", "Добрый вечер"),
        ("2018-02-16 03:01:58", "Доброй ночи"),
    ],
)
def test_greetings(date: str, greetings_output: str) -> Any:
    """Функция тестирует вывод приветствия в зависимрсти от времени суток"""
    assert greetings(date) == greetings_output


def test_start_month(month: str) -> Any:
    """Функция тестирует вывод начала месяца от предоставленной даты"""
    assert start_month("2018-02-16 12:01:58") == month


@pytest.mark.parametrize(
    "date, formatted_date",
    [
        ("16.02.2018", "2018-02-16"),
        ("01.01.2001", "2001-01-01"),
        ("1.02.2018", "2018-02-01"),
    ],
)
def test_format_date(date: str, formatted_date: str) -> Any:
    """Функция тестирует вывод приветствия в зависимрсти от времени суток"""
    assert format_date(date) == formatted_date
