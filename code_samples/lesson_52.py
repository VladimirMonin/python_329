"""
Lesson 52
04.02.2024
- SqlAlchemy 2.0
- Engine
- Connection
- Session
"""
import dataclasses

from sqlalchemy import create_engine, Integer, String, Column, select, update, delete, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

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

"""
Отношения в таблице один к одному
- Один студент может иметь только один юзернейм
- Один юзернейм может принадлежать только одному студенту

Отношения в классе прописываются через 
relationship
"""


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    teacher = Column(String, nullable=False)
    faculty = Column(String, nullable=False)
    # Указываем связь один к одному, и что "username" обратная связь к  "student"
    username = relationship("Username", back_populates="student", uselist=False)


class Username(Base):
    __tablename__ = "username"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("student.id"))
    # Указываем связь один к одному, и что "student" обратная связь к  "username"
    student = relationship("Student", back_populates="username")


# Создание таблицы в базе данных
Base.metadata.create_all(engine)


