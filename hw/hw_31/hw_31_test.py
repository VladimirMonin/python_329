import pytest
from sqlalchemy import create_engine
from sqlalchemy import text

# Список параметров для тестов, где каждый элемент - это кортеж из имени файла и ожидаемого числа строк
test_parameters = [
    (r'1.sql', 6)
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
