"""
Lesson 80
16.12.2023

- Паттерны проектирования
- Паттерн "Одиночка" - Singleton

"""
import sqlite3


class Singleton:
    _instance = None  # Статическая переменная для хранения единственного экземпляра

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect("my_database.db")  # Подключение к базе данных
        return cls._instance

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result


# Использование Singleton для подключения к базе данных
db_connection1 = DatabaseConnection()
# Создаем таблицу users
db_connection1.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
result1 = db_connection1.execute_query("SELECT * FROM users")

db_connection2 = DatabaseConnection()  # Получаем тот же самый объект
# Создаем таблицу orders
db_connection2.execute_query("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, user_id INTEGER, "
                             "product_name TEXT, price INTEGER)")
result2 = db_connection2.execute_query("SELECT * FROM orders")

print(result1)
print(result2)

print(id(db_connection1))
print(id(db_connection2))
print(db_connection1 is db_connection2)  # True, это один и тот же объект

# Использование Singleton
instance1 = Singleton()
instance2 = Singleton()

print(instance1 is instance2)  # True, это один и тот же объект
