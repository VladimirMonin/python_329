
# lower() - преобразует строку в нижний регистр
# upper() - преобразует строку в верхний регистр
# replace() - заменяет одну подстроку на другую
# strip() - удаляет пробелы в начале и в конце строки
# find() - Поиск подстроки в строке. Возвращает номер первого вхождения или -1
# index() - Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError
# count() - Возвращает количество вхождений подстроки в строке
# isdigit() - Проверяет, состоит ли строка из цифр. Возвращает True или False
# isalpha() - Проверяет, состоит ли строка из букв. Возвращает True или False
# isalnum() - Проверяет, состоит ли строка из цифр или букв. Возвращает True или False
# capitalize() - Переводит первый символ строки в верхний регистр, а все остальные в нижний
# title() - Переводит первый символ каждого слова строки в верхний регистр, а все остальные в нижний

# Проверка номера

"""
Вводные данные

+77053183958
+77773183958
87773183958
+(777)73183958
+7(777)-731-83-58
+7(777) 731 83 58
"""

# Проверка длины. Начало номера. 8 +7. Только числа.

# 1) Убираем все лишнее. Методы lstrip для + и replace для скобок, пробелов и тире
# 2) Проверяем длину. Метод len
# 3) Проверяем начало номера. Метод startswith или индекс
# 4) Проверяем, что все символы - цифры. Метод isdigit


# Задача №2. Проверка пароля
"""
- Должен содержать хотя бы один спецзнак
- Не должен содержать пробел
- Должен содержать символы разных регистров (большие и маленькие)
- Должен быть более 7 символов длиной
"""

# find - для проверки на пробел. Если получаем -1 = все хорошо
# len - для проверки длины пароля
# islower and isupper - для проверки на регистр
# if not string.isalnum() - для проверки на спецсимволы


# print(string.isupper())
# print(string.islower())
# print(string.isalnum())  # Буквы. Числа. Без пробелов. Без сцезнаков

#  Начинаем новый материал.
# Цикл for. Перебор элементов последовательности

# string = 'Hello World!'
#
# for letter in string:
#     if letter != ' ':
#         print(letter)

string = 'He:*::l24234lo Wo*(*?*?:?:%:%;:234256rld!'
new_string = ''

for letter in string:
    if letter.isalpha() or letter == ' ':
        # new_string = new_string + letter # Полная запись
        new_string += letter  # Сокращенная запись

print(new_string)

# Проверка пароля в цикле. Считаем количество спецсимволов, букв, цифр
# Мы задаем условия по сложности пароля
digit = 3
letter = 3
special = 3

digit_count = 0
letter_count = 0
special_count = 0

password = '1234567890'
old_passwords = ['1234567890', '1234567890', '1234567890']

is_old = False

for symbol in password:
    if symbol.isdigit():
        digit_count += 1
        # digit_count = digit_count + 1 # Полная запись
    elif symbol.isalpha():
        letter_count += 1
    elif not symbol.isalnum():
        special_count += 1

if password in old_passwords: #
    is_old = True

# if digit_count >= digit and letter_count >= letter and special_count >= special\
#         and not is_old and len(password) >= 8:
#     print('Пароль подходит')

product_list = ['мясо', 'рыба', 'печенье', 'бананы', 'молоко', 'яблоки', 'авакадо',
                'соевое молоко', 'соевый соус', 'соевый творог', 'соевый сыр', 'фасоль']
bad_list = ['рыба', 'мясо', 'молоко']

# Создаем копию списка
new_list = ['мясо', 'рыба', 'молоко']
for product in product_list:
    new_list.append(product)

new_list = [product for product in product_list]

# new_list = []
# for product in product_list:
#     if product not in bad_list:
#         new_list.append(product)
#
new_list = [product for product in product_list if product not in bad_list]
print(new_list)

# Практика. Проверка вхождения юзернейма в список.
# Задача №1. Проверка юзернейма

# Получить юзернейм от пользователя, и сравнить его с теми, что есть в списке.
# Сравнение должно быть нечувствительным к регистру. Сделайте проверку в цикле!
# Список в чате.

users_lst = ['John88', 'Legolas123', 'YagamiLight',
             'Catwoman', 'Dragonborn', 'Daenerys',
             'Nagibator228', 'BigDaddy', 'Killer007',
             'Сергей']

# username = input('Введите юзернейм: ')
# if username.lower() in [user.lower() for user in users_lst]:
#     print('Такой юзернейм уже существует')

# Методы списков
# append - добавляет элемент в конец списка
# insert - добавляет элемент в список по индексу
# extend - расширяет список другим списком
# remove - удаляет элемент из списка по значению
# pop - удаляет элемент из списка по индексу и возвращает его
# clear - очищает список
# index - возвращает индекс элемента
# count - возвращает количество элементов
# sort - сортирует список
# reverse - переворачивает список
# copy - копирует список
# del - удаляет элемент по индексу или срез. Пишется как функция del list[0]

# Метод append
product_list = ['сыр']
new_product = 'молоко'
product_list.append(new_product)
print(f'Это результат работы append: {product_list}')

# Метод insert
product_list = ['сыр']
new_product = 'молоко'
product_list.insert(0, new_product) # Первый аргумент - индекс, второй - элемент
print(f'Это результат работы insert: {product_list}')
product_list.insert(100, new_product) # Если индекс больше длины списка, то элемент добавится в конец
print(f'Это результат работы insert_100: {product_list}')

# Метод remove
product_list = ['сыр', 'молоко']
product_list.remove('сыр')  # Удаляет элемент из списка. Если элементов несколько, то удаляется первый
print(f'Это результат работы remove: {product_list}')
# product_list.remove('сыр') # Если элемента нет в списке, то будет исключение ValueError

# Метод pop
product_list = ['сыр', 'молоко']
print(product_list.pop(0)) # Удаляет элемент. Возвращает удаленный элемент. Удаляет по индексу. Если индекс не указан, то удаляется последний элемент

# Метод clear
product_list = ['сыр', 'молоко']
product_list.clear()  # Очищает список
print(product_list)

# Метод index
product_list = ['сыр', 'молоко']
print(product_list.index('сыр')) # Возвращает индекс элемента. Если элементов несколько, то возвращает индекс первого

# Метод count
product_list = ['сыр', 'молоко', 'сыр']
print(product_list.count('сыр')) # Возвращает количество элементов

# Метод sort
product_list = ['сыр', 'молоко', 'сыр']
product_list.sort()  # Сортирует список

# Del
product_list = ['сыр', 'молоко', 'сыр']
del product_list[0]  # Удаляет элемент по индексу

# Практика
# Задача №2
# Пройдите по списку юзернеймов, и если юзернейм содержит в себе цифры,
# добавьте его в новый список. Удалите его из старого списка.

users_lst = ['John88', 'Legolas123', 'YagamiLight',
             'Catwoman', 'Dragonborn', 'Daenerys',
             'Nagibator228', 'BigDaddy', 'Killer007',
             'Сергей']

new_users_lst = []

for user in users_lst:
    if not user.isalpha():
        new_users_lst.append(user)
        users_lst.remove(user)



some_lst = [1, 1.1, True, 'string', [1, 2, 3]]

for element in some_lst:
    print(type(element))
    if type(element) in [str, list]:
        for item in element:
            print(item)

# Вложенность до 3-4 уровня - нормально. Больше - не очень.
users = [
    ['username', 'pass', 'age'],
    ['Catwoman', 'sdfjlj', '22'],
    ['Nagibator228', 'BigDaddy', 'Killer007'],
]

for user in users:
    for username in user:
        print(username)
