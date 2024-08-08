import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.views import home_page

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


def test_home_page(page: str) -> str:
    """Функция тестирует работу главной функции home_page"""
    with (
        patch("src.views.get_currency_rates") as mock_get_currency_rates,
        patch("src.views.get_stock_prices") as mock_get_current_stocks,
    ):
        mock_get_currency_rates.return_value = [
            {"currency": "USD", "rate": 85.67821},
            {"currency": "EUR", "rate": 93.650737},
        ]
        mock_get_current_stocks.return_value = [
            {"stock": "AAPL", "price": 189.68214},
            {"stock": "AMZN", "price": 168.6823},
            {"stock": "GOOGL", "price": 153.1682},
            {"stock": "MSFT", "price": 404.13535},
            {"stock": "TSLA", "price": 203.6644},
        ]
        assert home_page(abs_xlsx_path) == page
