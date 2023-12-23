"""

# Домашнее задание 📃

**"Погодный Аналитик с Marshmallow и Dataclasses"**

### Краткое содержание
В этом задании Вы будете работать с реальными данными погоды, используя Python. Ваша задача – написать программу, которая
запрашивает данные о погоде с использованием предоставленного API, анализирует их и сохраняет
структурированно. Вы будете использовать dataclasses для структурирования данных и библиотеку
Marshmallow для валидации и сериализации.

### Описание Задания
1. **Использование API для получения погодных данных:**
   - Используйте предоставленный код для запроса данных о погоде с OpenWeatherMap API.

```python
import requests

def get_weather(city_name):
    api_key = "ВАШ_API_КЛЮЧ" # Можете взять мой. 23496c2a58b99648af590ee8a29c5348
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'lang': 'ru',
        'units': 'metric',
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    return response.json()

# Пример использования
city = "Москва"
weather_data = get_weather(city)
print(weather_data)

```


2. **Создание Dataclass `CurrentWeather`:**
   - Определите датакласс `CurrentWeather`, включающий интересные Вам поля из ответа API. Некоторые поля должны быть обязательными, другие – необязательными.

3. **Реализация схемы Marshmallow:**
   - На основе датакласса `CurrentWeather` создайте схему Marshmallow.
   - Расширьте созданную схему, добавив в неё дополнительные проверки (например, проверка на диапазон значений, формат даты).

4. **Генерация JSON Schema:**
   - Используйте библиотеку `marshmallow_jsonschema` для преобразования вашей схемы Marshmallow в JSON Schema.
   - Сохраните сгенерированную схему в файл.

5. **Творческий аспект:**
   - Выбор полей для датакласса и методов проверки остаётся за Вами. Будьте творческими и выберите те поля, которые считаете наиболее интересными и показательными.


### Примерная Структура Кода
```python
# Импорты и определение классов/схем здесь

# Здесь код для запроса данных о погоде и их обработки (пользовательский ввод через инпут)

# Создание экземпляра датакласса

# Валидация и сериализация данных с помощью Marshmallow

# Генерация и сохранение JSON Schema

# Вывод погоды в терминал

if __name__ == "__main__":
    validate_it = Validate()
    validate_it()
```

Это задание предназначено для развития навыков работы с внешними API, обработки и валидации данных, а также работы с сериализацией. Удачи!

# Критерии проверки 👌

- Чистота и структура кода.
- Эффективное использование dataclasses.
- Корректное применение библиотек marshmallow, marshmallow_dataclass и marshmallow_jsonschema.
- Работа сдается в виде одного файла .py.
- При запуске кода
	- запрос города
	- получение данных
	- валидация данных
	- десериализация данных
	- отображение погоды в городе
	- должна генерироваться JSON Schema (опционально: можете сделать проверку, если файл уже есть - чтобы он не писался)
- Хорошая документация (модуль, т.е. файл + классы + методы)

"""
import json
import os
from dataclasses import dataclass
from pprint import pprint
from typing import List

from marshmallow import Schema, fields, ValidationError, validate
from marshmallow_dataclass import class_schema

from marshmallow_jsonschema import JSONSchema

import requests


class WeatherRequest:
    def __init__(self):
        self.city_name = None
        self.api_key = "23496c2a58b99648af590ee8a29c5348"
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.params = {
            'q': None,
            'lang': 'ru',
            'units': 'metric',
            'appid': self.api_key
        }
        self.__response = None

    def __str__(self):
        return f'{self.weather_data}'

    def __get_response(self):
        response = requests.get(self.base_url, params=self.params)
        self.__response = response.json()

    def __call__(self, city_name):
        self.city_name = city_name
        self.params['q'] = self.city_name
        self.__get_response()
        return self.__response


@dataclass
class CurrentWeather:
    city_name: str
    temp: float
    feels_like: float
    description: str
    visibility: int
    pop: float = None

    def __str__(self):
        return f'Погода в городе {self.city_name}:\n' \
               f'Температура: {self.temp}°C\n' \
               f'Ощущается как: {self.feels_like}°C\n' \
               f'Описание: {self.description}\n' \
               f'Видимость: {self.visibility} м\n' \
               f'Вероятность осадков: {self.pop}'


# Создаем экземпляр схемы на основе датакласса
BaseCurrentWeatherSchema = class_schema(CurrentWeather)


# Создание расширенной схемы, на основе базовой схемы
# Дополнительные проверки

class CurrentWeatherSchema(BaseCurrentWeatherSchema):
    city_name = fields.Str(required=True, validate=validate.Length(min=2, max=80))
    temp = fields.Float(required=True, validate=validate.Range(min=-80, max=80))
    feels_like = fields.Float(required=True, validate=validate.Range(min=-80, max=80))
    description = fields.Str(required=True, validate=[
        validate.Length(min=2, max=80),
        validate.Regexp(r'^[А-Яа-яЁёA-Za-z0-9\s]+$')
    ])
    visibility = fields.Int(required=True, validate=validate.Range(min=0, max=10000))
    pop = fields.Float(required=False, validate=validate.Range(min=0, max=1))


def main():
    # Запрашиваем у пользователя город
    city = input('Введите город: ')

    # Создаем экземпляр класса WeatherRequest (запрос)
    weather_request = WeatherRequest()
    # Отправляем запрос
    weather_data = weather_request(city)
    # pprint(weather_data)

    # Обрабатываем сырой ответ и получаем нужные нам данные
    weather_data = {
        'city_name': weather_data['name'],
        'temp': weather_data['main']['temp'],
        'feels_like': weather_data['main']['feels_like'],
        'description': weather_data['weather'][0]['description'],
        'visibility': weather_data['visibility']
    }

    # Создаем базовую схему
    base_schema = BaseCurrentWeatherSchema()
    # Создаем расширенную схему
    schema = CurrentWeatherSchema()

    # проверяем, существует ли файл схемы hw_28_schema.json

    if not os.path.exists('hw_28_schema.json'):
        # Сохраняем схему в файл hw_28_schema.json indent 4 ensure_ascii=False
        schema_file = JSONSchema()

        with open('hw_28_schema.json', 'w', encoding='utf-8') as f:
            json.dump(schema_file.dump(schema), f, indent=4, ensure_ascii=False)

    # Валидируем и десериализуем данные. Выводим полученные данные в терминал
    try:
        result = schema.load(weather_data)
        print(result)
    except ValidationError as err:
        print(err.messages)


main()
