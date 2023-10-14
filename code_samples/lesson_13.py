# Lesson 13 (25-26)
# Повторяем словари

# Словарь. Dictionary. dict
# Словарь - это структура данных, которая хранит данные в виде пары ключ-значение
# Словарь - это изменяемый тип данных
# Словарь - это неупорядоченная структура данных
# Словарь - это структура данных, которая может хранить в себе любые типы данных
# Ключами словаря могут быть только неизменяемые типы данных (строка, число, кортеж)
# Значениями словаря могут быть любые типы данных

# some_dict = {}  # Пустой словарь (пустой dict)
# some_dict1 = dict()  # Пустой словарь (пустой dict)

# Пример простого словаря

# shop_dict = {'молоко': 1,
#              'хлеб': 2,
#              'яйца': 10,
#              'сыр': 1,
#              'колбаса': 1}

# pprint(shop_dict)

# Добавление элементов в словарь

# user_input = input('Введите название продукта'
#                    ' и количество через пробел: ').split()
#
# shop_dict.update({user_input[0]: int(user_input[1])})
# shop_dict[user_input[0]] = int(user_input[1])
#
# pprint(shop_dict)

# Методы словаря

# .get() - получение значения по ключу
# .values() - получение всех значений словаря
# .keys() - получение всех ключей словаря
# .items() - получение всех пар ключ-значение словаря
# .pop() - удаление элемента по ключу

# shop_dict_keys = shop_dict.keys()
# shop_dict_values = shop_dict.values()
# shop_dict_items = shop_dict.items()
#
# print(shop_dict_keys)
# print(shop_dict_values)
# print(shop_dict_items)
#
# print(type(shop_dict_keys))
# print(type(shop_dict_values))
# print(type(shop_dict_items))
#
# # print(full_dict[1]['title'])
#
# for key, value in full_dict.items():
#     # print(key)
#     # print(value['title'])
#     print(f'{key}) {value["title"]}')
#
# films_title = [value['title'] for value in full_dict.values()]
# print(films_title)
#
# # Выводим названия фильмов films_title + enumerate
# for index, film in enumerate(films_title, 1):
#     print(f'{index}) {film}')


# first_name = 'John'
# second_name = first_name
#
# print(id(first_name))
# print(id(second_name))
#
# shop_dict = {'молоко': 1,
#               'хлеб': 2,
#               'яйца': 10,
#               'сыр': 1,
#               'колбаса': 1}
#
#
# keys_shop_list = list(shop_dict.keys())
# value_shop_list = list(shop_dict.values())
#
# print(keys_shop_list)
# print(value_shop_list)
#
# # Объединяем 2 списка в словарь без функции zip
# shop_dict = {}
# for index in range(len(keys_shop_list)):
#     shop_dict[keys_shop_list[index]] = value_shop_list[index]
#
# print('Это результат работы цикла for')
# pprint(shop_dict)
#
# # Объединяем 2 списка в словарь с функцией zip
# shop_dict = dict(zip(keys_shop_list, value_shop_list))
# print('Это результат работы функции zip')
# pprint(shop_dict)
#
#
# marvel_2 = full_dict = {
#     1: {
#         'title': 'Железный человек',
#         'year': 2008,
#         'director': 'Джон Фавро',
#         'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
#         'producer': 'Ави Арад и Кевин Файги',
#         'stage': 'Первая фаза',
#         'actors': {
#             'Роберт Дауни мл.': ['Железный человек', 'Авенджеры', 'Шерлок Холмс'],
#             'Гвинет Пэлтроу': ['Железный человек', 'Итальянец', 'Изабелла'],
#             'Джефф Бриджес': ['Железный человек', 'Крушители', 'Лев'],
#         }
#     },
#     2: {
#         'title': 'Невероятный Халк',
#         'year': 2008,
#         'director': 'Луи Летерье',
#         'screenwriter': 'Зак Пенн',
#         'producer': 'Ави Арад, Гейл Энн Хёрд и Кевин Файги',
#         'stage': 'Первая фаза',
#         'actors': {
#             'Эдвард Нортон': ['Невероятный Халк', 'Бердмэн', 'Иллюзия обмана'],
#             'Лив Тайлер': ['Невероятный Халк', 'Властелин колец', 'Армагеддон'],
#             'Тим Рот': ['Невероятный Халк', 'Правдивая ложь', 'Молчание ягнят']
#         }
#     },
#     3: {
#         'title': 'Железный человек 2',
#         'year': 2010,
#         'director': 'Джон Фавро',
#         'screenwriter': 'Джастин Теру',
#         'producer': 'Кевин Файги',
#         'stage': 'Первая фаза',
#         'actors': {
#             'Роберт Дауни мл.': ['Железный человек', 'Железный человек 2', 'Другие фильмы'],
#             'Джонни Депп': ['Железный человек 2', 'Пираты Карибского моря', 'Алиса в Зазеркалье'],
#             'Гвинет Пэлтроу': ['Железный человек', 'Железный человек 2', 'Другие фильмы', 'Первый мститель',]
#         }
#     },
#     4: {
#         'title': 'Тор',
#         'year': 2011,
#         'director': 'Кеннет Брана',
#         'screenwriter': 'Эшли Эдвард Миллер и Зак Стенц, Дон Пейн',
#         'producer': 'Нет данных',
#         'stage': 'Первая фаза',
#         'actors': {
#             'Крис Хемсворт': ['Тор', 'Мстители: Финал', 'Охотники за привидениями'],
#             'Натали Портман': ['Тор', 'Черный лебедь', 'Звездные войны. Эпизод I: Скрытая угроза'],
#             'Том Хиддлстон': ['Тор', 'Авенджеры', 'Многоликий дьявол', 'Первый мститель']
#         }
#     },
#     5: {
#         'title': 'Первый мститель',
#         'year': 2011,
#         'director': 'Джо Джонстон',
#         'screenwriter': 'Кристофер Маркус и Стивен Макфили',
#         'producer': 'Нет данных',
#         'stage': 'Первая фаза',
#         'actors': {
#             'Крис Эванс': ['Первый мститель', 'Мстители: Война бесконечности', 'Тачки'],
#             'Хейли Атвелл': ['Первый мститель', 'Призрачный патруль', 'Мамы'],
#             'Себастьян Стэн': ['Первый мститель', 'Черепашки-ниндзя', 'Логан']
#         }
#     }
# }
# print(marvel_2[5]['actors']['Себастьян Стэн'][0])
# films_title = 'Первый мститель'
# # ДОБЫТЬ ИМЕНА АКТЕРОВ КОТОРЫЕ ИГРАЛИ В films_title, ДАЖЕ ИЗ ДРУГИХ ФИЛЬМОВ
# actors_lst = []
# for value in marvel_2.values():
#     # pprint(value)
#     # print(type(value))
#     for key_2, value_2 in value.items():
#         pprint(key_2)
#         # pprint(value_2)
#         if key_2 == 'actors':
#             for key_3, value_3 in value_2.items():
#                 if films_title in value_3:
#                     actors_lst.append(key_2)

# print(actors_lst)


# actor_films = [
#     {
#         'actor': 'Роберт Дауни мл.',
#         'films': ['Железный человек', 'Авенджеры', 'Шерлок Холмс', 'Железный человек 2', 'Другие фильмы']
#     },
#     {
#         'actor': 'Гвинет Пэлтроу',
#         'films': ['Железный человек', 'Молчание котят', 'Изабелла', 'Железный человек 2', 'Другие фильмы']
#     },
#     {
#         'actor': 'Джефф Бриджес',
#         'films': ['Железный человек', 'Крушители', 'Молчание котят', 'Другие фильмы']
#     },
#     {
#         'actor': 'Эдвард Нортон',
#         'films': ['Невероятный Халк', 'Бердмэн', 'Молчание котят', 'Другие фильмы']
#     },
#     {
#         'actor': 'Лив Тайлер',
#         'films': ['Невероятный Халк', 'Властелин колец', 'Армагеддон', 'Другие фильмы']
#     },
#     {
#         'actor': 'Тим Рот',
#         'films': ['Невероятный Халк', 'Правдивая ложь', 'Молчание котят', 'Другие фильмы']
#     },
# ]
# film_title = 'Молчание котят'
# ИЩЕМ АКТЕРОВ КОТОРЫЕ ИГРАЛИ в ФИЛЬМЕ film_title

# actors_lst = []
#
# for item in actor_films:
#     if film_title.lower() in [film.lower() for film in item['films']]:
#         actors_lst.append(item['actor'])
#
# # Однострочник с генератором
# actors_lst2 = [item['actor'] for item in actor_films if film_title.lower() in [film.lower() for film in item['films']]]
# actors_lst3 = [item['actor'] for item in actor_films if film_title in item['films']]
#
# print(', '.join(actors_lst))
# print(actors_lst2)
# print(actors_lst3)

# Pyinstaller - упаковщик Python-программ в исполняемые файлы для Windows, Linux, Mac OS X, FreeBSD, Solaris и AIX.
# pip install pyinstaller
# pip freeze > requirements.txt
# pip install -r requirements.txt

# pyinstaller
# documantation - https://pyinstaller.readthedocs.io/en/stable/

# pyinstaller -F main.py

print('Hello world!')
input('Нажмите Enter для выхода из программы')