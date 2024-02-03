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

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение URL базы данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)
# sqlite:///root/data/base.db
# postgresql://user:password@localhost:5432/db_name
# mysql://user:password@localhost:3306/db_name