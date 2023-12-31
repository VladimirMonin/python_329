"""
Подготовка базы данных SQLite3 из xls файлов дампа реальной базы данных 2ГИС за 2023 год.

На входе папка с файлами xlsx, у всех файлов одинаковая структура, но разные данные (по регионам).

Поля таблицы:
ID	Название	Регион	Район	Город	Район города	Адрес	Индекс	Телефон	Мобильный телефон	Email
Сайт	Рубрика	Подрубрика	Время работы	Способы оплаты	whatsapp	viber	telegram	facebook
instagram	vkontakte	odnoklassniki	youtube	twitter	skype	icq	googleplus	linkedin	pinterest	Широта	Долгота

На выходе база данных SQLite3 с таблицей 2gis_businesses

Используется библиотека openpyxl для чтения данных из файлов xlsx
А также библиотека SQLAlchemy для работы с базой данных SQLite3

Рекурсивный обход директорий и поиск файлов xlsx, с последующим сохранением данных в базу данных SQLite3

Используется генератор для построчного чтения данных из файла xlsx, чтобы не хранить все данные в памяти.
"""

from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import openpyxl

FOLDER_PATH = r"C:\1"

Base = declarative_base()  # Базовый класс для создания моделей


class Business(Base):
    """
    Модель для таблицы 2gis_businesses

    """
    __tablename__ = '2gis_businesses'
    id = Column(Integer, primary_key=True, autoincrement=True)  # Внутренний ID
    gis_id = Column(Integer, nullable=True)  # ID из файла, может быть пустым
    name = Column(String, nullable=False)
    region = Column(String, nullable=True)
    district = Column(String, nullable=True)
    city = Column(String, nullable=True)
    city_district = Column(String, nullable=True)
    address = Column(String, nullable=True)
    index = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    mobile_phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    website = Column(String, nullable=True)
    category = Column(String, nullable=True)
    subcategory = Column(String, nullable=True)
    working_hours = Column(String, nullable=True)
    payment_methods = Column(String, nullable=True)
    whatsapp = Column(String, nullable=True)
    viber = Column(String, nullable=True)
    telegram = Column(String, nullable=True)
    facebook = Column(String, nullable=True)
    instagram = Column(String, nullable=True)
    vkontakte = Column(String, nullable=True)
    odnoklassniki = Column(String, nullable=True)
    youtube = Column(String, nullable=True)
    twitter = Column(String, nullable=True)
    skype = Column(String, nullable=True)
    icq = Column(String, nullable=True)
    googleplus = Column(String, nullable=True)
    linkedin = Column(String, nullable=True)
    pinterest = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)


# Создание соединения с базой данных
engine = create_engine('sqlite:///businesses.db')
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()


def process_workbook(workbook_path: str):
    """
    Функция для построчного чтения данных из файла xlsx
    :param workbook_path:
    :return:
    """
    # Открытие файла xlsx
    workbook = openpyxl.load_workbook(workbook_path, read_only=True)
    sheet = workbook.active

    # Использование генератора для построчного чтения данных из файла xlsx
    for row in sheet.iter_rows(min_row=2, values_only=True):  # пропускаем заголовок
        if all(value is None for value in row):  # Если вся строка пуста, прерываем чтение
            break

        business = Business(
            gis_id=row[0].replace('=', '').replace("'", '').replace('"', '').strip(),
            name=row[1],
            region=row[2],
            district=row[3],
            city=row[4],
            city_district=row[5],
            address=row[6],
            index=row[7],
            phone=row[8],
            mobile_phone=row[9],
            email=row[10],
            website=row[11],
            category=row[12],
            subcategory=row[13],
            working_hours=row[14],
            payment_methods=row[15],
            whatsapp=row[16],
            viber=row[17],
            telegram=row[18],
            facebook=row[19],
            instagram=row[20],
            vkontakte=row[21],
            odnoklassniki=row[22],
            youtube=row[23],
            twitter=row[24],
            skype=row[25],
            icq=row[26],
            googleplus=row[27],
            linkedin=row[28],
            pinterest=row[29],
            latitude=row[30],
            longitude=row[31]

        )
        yield business


def write_log(workbook_path: str, error: str):
    """
    Функция записи ошибок в лог-файл txt
    :param workbook_path:
    :param error:
    :return:
    """
    with open('errors.txt', 'a', encoding='utf-8') as f:
        f.write(f'Ошибка при сохранении данных из файла {workbook_path}: {error}\n')


def save_to_database(workbook_path: str):
    """
    Функция сохранения данных из файла xlsx в базу данных SQLite3
    :param workbook_path:
    :return:
    """
    try:
        for business in process_workbook(workbook_path):
            session.add(business)
        session.commit()
    except Exception as e:
        print(f'Ошибка при сохранении данных из файла {workbook_path}: {e}')
        write_log(workbook_path, e)
        session.rollback()  # Откатываем транзакцию в случае ошибки


def main():
    """
    Основная функция
    :return:
    """
    # Рекурсивный обход директорий и поиск файлов xlsx
    for root, dirs, files in os.walk(FOLDER_PATH):  # Замените '.' на вашу стартовую директорию
        for file in files:
            if file.endswith('.xlsx'):
                workbook_path = os.path.join(root, file)
                save_to_database(workbook_path)

    # Закрываем сессию
    session.close()


if __name__ == '__main__':
    main()
