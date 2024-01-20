import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy import text  # Используется для создания запроса из строки

# Список параметров для тестов, где каждый элемент - это кортеж из имени файла и ожидаемого числа строк
test_parameters = [
    (r'1.sql', 11264),
    (r'2.sql', 10),
    (r'3.sql', 3),
    (r'4.sql', 30),
    (r'5.sql', 71671),
    (r'6.sql', 73675),
    (r'7.sql', 25060),
    (r'8.sql', 504232),
    (r'9.sql', 73558),
    (r'10.sql', 1),
]


@pytest.fixture(scope='module')
def db_engine():
    """
    Фикстура для создания соединения с базой данных
    :return:
    """
    # Путь к вашей базе данных SQLite
    database_path = r'sqlite:///D:\Syncthing\Работа\Academy_Top\ПРИМЕРЫ КОДА\python_329_code\data\businesses.db'
    engine = create_engine(database_path)
    return engine


# Параметризированный тест проверяющий наличие в этой же папки файлов с запросами
@pytest.mark.parametrize("sql_file, expected_rows", test_parameters)
def test_is_file_exists(sql_file, expected_rows):
    """
    Тест проверяет, что файл с запросом существует
    :param sql_file: Имя файла с запросом
    """
    assert os.path.exists(sql_file), f"Файл {sql_file} не найден"


@pytest.mark.parametrize("sql_file,expected_rows", test_parameters)
def test_sql_query(db_engine, sql_file, expected_rows):
    """
    Тест проверяет, что запрос из файла sql_file возвращает ожидаемое количество строк
    :param db_engine: Фикстура для создания соединения с базой данных
    :param sql_file: Имя файла с запросом
    :param expected_rows: Ожидаемое количество строк
    """
    with open(sql_file, 'r', encoding='utf-8') as file:  # Убедитесь, что файл читается с правильной кодировкой
        query = file.read()

    with db_engine.connect() as connection:
        result = connection.execute(text(query))
        rows = result.fetchall()

    assert len(rows) == expected_rows, f"Запрос из {sql_file} возвратил неправильное количество строк"
