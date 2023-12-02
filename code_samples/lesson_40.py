"""
Lesson 40
02.12.2023

Тема: Разбор ДЗ по игре в города на ООП - HW_25.md
- Добавление ручной сериализации и валидации данных + dataclass
"""
import json
from pprint import pprint
from typing import List, Any, Dict, Optional


class JsonFileHandler:
    """
    Класс JsonFileHandler
    read_file(filepath, as_dict=False): Метод для чтения данных из JSON файла. Флаг as_dict работает аналогично как в классе CsvFileHandler. Должен быть реализован как метод экземпляра.
    write_file(filepath, data, as_dict=False): Метод для записи данных в JSON файл. Флаг as_dict работает аналогично как в классе CsvFileHandler. Должен быть реализован как метод экземпляра.
    append_file(filepath, data): Метод для дописывания данных в JSON файл. При попытке вызова этого метода должно возникать исключение TypeError с сообщением, что данный тип файла не поддерживает операцию дописывания. Должен быть реализован как метод экземпляра.
    """

    def __init__(self, filepath: str):
        self.data: Optional[None, list] = None
        self.filepath = filepath

    def read_file(self, as_dict=False) -> List[dict] | List[list]:
        """
        Метод для чтения данных из JSON файла.
        Флаг as_dict работает аналогично как в классе CsvFileHandler.
        Должен быть реализован как метод экземпляра.
        :return: List[Dict] | List[List]
        """
        with open(self.filepath, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
            return self.data

    def write_file(self, data: List[dict] | List[list]) -> None:
        """
        Метод для записи данных в JSON файл.
        Флаг as_dict работает аналогично как в классе CsvFileHandler.
        Должен быть реализован как метод экземпляра.
        :param data: List[Dict] | List[List]
        """
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def append_file(self, data: List[list | dict]) -> None:
        """
        Метод для дописывания данных в JSON файл.
        Метод читает содержимое файла в self.data, добавляет в конец файла данные из параметра data и записывает в файл.
        :param data: List[str]
        """
        if not isinstance(data, list):
            raise TypeError('Данный тип файла не поддерживает операцию дописывания')
        self.read_file()
        self.data.extend(data)
        self.write_file(self.data)

    def get_cities_set(self, cities_list: List[dict]) -> set:
        """
        Метод принимает список словарей, формирует из них сет и записывает в JSON файл
        Возвращает сет
        :return:
        """
        cities_set = set()
        for city in cities_list:
            cities_set.add(city['name'])

        # Запись сета в JSON файл с использованием JsonFileHandler
        self.write_file(list(cities_set))
        return cities_set


# Создаем dataclass Cities который в инит создает объект JsonFileHandler и вызывает метод get_cities_set

class Cities:
    """
    Класс Cities
    __init__(self, city_data): Конструктор класса Cities, который принимает список городов city_data и инициализирует состояние объекта. В этом конструкторе происходит наполнение городами.
    """

    def __init__(self, cities_list: list):
        self.cities_set: set = set(cities_list)

    def get_cities_list(self) -> set:
        """
        Метод для получения списка городов
        :

        :return:
        """
        return set(self.cities_set)

    def remove_city(self, city: str) -> None:
        """
        Метод для удаления города из списка
        :param city:
        :return:
        """
        self.cities_set.discard(city)


class CityGame:
    def __init__(self, cities: Cities):
        self.cities = cities
        self.human_city: str = ''
        self.computer_city: str = ''

    def check_game_rules(self, last_city: str, new_city: str) -> bool:
        """
        Метод проверки правил игры
        :param last_city:
        :param new_city:
        :return:
        """
        if last_city[-1].lower() == new_city[0].lower():
            return True
        else:
            return False

    def human_step(self):
        """
        Метод для хода человека
        :return:
        """
        self.human_city = input('Введите город: ')
        if self.human_city == 'стоп':
            print('Вы проиграли')
            return False

        if self.human_city not in self.cities.get_cities_list():
            print(f'Города {self.human_city} нет в списке. Вы проиграли')
            return False

        if self.computer_city:
            if not self.check_game_rules(self.computer_city, self.human_city):
                print(f'Вы проиграли. Ваш ответ не начинается на букву {self.computer_city[-1]}')
                return False

        self.cities.remove_city(self.human_city)
        self.human_city = self.human_city
        return True

    def computer_step(self):
        """
        Метод для хода компьютера
        :return:
        """

        for city in self.cities.get_cities_list():
            # Проверка правил игры методом
            if self.check_game_rules(self.human_city, city):
                print(f'Компьютер называет город: {city}')
                self.computer_city = city
                self.cities.remove_city(city)
                return True

        else:
            print('Вы победили! Компьютер не смог назвать город')
            return False


class GameManager:
    def __init__(self):
        self.json_file = JsonFileHandler('../data/cities_set.json')
        self.cities = Cities(self.json_file.read_file())
        self.game = CityGame(self.cities)

    def __call__(self):
        self.run_game()

    def run_game(self):
        while True:
            if not self.game.human_step():
                break
            if not self.game.computer_step():
                break


if __name__ == "__main__":

    from data.cities import cities
    pprint(cities)