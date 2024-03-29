"""
Lesson 50
sqlite3 module
- Использование модуля sqlite3
- cursor
- conneciton
- execute
- executemany
- executescript
- fetchone
- fetchall
- commit
- rollback
- Exceptions
"""
# Импортируем модуль sqlite3
import sqlite3
from pprint import pprint

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
# with open(SQL_FILE, 'r', encoding='utf-8') as f:
#     sql_query = f.read()

# print(sql_query)

# Два варианта выполнения запроса
# 1. Разбить запрос по ; и выполнить каждый запрос отдельно через try/except
# 2. Использовать метод executescript() - он сам разобьет запрос по ;

# Выполняем запрос c помощью метода executescript()
# cursor.executescript(sql_query)

# Выполняем запрос c помощью метода execute()

"""
SQLite3 автоматически создает транзакцию для каждого запроса.
Если запрос выполняется успешно, то транзакция автоматически фиксируется.

Если запрос выполняется с ошибкой у нас нет возможности откатить ВСЕ изменения.
"""
# for query in sql_query.split(';'):
#     try:
#         # Делаем начало транзакции
#         cursor.execute(query)
#
#     except sqlite3.DatabaseError as err:
#         print(err)
#         print(query)
#         conn.rollback()
#         break
# else:
#     conn.commit()

# Выполняем запрос c помощью cursor.executescript(sql_query)

# try:
#     cursor.executescript(sql_query)
# except sqlite3.DatabaseError as err:
#     print(err)
#     conn.rollback()
# else:
#     conn.commit()

# Выполним этот запрос с помощью cursor.execute(sql_query)

group_add_query = """
-- Добавляем группу в таблицу групп
INSERT INTO groups (group_name) VALUES ('python329');
"""

group_add_query2 = """
-- Добавляем группу в таблицу групп
INSERT INTO groups (group_name) VALUES ('python331');
"""


student_add_query = """
-- Добавляем студентов в таблицу студентов (id group= 1)
INSERT INTO students (first_name, middle_name, last_name, group_id) VALUES
('Андрей', 'Сергеевич', 'Анохин', 1),
('Елена', 'Сергеевна', 'Гудкова', 1),
('Станислав', 'Константинович', 'Козлов', 1),
('Виталий', 'Валерьевич', 'Костин', 1),
('Артур', 'Рамазанович', 'Кузяев', 1),
('Андрей', 'Викторович', 'Кукуяшный', 1),
('Владимир', 'Фёдорович', 'Кулагин', 1),
('Максим', 'Олегович', 'Обухов', 1),
('Игорь', 'Александрович', 'Основин', 1),
('Евгений', 'Владимирович', 'Сахаров', 1),
('Илья', 'Анатольевич', 'Сидоренко', 1),
('Александр', 'Васильевич', 'Соминов', 1),
('Александр', 'Александрович', 'Тимофеев', 1),
('Шердорбек', 'Улугбекович', 'Хасанов', 1),
('Юрий', 'Николаевич', 'Шибаев', 1);
"""

queries = [group_add_query, group_add_query2, student_add_query]

# Делаем через execute() и цикл
# Явно делаем начало транзакции
# cursor.execute("BEGIN")
# for query in queries:
#     try:
#         cursor.execute(query)
#     except Exception as err:
#         print(err)
#         conn.rollback()
#         break
# else:
#     conn.commit()

# Делаем через executmany()

# Определяем коллекцию для добавления данных
groups = [('python315',), ('python316',)]

# Определяем запрос для executemany()
group_add_query = """
-- Добавляем группу в таблицу групп
INSERT INTO groups (group_name) VALUES (?);
"""

# Явно делаем начало транзакции
# cursor.execute("BEGIN")
# try:
#     cursor.executemany(group_add_query, groups)
# except Exception as err:
#     print(err)
#     conn.rollback()
# else:
#     conn.commit()


# Делаем чтение данных из таблицы групп

select_q1 = """
-- Добываем данные из таблицы групп
SELECT * FROM groups;
"""

select_q2 = """
-- Добываем данные из таблицы студентов, подставляя вместо id группы её название
SELECT students.id, students.first_name, students.middle_name, students.last_name, groups.group_name FROM students
JOIN groups ON students.group_id = groups.id;
"""

cursor.execute(select_q2)
q1_result = cursor.fetchall()
pprint(q1_result)
# tabulate print
from tabulate import tabulate
print(tabulate(q1_result, headers=['id', 'first_name', 'middle_name', 'last_name', 'group_name'], tablefmt='grid'))

