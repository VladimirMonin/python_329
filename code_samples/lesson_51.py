"""
Lesson 51 - Знакомство с SQLAlchemy 2.0
- Понятие ORM
- Основные сущности SQLAlchemy 2.0
- Разница между SQLAlchemy 1.4 и 2.0
- Установка и настройка SQLAlchemy 2.0
- pip install sqlalchemy python-dotenv
- Переменные окружения

"""

# ORM - Object-Relational Mapping - объектно-реляционное отображение
# Позволяет использовать объекты в коде для работы с данными в базе данных

# Основные сущности SQLAlchemy 2.0
# - Engine - движок, который обеспечивает соединение с базой данных
# - Connection - соединение с базой данных
# - Session - сессия, которая обеспечивает работу с объектами базы данных


import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, Integer, select
from sqlalchemy.orm import sessionmaker, declarative_base

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение URL базы данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)
# sqlite:///root/data/base.db
# postgresql://user:password@localhost:5432/db_name
# mysql://user:password@localhost:3306/db_name

"""
Почему важно хранить данные в переменных окружения?
- Безопасность
- Переносимость
- Удобство использования
- Отладка

"""

# create_engine - создание объекта Engine
# - echo - выводит все SQL-запросы, которые отправляются в базу данных
# - future - поддержка новых возможностей SQLAlchemy 2.0
# DeclareBase - базовый класс для создания моделей
# sessionmaker - создание объекта Session для работы с базой данных
# - autocommit - автоматическое подтверждение транзакций
# - autoflush - автоматическая очистка сессии
# - bind - связь с объектом Engine


# Создание объекта Engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Определение базового класса для создания моделей
Base = declarative_base()

# Создание объекта Session
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Пример модели
class User(Base):
    """
    Модель пользователя
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)


# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

with Session() as session:
    # Создание пользователя
    # INSERT INTO users (name, age) VALUES ('John', 30)
    # user = User(name="John", age=30)
    # session.add(user)
    # session.commit()


    # Получение первого пользователя из базы данных
    stmt = select(User)
    result = session.execute(stmt)
    user1 = result.scalars().first()

    # Получение всех пользователей
    stmt = select(User)
    result = session.execute(stmt)
    users1 = result.scalars().all()

    # Получение первых 10 пользователей
    stmt = select(User).limit(10)
    result = session.execute(stmt)
    users2 = result.scalars().all()

    # Получение пользователей с именем John
    stmt = select(User).where(User.name == "John")
    result = session.execute(stmt)
    users3 = result.scalars().all()

    # Получение пользователей с именем John и возрастом 30
    stmt = select(User).where(User.name == "John", User.age == 30)
    result = session.execute(stmt)
    users4 = result.scalars().all()

    # Получение только возраста
    stmt = select(User.name, User.age).where(User.age == 30)
    result = session.execute(stmt)
    users5 = result.scalars().all()

print(f'User ID: {user1.id}, Name: {user1.name}, Age: {user1.age}')

for user in users1:
    print(f'User ID: {user.id}, Name: {user.name}, Age: {user.age}')

for user in users2:
    print(f'User ID: {user.id}, Name: {user.name}, Age: {user.age}')

for user in users3:
    print(f'User ID: {user.id}, Name: {user.name}, Age: {user.age}')