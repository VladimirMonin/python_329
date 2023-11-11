"""
Lesson 30
11.11.2023

Тема: Повторение всего. Разбор ДЗ по ООП.
- Разбор ДЗ про чтение-запись файлов HW_21.md
"""
import json
from pprint import pprint
from typing import List, Any, Dict, Optional

"""
Домашнее задание 📃
Мы возвращаемся к игре в города! В этот раз мы сделаем её рефакторинг на ООП! Вам пригодится сет городов, который вы получили в виде JSON файла в одной из прошлых реализаций игры.

Я предлагаю вам такую структуру программы. Ниже описана структура классов и методов. Классы желательно оставить в этом же количестве, методы могут называться иначе и работать иначе.

Класс JsonFile: по работе с JSON который мы писали на прошлом занятии. Имеет методы по чтению и записи JSON. Поправьте аннотацию типов (мы читаем сет строк - наши города)

Класс Cities: Этот класс будет использоваться для представления данных о городах из JSON-файла. Он будет содержать список всех городов.

__init__(self, city_data): Конструктор класса Cities, который принимает список городов city_data и инициализирует состояние объекта. В этом конструкторе происходит наполнение городами.
Класс CityGame: Этот класс будет управлять самой игрой. Он будет принимать экземпляр класса Cities в качестве аргумента. Методы класса CityGame включают в себя:

__init__(self, cities): Конструктор класса CityGame, который принимает экземпляр класса Cities и инициализирует состояние игры.

start_game(self): Метод для начала игры, который включает первый ход компьютера.

human_turn(self, city_input): Метод для хода человека, который будет обрабатывать ввод пользователя.

computer_turn(self): Метод для хода компьютера, который будет выбирать город на основе правил игры.

check_game_over(self): Метод для проверки завершения игры и определения победителя.

save_game_state(self): Метод для сохранения состояния игры, если это необходимо.

Управляющий класс GameManager: Этот класс принимает экземпляры классов JsonFile, Cities и CityGame в качестве аргументов. Методы класса GameManager включают в себя:

__call__(self): Метод __call__, который позволяет вызывать объекты этого класса, как если бы они были функциями, и который будет запускать всю игру.

run_game(self): Метод для запуска игры, который будет вызывать методы start_game(), human_turn() и computer_turn() поочередно до завершения игры.

display_game_result(self): Метод для отображения результата игры после завершения. (По желанию. Опционально)

Общие преимущества структуры программы:

Модульность: Каждый класс выполняет свою специфическую функцию, что делает код более модульным и понятным.
Улучшенная читаемость: Хорошо организованный код легче понимать и поддерживать.
Разделение обязанностей: Каждый класс отвечает за свои обязанности, что позволяет изолировать изменения и уменьшить связность между компонентами.
Возможность повторного использования: Классы могут быть повторно использованы в других проектах или частях программы.
Каждый из этих классов выполняет свою роль в системе, что помогает создать более структурированный и поддерживаемый код для вашей игры.

Критерии проверки 👌
Вся работа в одном файле
Работа сдается в виде файла .py
Аннотации типов
Игра запускается вызовом экземпляра класса GameManager
Количество классов соблюдено, методы могут отличаться
Игра запускается в конце документа примерно в такой конструкции
if __name__ == "__main__":
    # Создайте экземпляры необходимых классов
    json_file = JsonFile("data.json")  # Замените "data.json" на имя вашего JSON-файла
    cities = Cities(json_file.read_data())
    game = CityGame(cities)

    # Создайте экземпляр GameManager и вызовите его, чтобы начать игру
    game_manager = GameManager(json_file, cities, game)
    game_manager()

"""


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
        self.cities = cities_list

    def get_cities_list(self) -> set:
        """
        Метод для получения списка городов
        :

        :return:
        """
        return set(self.cities)


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

        self.cities.get_cities_list().remove(self.human_city)
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
                self.cities.get_cities_list().remove(city)
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
    game_manager = GameManager()
    game_manager()
