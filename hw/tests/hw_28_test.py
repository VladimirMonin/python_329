import pytest

from hw.hw_28 import WeatherRequest


# WEATHER_API_RESPONSE = """{"coord": {"lon": 37.6156, "lat": 55.7522},
#                         "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}],
#                         "base": "stations",
#                         "main": {"temp": 272.51, "feels_like": 269.15, "temp_min": 271.79, "temp_max": 273.28,
#                                  "pressure": 988, "humidity": 95, "sea_level": 988, "grnd_level": 970},
#                         "visibility": 10000, "wind": {"speed": 2.72, "deg": 209, "gust": 6.75}, "clouds": {"all": 100},
#                         "dt": 1703420434,
#                         "sys": {"type": 2, "id": 47754, "country": "RU", "sunrise": 1703397520, "sunset": 1703422735},
#                         "timezone": 10800, "id": 524901, "name": "Москва", "cod": 200}"""
#
#
# # Мокируем приватный метод WeatherRequest __get_response именно ту часть response = requests.get(self.base_url, params=self.params)
# # которая возвращает json
#
# def test_weather_request(mocker):
#     mocker.patch('hw.hw_28.requests.get', return_value='')
#     # Мокируем response.json() и возвращаем WEATHER_API_RESPONSE
#     mocker.patch('hw.hw_28.requests.Response.json', return_value=WEATHER_API_RESPONSE)
#     weather_request = WeatherRequest()
#     assert weather_request('Москва') == WEATHER_API_RESPONSE


# Создаем экземпляр класса WeatherRequest - помещаем это в фикстуру.
# Применяем эту фикстуру для разных тестов

# Обычная фикстура для большинства тестов
@pytest.fixture(scope='module')
def weather_request():
    result = WeatherRequest()('Москва')
    return result


# Список городов и их координаты для параметризации теста с именами городов
cities = [
    ('Москва', {"lon": 37.6156, "lat": 55.7522}),
    ('Воронеж', {"lon": 39.17, "lat": 51.6664}),
    ('Санкт-Петербург', {"lon": 30.2642, "lat": 59.8944}),
    ('Краснодар', {"lon": 38.9747, "lat": 45.0448}),
    ('Сочи', {"lon": 39.7303, "lat": 43.5858}),
]

# Пара

# Тест 1 - проверяем то, что в ответе есть ['sys']['name'] == 'Москва'
def test_weather_request(weather_request):
    assert weather_request['name'] == 'Москва'


# Тест 2 - проверяем что {"coord": {"lon": 37.6156, "lat": 55.7522} в ответе
def test_weather_request_2(weather_request):
    assert weather_request['coord'] == {"lon": 37.6156, "lat": 55.7522}


# Тест 3 - проверяем то, что в "weather" есть ключи id, main, description, icon
def test_weather_request_3(weather_request):
    assert weather_request['weather'][0].keys() == {'id', 'main', 'description', 'icon'}


# Тест 4 - проверяем то, что в "main" есть ключи temp, feels_like, temp_min, temp_max, pressure, humidity
def test_weather_request_4(weather_request):
    main_keys = set(weather_request['main'].keys())
    # проверяем что в "main" есть ключи temp, feels_like, temp_min, temp_max, pressure, humidity
    # через метод issubset
    assert {'temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity'}.issubset(main_keys)
