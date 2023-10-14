# LESSON 21-22
# Изучаем Match case и смотрим примеры
# Аналог switch case из других языков, или elif из питона
#
# cmd = 'top'
#
# match cmd:
#     case 'top':
#         print('вверх')
#     case _: # Условный else - все что не top
#         print('неизвестная команда')
#
# match cmd:  # должен быть хотя бы один case
#     case 'top' | 'right':
#         print('вверх или право')
#     case 'left':
#         print('влево')
#     case 'top':
#         print('вверх опять')
#     case _:  # wildcard отрабатывает если другие блоки не сработали - опционально (любое ДРУГОЕ значение)
#         print('неизвестная команда')
#
# print('Проверки завершены')
#
# ####
#
# match cmd:
#     case command:  # command - переменная в которую попадает значение cmd
#         print(f'Вы ввели команду {command}')
#
#
#         # case вызовет ошибку так как не может быть двух одинаковых команд
#     # похоже на if else (последний не может быть первым)
# ####
#
# match cmd:
#     case str():  # проверка на тип данных (в данном случае класс строка)
#         print('Вы ввели строку')
#     case _:  # wildcard
#         print('Вы ввели что-то другое')
#
#     ####
#
# match cmd:
#     case str() as command:  # as - присваивание переменной command только после проверки типа данных
#         print(f'Вы ввели команду {command}')
#     case _:  # wildcard
#         print('Вы ввели что-то другое')
#
#     ####
#
# match cmd:
#     case str(command):  # запись идентичная предыдущей
#         print(f'Вы ввели команду {command}')
#     case _:  # wildcard
#         print('Вы ввели что-то другое')
#
#     ####
# # Сначала частные шаблоны, потом более общие (похожая логика на if else)
#
# cmd = 1  # 10 #cmd
# match cmd:
#     # guard - дополнительная проверка можно прописывать условия внутри case по правилам if
#     case int() | float() as command if 0 < command < 10:  # сначала проверка на тип данных, потом на диапазон
#         print(f'Вы ввели число от 0 до 9 {command}')
#         # проверка на длину и на то что строка состоит только из букв
#     case str() as command if len(command) < 10 and command.isalpha() and command[0] == 'c':
#         print(f'Вы ввели строку command {command}')
#     case _:  # wildcard
#         print('Вы ввели что-то иное. Проверьте тип данных')
#         raise TypeError('Неверный тип данных')
#
#     # Почему не if elif else? - match case более читаемый и понятный
#
# ####
# # Match case для списков (и кортежей)
#
# cmd = ['Monty Python', 'Python', '2023']
#
# match cmd:
#     case list() as book:
#         print(f'{book} - это список!')
#     case _:  # wildcard
#         print('Вы ввели что-то другое')
#
#     #### Работает и для кортежей
# match cmd:
#     # распаковка списка (только если 3 элемента длины) можно добавить
#     # *_ - для остальных. Можно добавить защитника и скобки на условия
#     case author, title, year, *_ if len(cmd) < 6:
#         print(f'Автор: {author}, название: {title}, год: {year}')
#
#     ####  Работает и для кортежей
# match cmd:
#     case [str() as author, str() as title, int() | float() as year, *_] if len(cmd) < 6 and len(title) > 2:
#         print(f'Автор: {author}, название: {title}, год: {year}')
#
#     ####  Варианты для 2 шаблонов
# cmd = ['Monty Python', 'Python', '2023']
# cmd1 = ['test', 'Monty Python', 'Python', '2023', 'test2', 'test3']
#
#
# # количество переменных и их имена должны совпадать, допускается использование wildcard
# # если шаблоны разные - надо создавать отдельный case    case [author, title, year] | [_, author, title, year, *_] if len(title) > 2:  # можно использовать круглые скобки
#
# match cmd, cmd1:
#     case [author, title, year], [_, author1, title1, year1, *_] if len(title) > 2:  # можно использовать круглые скобки
#
# ####  Работа со словарями
# # cmd = {'author': 'Monty Python', 'title': 'Python', 'year': 2023, 'pages': 238}
# #
# # match cmd:
# #     # Важно чтобы эти ключи словаря были, иначе будет wildcard
# #     case {'author': str(author), 'title': str() as title, 'year': int(year) | float(year),
# #           'pages': 238 | 239} if len(cmd) > 2:
# #         print(f'Автор: {author}, название: {title}, год: {year}')
# #     case _:
# #         print('Неверные данные')
#
#     ####  Проверка на количество ключей
#
# match cmd:
#     case {'author': str() as author, 'title': str() as title, **kwargs} if len(
#         kwargs) >= 2:  # **kwargs - остальные ключи
#         print(f'Автор: {author}, название: {title}, год: {kwargs.get("year")}')
#     case _:
#         print('Неверные данные!!!')
#
#     # Проверка на содержимое ключей
#
# match cmd:
#     case {'author': 'Monty Python' as author, 'title': str() as title, **kwargs} if len(kwargs) >= 2:
#         print(f'Автор: {author}, название: {title}, год: {kwargs.get("year")}')
#
#
# match cmd:
#     case str() as command:  # as - присваивание переменной command только после проверки типа данных
#         print(f'Вы ввели команду {command}')
#     case _:  # wildcard
#         print('Вы ввели что-то другое')

some_str = 'fish'
print(some_str[::-1])  # start stop step
# Делаем проверку на палиндром
# Реализуем домашнее задание на match case

# user_input
# проверка на палиндром
# если палиндром - вывести сообщение
# если не палиндром - вывести сообщение

user_input = input('Введите слова через запятую: ').split(',')

for word in user_input:
    # if type(word) == str and word == word[::-1]:
    #     print(f'Слово {word} - палиндром')

    match word:
        case str() as word if word == word[::-1]:
            print(f'Слово {word} - палиндром')


#########################################################
# ЗНАКОМСТВО С ФУНКЦИЯМИ
# Функция - это именованный блок кода, который можно вызвать из другого места программы
# Применяем при многократном повторении кода
# Облегчает читаемость кода, работу с большими программами

# Правила именования функций
# 1. Имя функции должно быть глаголом
# 2. Имя функции должно быть в нижнем регистре
# 3. Имя функции может содержать буквы, цифры и символ _
# 4. Имя функции не должно совпадать с ключевыми словами и встроенными функциями
# 5. Имя функции должно быть описательным

# def - ключевое слово для создания функции
# Функция должна выполнять одно действие

def say_hello():
    # print('Hello, World!') # print - выводит значение на экран
    return 'Hello, World!'  # return - возвращает значение из функции. Иначе возвращает None


say_hello()  # вызов функции через имя и круглые скобки
print(f'Привет!{say_hello()}')  # Если нет return - то None


# Параметры функции
def say_som(string):
    return string.upper()


print(say_som('Hello, World!'))

# Практика
# Напишите функцию проверки на палиндром
# Функция принимает строку и возвращает True или False
# Инпут, и проверка на палиндром

is_true = True

match is_true:
    case True:
        print(f'Это {is_true}')

if is_true:
    print(f'Это {is_true}')


def check_palindrome(string):
    return string == string[::-1]


def check_palindrome2(word):
    match word:
        case str() as w if w == w[::-1]:
            return True
        case _:
            return False


user_input = input('Введите слово: ')
if check_palindrome(user_input):
    print('Это палиндром')
else:
    print('Это не палиндром')

# Много параметров в функции
word3 = 'fish'


def say_hello_name(name, hello):  # Порядок передачи параметров важен
    return f'{hello}, {name}!'


print(say_hello_name('Alex', 'Hello'))

# Именованные параметры

print(say_hello_name(hello='Hello', name='Alex'))


# Параметры по умолчанию

def say_hello_name2(name, hello='Hello'):  # Порядок передачи параметров важен
    return f'{hello}, {name}!'


print(say_hello_name2('Alex'))
print(say_hello_name2('Alex', 'Good night'))

# Пример функции  ЗАПИСИ JSON в файл, с параметрами по умолчанию encoding='utf-8' enshure_ascii=False, indent=4


def write_json(data, file_name, encoding='utf-8', ensure_ascii=False, indent=4):
    """
    Запись данных в файл в формате JSON
    :param data: Данные для записи
    :param file_name: Имя файла
    :param encoding: Кодировка
    :param ensure_ascii: ASCII
    :param indent: Отступ
    :return: None
    """
    import json
    with open(file_name, 'a', encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=ensure_ascii, indent=indent)


data = {'name': 'Alex', 'age': 30}
write_json(data, '../data.json')
