from src.utils import *
from src.views import *
import pytest
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


# @pytest.mark.parametrize("df, input_list_dicts", [("2018-02-16 12:01:58", {'greeting': 'Добрый день', 'cards': [{'last_digits': '*4556', 'total_spent': 9115.3, 'cashback': 91.15}, {'last_digits': '*5441', 'total_spent': 196143.78, 'cashback': 1961.44}, {'last_digits': '*7197', 'total_spent': 17671.41, 'cashback': 176.71}], 'top_transactions': [{'date': '15.02.2018', 'amount': 30000.0, 'category': 'Пополнения', 'description': 'Перевод с карты'}, {'date': '15.02.2018', 'amount': 30000.0, 'category': 'Пополнения', 'description': 'Перевод с карты'}, {'date': '09.02.2018', 'amount': 30000.0, 'category': 'Пополнения', 'description': 'Перевод с карты'}, {'date': '09.02.2018', 'amount': 30000.0, 'category': 'Пополнения', 'description': 'Перевод с карты'}, {'date': '15.02.2018', 'amount': 29963.87, 'category': 'Пополнения', 'description': 'Перевод с карты'}], 'currency_rates': [{'currency': 'USD', 'rate': 85.252748}, {'currency': 'EUR', 'rate': 93.015835}], 'stock_prices': [{'stock': 'AAPL', 'price': 189.68214}, {'stock': 'AMZN', 'price': 168.6823}, {'stock': 'GOOGL', 'price': 153.1682}, {'stock': 'MSFT', 'price': 404.13535}, {'stock': 'TSLA', 'price': 203.6644}]})])
# def test_home_page(df, input_list_dicts):
#     """Функция тестирует вывод приветствия в зависимрсти от времени суток"""
#     assert home_page(df) == input_list_dicts


def test_home_page(page):
    assert home_page(df) == page
