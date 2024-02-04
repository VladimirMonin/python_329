"""
Lesson 52
04.02.2024
- SqlAlchemy 2.0
- Engine
- Connection
- Session
"""
import dataclasses

from sqlalchemy import create_engine, Integer, String, Column, select, update, delete
from sqlalchemy.orm import declarative_base, sessionmaker

# Основные сущности SQLAlchemy 2.0
# - Engine - движок, который обеспечивает соединение с базой данных
# - Connection - соединение с базой данных
# - Session - сессия, которая обеспечивает работу с объектами базы данных

# create_engine - создание объекта Engine
# - echo - выводит все SQL-запросы, которые отправляются в базу данных
# - future - поддержка новых возможностей SQLAlchemy 2.0
# DeclareBase - базовый класс для создания моделей
# sessionmaker - создание объекта Session для работы с базой данных
# - autocommit - автоматическое подтверждение транзакций
# - autoflush - автоматическая очистка сессии
# - bind - связь с объектом Engine


# Переменная для хранения URL базы данных (на 1 уровень выше и data/lesson_52.db)
# DATABASE_URL = "sqlite:///lesson_52.db"
DATABASE_URL = "sqlite:///../data/lesson_52.db"

# Создание объекта Engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Определение базового класса для создания моделей
Base = declarative_base()

"""
Таблица student class Student(Base):
- id - целочисленное поле, первичный ключ автоинкрементируемое
- username - строковое поле, уникальное, не может быть пустым
- email - строковое поле, уникальное, не может быть пустым
- password - строковое поле, не может быть пустым
- teacher - строковое поле, не может быть пустым
- faculty - строковое поле, не может быть пустым
"""


# Определение модели Student
class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    teacher = Column(String, nullable=False)
    faculty = Column(String, nullable=False)

    # def __str__(self):
    #     return f"Студент: {self.name} {self.last_name}, {self.faculty}. Юзернейм: {self.username}"


class StudentData:
    id: int
    username: str
    name: str
    last_name: str
    email: str
    password: str
    teacher: str
    faculty: str


# Создание таблицы в базе данных
Base.metadata.create_all(engine)

# Операции CRUD в рамках одной таблицы
# - Create - создание новой записи

"""
Перед тем как мы начнем работать с объектами, необходимо создать сессию
Это можно сделать с помощью объекта Session.

Это открывает соединение с базой данных,
которое будет использоваться для всех операций с базой данных.
"""

# Создание объекта Session
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# with Session() as session:
#     # Создание нового объекта Student
#     student = Student(
#         username="vic007",
#         name="Виктор",
#         last_name="Иванов",
#         email="victor_007@mail.ru",
#         password="123456",
#         teacher="Станислав Козлов",
#         faculty="Информационные технологии")
#
#     # Добавление объекта в сессию
#     session.add(student)
#
#     # Подтверждение транзакции
#     session.commit()

# Добавление нескольких объектов в базу данных
# with Session() as session:
#     students = [
#         Student(
#             username="alex007",
#             name="Алексей",
#             last_name="Смирнов",
#             email="alex@mail.ru",
#             password="123456",
#             teacher="Елена Гудкова",
#             faculty="Информационные технологии")
#     ]
#     session.add_all(students)
#     session.commit()


# Этот запрос без контекстного менеджера whith

# session = Session()
# student = Student(
#     username="vic007",
#     name="Виктор",
#     last_name="Иванов",
#     email="
#     password="123456",
#     teacher="Станислав Козлов",
#     faculty="Информационные технологии")
# session.add(student)
# session.commit()
# session.close()


# - Read - чтение данных
"""
1. Создание движка
2. Создание сессии
3. Формирование запроса
4. Выполнение запроса
5. Получение данных


Для операций чтения данных используется select
Это инструмент появившийся не так давно

stmt = select(Student) - формируем запрос
result = session.execute(stmt) - выполняем запрос
students = result.scalars().all() - получаем результат

scalars - скалярное значение (одно значение)
all - все значения
one - одно значение
first - первое значение
"""
# SELECT * FROM student
# with Session() as session:
#     stmt = select(Student)  # stmt - statement (запрос) FROM student SELECT *
#     result = session.execute(stmt)  # result - результат запроса
#     students = result.scalars().all()  # scalar - скалярное значение (одно значение), all - все значения
#     for student in students:
#         print(student)


# SELECT username name last_name FROM student WHERE faculty = "Информационные технологии"
# SELECT username, name, last_name FROM student WHERE faculty = "Информационные технологии" LIMIT 1 OFFSET 1
# todo Почему идут репры, при выборке всего, но при выборке столбцов идут кортежи?
# todo Получение чистых данных?


# with Session() as session:
#     # stmt = select(Student.username, Student.name, Student.last_name).where(Student.faculty == "Информационные технологии")
#     stmt = select(Student.username, Student.name, Student.last_name).where(
#         Student.faculty == "Информационные технологии").limit(1).offset(1)
#     result = session.execute(stmt)
#     # student = result.all()
#     # students = result.scalars().one() # one даст ошибку если не найдет или больше одного
#     # students = result.first()  # first даст None если не найдет
#     students = result.all()
#     print(students)

# - Update - обновление данных
"""
Для обновления данных используется метод update
stmt = update(Student).where(Student.username == "vic007").values(username="victor007")
values - значения, которые будут обновлены
result = session.execute(stmt)

"""

# with Session() as session:
#     stmt = update(Student).where(Student.username == "vic007").values(username="victor007")
#     result = session.execute(stmt)
#     session.commit()
#
#     # Прочитаем и проверим
#     stmt = select(Student.name, Student.username).where(Student.username == "victor007")
#     result = session.execute(stmt)
#     students = result.all()
#     print(students)
#
#     # Добавим еще одного студента
#     student = Student(
#         username="yar007",
#         name="Ярослав",
#         last_name="Иванов",
#         email="yarik12@yandex.ru",
#         password="123456",
#         teacher="Станислав Козлов",
#         faculty="Информационные технологии")
#
#     session.add(student)
#     session.commit()


# - Delete - удаление данных


"""
Для удаления данных используется метод delete
stmt = delete(Student).where(Student.username == "yar007")
"""

# with Session() as session:
#     # Читаем всех студентов поля имя, фамилия, юзернейм
#     stmt = select(Student.name, Student.last_name, Student.username)
#     result = session.execute(stmt)
#
#     students = result.all()
#     print(students)
#
#     # Удаляем студента
#     stmt = delete(Student).where(Student.username == "yar007")
#     result = session.execute(stmt)
#     session.commit()
#
#     # Читаем всех студентов поля имя, фамилия, юзернейм
#     stmt = select(Student.name, Student.last_name, Student.username)
#     result = session.execute(stmt)
#     students = result.all()
#
#     print(students)