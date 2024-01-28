"""
Lesson 50
sqlite3 module
"""
# Импортируем модуль sqlite3
import sqlite3

SQL_FILE = 'lesson_50.sql'
DB_PATH = '../data/lesson_50.db'

# Создаем соединение с базой данных

# Создаем соединение с базой данных (если базы данных нет, то она создается)
conn = sqlite3.connect(DB_PATH)

# Закрываем соединение с базой данных
# conn.close()

# Создаем курсор
cursor = conn.cursor()

# Инструменты для работы с транзакциями
# conn.commit() - сохранить изменения
# conn.rollback() - откатить изменения

# Исключения для работы с базой данных
# sqlite3.DatabaseError - базовое исключение
# sqlite3.OperationError - исключение, возникающее по техническим причинам
# sqlite3.IntegrityError - исключение, возникающее при нарушении целостности данных (дублирование данных)
# sqlite3.ProgrammingError - исключение, возникающее при ошибке в SQL запросе (например, синтаксическая ошибка)
# sqlite3.NotSupportedError - исключение, возникающее при попытке выполнить не поддерживаемую операцию


# Для выполнения запросов:
# cursor.execute(sql, params) - выполнить запрос
# cursor.executemany(sql, params) - выполнить запрос много раз
# cursor.executescript(sql) - выполнить несколько запросов (разделенных ;)

# Для получения данных:
# cursor.fetchone() - получить одну строку
# cursor.fetchall() - получить все строки

# Читаем SQL запрос из файла
with open(SQL_FILE, 'r', encoding='utf-8') as f:
    sql_query = f.read()

print(sql_query)