# Vitaliy_Avdoshkin_CourseWork_3

# Проект 1. Приложение для анализа банковских операций

## Описание

В рамках проекта будет разработано приложение для анализа транзакций,
которые находятся в Excel-файле.
Приложение будет генерировать JSON-данные для веб-страниц,
формировать Excel-отчеты, а также предоставлять другие сервисы.

## Установка:

1. Клонируйте репозиторий:

```
git clone https://github.com/Vitaliy-Avdoshkin/vitaliy_avdoshkin_CourseWork_3.git
```
## Конфигурация
1. Создайте виртуальное окружение poetry.

```
poetry env
```

2. Установите библиотеки Flake8, black, isort, mypy в группу lint.

```commandline
poetry add --group lint flake8
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint mypy
```

3. Создайте файл .flake8 для настройки библиотеки flak8


4. Настройте установленные библиотеки, используя кода ниже

Файл .flake8

```
[flake8]
max-line-length = 119
exclude = .git, __pycache__
```

Файл pyproject.toml

black, isort, mypy
```
[tool.black]
line_length = 119
exclude = '''
/(
  | \.git
)/
'''

[tool.isort]
line_length = 119

[tool.mypy]
disallow_untyped_defs = true
warn_return_any = true
exclude = '''
/(
  | \.venv
)/
'''
```

5. Установите библиотеку pandas, для работы с табличными данными.
Также, для корректной работы с Excel-файлами в pandas необходимо
дополнительно установить библиотеку openpyxl.
 
```
poetry add pandas
poetry add openpyxl
```

6. Установите библиотеки requests и dotenv
````commandline
poetry add requests
poetry add python-dotenv
````

## Тестирование

1. Для тестирования кода установите Pytest
```
poetry add --group dev pytest
```
2. Установите Code coverage для расчета процента протестированного кода
```
poetry add --group dev pytest-cov
```
Запуск Code coverage
```commandline
pytest --cov
```
Чтобы сгенерировать отчет о покрытии в HTML-формате, используйте следующую команду
```commandline
pytest --cov=src --cov-report=html
```
Отчет будет сгенерирован в папке
```
htmlcov
```
 и храниться в файле с названием 
```
index.html
```

3. Для тестирования вывода в консоль используйте специальную фикстуру
```
capsys
```

# Модули

## Модуль Main
Модуль выводит результат работы всех главных функций в проекте

## Модуль reports
Модуль содержит функцию def spending_by_category, которая принимает на вход датафрейм с транзакциями, категорию и дату (опционально, по-умолчанию = текущая дата).
И возвращает информацию по каждой трате по заданной категории за последние три месяца (от переданной даты)
Также в моделе есть функция-декоратор log, которая декорирует вывод результата функции spending_by_category в файл reports_log

## Модуль services
В моделе находится функция def investment_bank, которая принимает на вход анализируемый месяц, список словарей с транзакциями, шаг округления
и возвращает анализ инвестиционных накоплений в виде json-ответа.

## Модуль utils
Модуль представляет собой набор функций-утилит, помогающих получать и формировать данные
Функция import_from_excel - принимает на вход путь до файла xlsx и возвращает DataFrame
def get_currency_rates - принимает на вход json-файл и возвращает список словарей с курсами требуемых валют. Курс валюты функция импортирует через API
def get_stock_prices - принимает на вход json-файл и возвращает список словарей с курсами требуемых акций. Стоимости акций функция импортирует через API
def greetings - принимает строку с датой и возвращает требуемое приветствие
def start_month - принимает на вход строку с датой и возвращает начало месяца
def filter_date - создает DataFrame по заданному периоду времени
def cards_info - принимает на вход путь до файла xlsx и возвращает DataFrame с требуемой информацией по банковским картам
def top_transactions - принимает на вход DataFrame и возвращает ТОП-5 транзакций по сумме платежа
def format_date - преобразует дату в требуемый формат

## Модуль view

Содержит функцию home_page, которая направляет работу функций:
 - input_from_excel;
 - greetings;
 - start_month;
 - cards_info;
 - top_transactions;
 - get_currency_rates;
 - get_stock_prices.
Для получения информации на Главной страницы web-приложения.
Функция возвращает json-ответ.