import json
from datetime import datetime

import pytest


@pytest.fixture
def month() -> datetime:
    return datetime(2018, 2, 1, 0, 0)


@pytest.fixture
def invest() -> str:
    result_list_dicts = {"month": "2021-12", "rounding_step": 10, "total_amount": 1187.69}

    json_output = json.dumps(result_list_dicts, ensure_ascii=False, indent=4)
    return json_output


@pytest.fixture
def page() -> str:
    result_list_dicts = {
        "greeting": "Добрый день",
        "cards": [
            {"last_digits": "*4556", "total_spent": 9115.3, "cashback": 91.15},
            {"last_digits": "*5441", "total_spent": 196143.78, "cashback": 1961.44},
            {"last_digits": "*7197", "total_spent": 17671.41, "cashback": 176.71},
        ],
        "top_transactions": [
            {"date": "15.02.2018", "amount": 30000.0, "category": "Пополнения", "description": "Перевод с карты"},
            {"date": "15.02.2018", "amount": 30000.0, "category": "Пополнения", "description": "Перевод с карты"},
            {"date": "09.02.2018", "amount": 30000.0, "category": "Пополнения", "description": "Перевод с карты"},
            {"date": "09.02.2018", "amount": 30000.0, "category": "Пополнения", "description": "Перевод с карты"},
            {"date": "15.02.2018", "amount": 29963.87, "category": "Пополнения", "description": "Перевод с карты"},
        ],
        "currency_rates": [{"currency": "USD", "rate": 85.67821}, {"currency": "EUR", "rate": 93.650737}],
        "stock_prices": [
            {"stock": "AAPL", "price": 189.68214},
            {"stock": "AMZN", "price": 168.6823},
            {"stock": "GOOGL", "price": 153.1682},
            {"stock": "MSFT", "price": 404.13535},
            {"stock": "TSLA", "price": 203.6644},
        ],
    }
    json_output = json.dumps(result_list_dicts, ensure_ascii=False, indent=4)
    return json_output
