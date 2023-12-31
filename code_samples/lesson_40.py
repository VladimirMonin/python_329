"""
Lesson 40
02.12.2023

Тема: Разбор ДЗ по игре в города на ООП - HW_25.md
- Добавление ручной сериализации и валидации данных + dataclass
"""
import json
from dataclasses import dataclass, field
from pprint import pprint
from typing import List, Any, Dict, Optional, Set


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


@dataclass(order=True)
class City:
    """
    Датакласс City. Содержит данные:
    Название города
    Субъект РФ
    Население
    Доступна сортировка по названию города. Для остальных полей сортировка не доступна
    """
    name: str
    subject: str = field(compare=False)
    population: int = field(compare=False)


class DataValidator:
    """
    Класс DataValidator для проверки и корректировки данных.
    Методы класса должны:
    Определить "плохие" буквы, на которые не начинаются названия городов, исключая такие города из датасета.
    Проверить тип данных для каждого поля (название города - строка, население - число).
    Привести название города к формату с заглавной буквы, если требуется.
    """
    #TODO Не работает проверка плохих букв!
    def __init__(self, cities_list: List[dict]):
        self.cities_list = cities_list
        self.bad_letters: set = self.get_bad_letters_from_cities_list()
        print(f'Плохие буквы: {self.bad_letters}')

    def get_bad_letters_from_cities_list(self) -> set:
        """
        Метод для получения списка плохих букв
        :return:
        """

        first_letters = set()
        last_letters = set()

        for city in self.cities_list:
            first_letters.add(city['name'][0].lower())
            last_letters.add(city['name'][-1].lower())

        bad_cities_set = last_letters - first_letters
        return bad_cities_set

    def check_city_name(self, city_name: str) -> bool:
        """
        Метод проверки названия города
        :param city_name:
        :return:
        """
        if city_name[0].lower() in self.bad_letters:
            return False
        else:
            return True

    def check_city_population(self, city_population: int) -> bool:
        """
        Метод проверки населения города
        :param city_population:
        :return:
        """
        if not isinstance(city_population, int):
            return False
        else:
            return True

    def check_city_name_case(self, city_name: str) -> str:
        """
        Метод проверки регистра названия города
        :param city_name:
        :return:
        """
        if city_name.islower():
            return city_name.title()
        else:
            return city_name

    def validate_data(self) -> List[dict]:
        """
        Метод валидации данных
        :return:
        """
        validated_data = []
        for city in self.cities_list:
            if self.check_city_name(city['name']) and self.check_city_population(city['population']):
                city['name'] = self.check_city_name_case(city['name'])
                validated_data.append(city)
        return validated_data


class DataSerializer:
    """
    Класс DataSerializer для десериализации данных из JSON.
    Использует DataValidator для проверки данных.
    Экземпляр класса DataSerializer должен принимать в конструкоре экземпляр JsonFileHandler а так же экземпляр DataValidator.
    Метод get_validated_data должен возвращать список словарей с валидными данными.
    """

    def __init__(self, json_file_handler: JsonFileHandler, data_validator: DataValidator):
        self.json_file_handler = json_file_handler
        self.data_validator = data_validator
        self.__row_data: List[dict] = self.json_file_handler.read_file()
        self.__validated_data: List[dict] = self.data_validator.validate_data()
        self.serialize_data: List[City] = self.serialize_data()

    def serialize_data(self) -> List[City]:
        """
        Метод сериализации данных
        :return:
        """
        return [City(**city) for city in self.__validated_data]


"""
4. **Интеграция десериализации в игру**:
   - Измените логику игры так, чтобы она использовала десериализованные данные. При загрузке игры, данные должны проходить через валидацию и десериализацию.
   - Результатом должен быть список объектов `City`, используемых в игре.
"""


class CityGame:
    def __init__(self, cities_obj: List[City]):
        self.cities = cities_obj
        self.cities_set: Set[str] = {city.name for city in self.cities}
        self.human_city: str = ''
        self.computer_city: str = ''

    @staticmethod
    def check_game_rules(last_city: str, new_city: str) -> bool:
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

        if self.human_city not in self.cities_set:
            print(f'Города {self.human_city} нет в списке. Вы проиграли')
            return False

        if self.computer_city:
            if not self.check_game_rules(self.computer_city, self.human_city):
                print(f'Вы проиграли. Ваш ответ не начинается на букву {self.computer_city[-1]}')
                return False

        self.cities_set.remove(self.human_city)
        self.human_city = self.human_city

        return True

    def computer_step(self):
        """
        Метод для хода компьютера
        :return:
        """
        for city in self.cities:
            if city.name[0].lower() == self.human_city[-1].lower():
                self.computer_city = city.name
                self.cities_set.remove(self.computer_city)
                print(f'Компьютер назвал город {self.computer_city}')
                return True
        print('Вы выиграли. Компьютер не смог назвать город')
        return False


class GameManager:
    def __init__(self, json_file_handler: JsonFileHandler, data_validator: DataValidator,
                 data_serializer: DataSerializer, city_game_obj: CityGame):
        self.json_handler_obj: JsonFileHandler = json_file_handler
        self.data_validator_obj: DataValidator = data_validator
        self.data_serializer_obj: DataSerializer = data_serializer
        self.cities: List[City] = self.data_serializer_obj.serialize_data
        self.game: CityGame = city_game_obj

    def __call__(self):
        self.run_game()

    def run_game(self):
        while True:
            if not self.game.human_step():
                break
            if not self.game.computer_step():
                break


if __name__ == "__main__":
    json_file_handler = JsonFileHandler('../data/cities.json')
    data_validator = DataValidator(json_file_handler.read_file())
    data_serializer = DataSerializer(json_file_handler, data_validator)
    game = CityGame(data_serializer.serialize_data)
    game_manager = GameManager(json_file_handler, data_validator, data_serializer, game)
    game_manager()
