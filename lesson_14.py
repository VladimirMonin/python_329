# Рефакторинг кода - процесс, при котором улучшается читабельность кода, но не меняется его функциональность.
# Рефакторинг кода - это не изменение функциональности, а улучшение кода.
import json
from pprint import pprint


# АЛГОРИТМ РАБОТЫ ИГРЫ ГОРОДА
# Чтение файла с городами
# Чтение файла с результатами прошлых игр (если он есть)

# Пользователь вводит город ПРОВЕРКИ
# Поиск по списку
# Проверка на последнюю букву (Если это не первый ход игры)
# Проверка на "плохую букву"


# Если есть, то программа выводит город, который начинается на последнюю букву введенного города
# Если такого города нет, то программа сообщает что игрок проиграл и игра завершается
# Ход компьютера ПРОВЕРКИ
# Поиск по списку
# Проверка на последнюю букву
# Проверка на "плохую букву"
# Круг повторяется пока кто-то не проиграет
# Запись результата в файл

# ИГРА ГОРОДА - СКРИПТОВАЯ ВЕРСИЯ

# MSG_USER_STOP = 'Пользователь проиграл. Ввод слова СТОП'
# MSG_BAD_FIRST_LETTER = 'Пользователь проиграл. Вы назвали город, ошибившись на первой букве'
# MSG_BAD_CITY = 'Пользователь проиграл. Такого города нет'
# MSG_USER_WIN = 'Пользователь победил. Компьютер не знает больше городов'
# LOG_FILE = 'game_log.txt'
#
# def read_json():
#     """Функция читает JSON с городами и возвращает список городов"""
#     pass
#
#
# def get_bad_first_letters():
#     """Функция возвращает сет плохих первых букв"""
#     pass
#
#
# def check_is_bad_first_letter():
#     """Функция проверяет является ли буква плохой"""
#     pass
#
#
# def check_is_letters_match():
#     """Функция проверяет соответствие букв"""
#     pass
#
#
# # Чтение файла с городами cities_set.json флаг r - read парсим json в питоновский объект
#
# with open('cities_set.json', 'r', encoding='utf-8') as file:
#     cities_set = json.load(file)
#
# cities_set = set(cities_set)
#
# # Формируем сет первых букв городов
# first_letters_set = set()
# last_letters_set = set()
#
# for city in cities_set:
#     first_letters_set.add(city[0].lower())
#     last_letters_set.add(city[-1].lower())
#
# print(f'{first_letters_set=}')
# print(f'{last_letters_set=}')
#
# # Формируем сет плохих последних букв через разницу множеств
# bad_last_letters_set = last_letters_set - first_letters_set
#
# print(f'{bad_last_letters_set=}')
#
# computer_city = None
#
# while True:
#     # Ход человека
#     human_city = input('Введите город: ')
#     # Проверка на плохую букву
#     if human_city[-1] in bad_last_letters_set:
#         print(f'Пожалуйста выберите другую букву. На букву{human_city[-1]} нет городов')
#         continue
#
#     # Проверка на стоп
#     if human_city == 'стоп':
#         print(MSG_USER_STOP)
#         # TODO Сделать запись результата игры в файл
#         break
#
#     # Проверка на соответствие букв
#     if computer_city:
#         if human_city[0].lower() != computer_city.lower()[-1]:
#             print(f'Вы проиграли. Ваш ответ не начинается на букву {computer_city[-1]}')
#             # TODO Сделать запись результата игры в файл
#             break
#
#     # Проверка на существование города
#     if human_city not in cities_set:
#         print(MSG_BAD_CITY)
#         # TODO Сделать запись результата игры в файл
#         break
#
#     # Удаляем город из сета
#     cities_set.remove(human_city)
#
#     # Ход машины
#     for city in cities_set:
#         if city[0].lower() == human_city[-1].lower() and city[0].lower() not in bad_last_letters_set:
#             computer_city = city
#             print(f'Мой город {computer_city}')
#             cities_set.remove(computer_city)
#             break
#     else:
#         print(MSG_USER_WIN)
#         # TODO Сделать запись результата игры в файл
#         break


# def main():
#     print('Игра начинается')
#     # while True:
#     #     # Функция
#     #     # Переменная = функция2
#     #     # Перменная2 = функция3(пеменная)
#     #     # проверка if функция(переменная2):
#     #     # принт
#     #
#     #     pass


# ЭКСПЕРИМЕНТЫ С __name__
# 1. Функция main - которая печатает "Привет, я main() и вызываюсь из файла
# {__name__}

# 2. Вызовите её

def main():
    print(f'Привет, я main() и вызываюсь из файла {__name__}')


main()
# 3. Создайте ещё один файл. Импортируйте в него файл с функцией main import название файла
# 4. Запустите файл с импортом

# 5. Вернитесь в первый файл. Обверните вызов функции main
if __name__ == '__main__':
    main()

#6. Попробуйте сделать запуск в обоих файлах