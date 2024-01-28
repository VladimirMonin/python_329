"""
Lesson 50
sqlite3 module
"""
# Импортируем модуль sqlite3
import sqlite3

SQL_FILE = ''

# Создаем соединение с базой данных
db_path = '../data/lesson_50.db'

# Создаем соединение с базой данных (если базы данных нет, то она создается)
conn = sqlite3.connect(db_path)

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

