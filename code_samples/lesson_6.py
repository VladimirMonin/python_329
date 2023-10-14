# Цикл for в Python
# Применяем для перебора элементов последовательности
# Строки

# string = 'Hello, Monty Python'
# for letter in string[::2]:
#     print(letter, end='')

# Итерация по спискам
# list_ = [1, 2, 3, 4, 5]
# for number in list_[::2]:
#     print(number)

# Len - возвращает длину последовательности
# range - возвращает последовательность чисел

# for number in range(10):
#     print(number)
#
# print(range(10))
# print(list(range(10)))
# print(type(range(10)))

# Цикл for + range + len
pages = 5

# for page in range(pages):  # range(5) = [0, 1, 2, 3, 4]
#     print('Page', page)
#     print('Страница', page + 1)

# Два списка одинаковой длины
# Перебираем элементы одного списка
# Используем индекс для получения элемента другого списка

list_1 = [1, 2, 3, 4, 5]
list_2 = ['Intel', 'AMD', 'Nvidia', 'Apple', 'Microsoft']

# for index in range(len(list_1)):  # range(5) = [0, 1, 2, 3, 4]
#     print(list_1[index], list_2[index])  # 1 Intel 2 AMD 3 Nvidia 4 Apple 5 Microsoft

# То же самое, но при итерации по списку
# Сложнее и надо отнять 1 от индекса

# for num in list_1:
#     num -= 1
#     print(list_1[num], list_2[num])
#

# Break, continue, else в цикле for
# Break - прерывает цикл
# Continue - пропускает итерацию
# Else - выполняется, если не было прерывания цикла

# Прерывание цикла

# for number in range(10):
#     if number == 2:
#         break # прерывает цикл, если number == 2
#     print(number)

# else:  # выполняется, если не было прерывания цикла и он завершился успешно
#     print('Цикл не был прерван')

# Пропуск итерации. Continue

# for number in range(10):
#     if number == 2:
#         continue # прерывает цикл, если number == 2
#     print(number, end='')

# Практика №1. Где я буду работать?
# Делаем запрос к пользователю, в какой компании он хочет работать
# Если в списке есть такая компания, то выводим ее название
# Останавливаем цикл через break.


vacancies = [
    "Яндекс",
    "Mail.Ru Group",
    "Kaspersky Lab",
    "Acronis",
    "EPAM Systems",
    "1С",
    "ABBYY",
    "Parallels",
    "QIWI",
    "Ozon",
    "JetBrains",
    "Wildberries",
    "Точка",
    "Сбер",
    "Тинькофф",
    "Самолет",
    "Альфа-Банк",
]

# user_input = input('Введите названия компаний через запятую: ').split(',')
# user input в виде генератора с lower
# user_input = [company for company in input('Введите названия компаний через запятую: ').split(',')]
# search = [company for company in user_input if company in vacancies]
#
# print(f'По вашему запросу '
#       f'найдены следующие компании:{search}')

####
# Практика №2. Поиск компаний. Пользователь вводит число от 1 до 5.
# Мы выводим на экран  запрошенное количество компаний.
# Программа выдаст рандомные компании без повторений.  random.randint + pop
# Цикл for - длиной len(user_input)

# 1. Пользовательский ввод. int
# Проверка. От 1 до 5
# Цикл for - длиной len(user_input)
# 2. Рандомный выбор компании. random.randint + pop
# 3. Вывод компании. print

# Вариант 2.
# Используем count + break

import random  # импортируем модуль random. Этот модуль позволяет работать с рандомными числами
#
# user_input = input('Введите число от 1 до 5: ')  # пользовательский ввод
# if user_input.isdigit():  # проверка, что введено число
#     user_input = int(user_input)  # преобразование в int
#     if 1 <= user_input <= 5:  # проверка, что число в нужном диапазоне
#         for _ in range(user_input):  # цикл for - длиной len(user_input)
#             print(vacancies.pop(random.randint(0, len(vacancies) - 1)))  # рандомный выбор компании
#     else:
#         print('Вы ввели число не из нужного диапазона')


# some_lst = [1, 2, 3, 4, 5]
#
# print(len(some_lst))
# print(list(range(0, 5)))
# print(some_lst[5])

# Пример. Состоит ли список из уникальных элементов?

shop_list = ['milk', 'bread', 'eggs', 'banana', 'lemon', 'milk', 'milk', 'bread']

not_unique = []

# for item in shop_list:
#     if shop_list.count(item) > 1:
#         not_unique.append(item)
#         print(f'Список не уникальный\n'
#               f'Элемент {item} встречается {shop_list.count(item)} раз')
#
# print(set(not_unique))

# Цикл while - цикл с условием ПОКА. Пока условие выполняется, цикл выполняется
# while условие: # условие выполняется, пока True

# while True: - бесконечный цикл, Истина будет всегда

# count = 0
# while True:
#     count += 1
#     print(f'Я буду делать это бесконечно. Мухаха!\n'
#           f'Сделаю это {count} раз!')

# Условие выхода из цикла - пользователь просит выйти из цикла

is_stopped = False

# while not is_stopped:
#     user_input = input('Введите что-нибудь: ')
#     if user_input == 'stop':
#         is_stopped = True
#     else:
#         print('Вы не ввели stop')
#
# Второй вариант с break

# while True:
#     user_input = input('Введите что-нибудь: ')
#     if user_input.lower() in ['stop', 'стоп', 'хватит', 'астанавись!']:
#         break
#     else:
#         print('Вы не ввели stop')

# Практика №3. Купи слона!
# while True:
#     print('Купи слона!')
#     user_input = input('Ты ведь купишь?')
#     if user_input.lower() != 'да':
#         print(f'Вот все говорят: {user_input.lower()}. А ты купи слона!')
#     else:
#         print('Спасибо, что купил слона!')
#         break

# Пример использования цикла while + continue - вывод четных чисел

num_lst = list(range(0, 20))
new_lst = []

while num_lst:
    number = num_lst.pop()
    if number % 2 != 0:
        continue
    print(number)
    new_lst.append(number)
print(new_lst)



