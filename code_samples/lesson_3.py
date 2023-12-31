# Pep8 and python Zen
# https://ru.wikipedia.org/wiki/%D0%94%D0%B7%D0%B5%D0%BD_%D0%9F%D0%B0%D0%B9%D1%82%D0%BE%D0%BD%D0%B0
# https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html

# ------ Блок-схемы в программировании ------
# ГОСТ - https://pro-prof.com/archives/1462
# РЕДАКТОР - https://products.aspose.app/diagram/ru/flowchart

# ----- Практика создания блок-схем -----
# 1. Какая температура на улице?
# 2. Какой индекс ультрафиолета?
# 3. Если температура больше 30 градусов и индекс ультрафиолета больше 6,
# предупредить пользователя о возможном солнечном ударе.


# ------ Условный оператор if ------
# if условие - если условие истинно, то выполняется код внутри блока if
# elif условие - если условие истинно, то выполняется код внутри блока elif
# else - если все условия ложные, то выполняется код внутри блока else

# a = 5.0000001
#
# if a == 5:
#     print('a равно 5')
#     print('Это всё ещё внутри блока if')
# else:
#     print('a не равно 5')
#
# print('Этот код выполняется в любом случае')
#

# temp = int(input('Введите температуру: '))
# uv = int(input('Введите индекс УФ: '))
#
# if temp > 30 and uv > 6:
#     print('Возможен солнечный удар')
# else:
#     print('Солнечный удар маловероятен')

# ------ ELIF ------

"""Когда исполняется инструкция if-elif-else, в первую очередь проверяется shop.
Если условие истинно, тогда исполняется блок инструкций if.
Следующие условия и инструкции пропускаются, и управление переходит к операторам вне if-elif-else.

Если shop оказывается ложным, тогда управление переходит к следующему условию elif, и проверяется shop.
Если оно истинно, тогда исполняются инструкции внутри первого блока elif.
Последующие инструкции внутри этого блока пропускаются.

Этот процесс повторяется, пока не находится условие elif, которое оказывается истинным.
Если такого нет, тогда исполняется блок else в самом конце."""

# a = 5
# if a == 5:
#     print('блок с IF a равно 5')
# if a < 6:
#     print('блок с IF a меньше 6')
# if a > 4:
#     print('блок с IF a больше 4')
#
#
# a = 5
# if a != 5:
#     print('блок с IF a равно 5')
# elif a < 6:
#     print('блок с ELIF a меньше 6')
# elif a > 4:
#     print('блок с ELIF a больше 4')

# Пример со строкой

# shop = 'молоко'
#
# if shop == 'молоко':  # True
#     print('Купить молоко')
# if shop == 'молоко':  # True
#     print('Купить ещё молоко')
# if shop == 'молоко':  # True
#     print('Купить ещё молоко')
#
# print('-------------------')
# Если одно из условий оказалось истинным, то остальные даже не проверяются

# if shop == 'молоко':  # True
#     print('Купить молоко')
# elif shop == 'молоко':  # True
#     print('Купить ещё молоко')
# elif shop == 'молоко':  # True
#     print('Купить ещё молоко')
#
# print('Идем дальше')

# ------ IF - расшифровка оценки ------
# mark = ('Введите оценку: '))  (строки или числа)
# Если оценка 5 - отлично
# Если оценка 4 - хорошо
# Если оценка 3 - удовлетворительно
# Если оценка 2 - неудовлетворительно
# Если оценка 1 - ужасно
# Иначе - неизвестная оценка

# НЕ ДЕЛАЙТЕ ТАК :)
# mark = int(input('Введите оценку: '))
# if mark > 1:
#     print('Вероятно, оценка выше 1')
# if mark > 2:
#     print('Вероятно, оценка выше 2')
# if mark > 3:
#     print('Вероятно, оценка выше 3')
# if mark > 4:
#     print('Вероятно, оценка выше 4')
# if mark <= 5:
#     print('Вероятно, мы поймаем все IF если оценка будет 5')


# РЕШЕНИЕ (сравниваем строки или числа, если интуем)
# mark = input('Введите оценку: ')
# if mark == '5':
#     print('Отлично')
# elif mark == '4':
#     print('Хорошо')
# elif mark == '3':
#     print('Удовлетворительно')
# elif mark == '2':
#     print('Неудовлетворительно')
# elif mark == '1':
#     print('Ужасно')
# else:
#     print('Неизвестная оценка')

# ------ Вложенный блок if ------
mark = int(input('Введите оценку от 1 до 5: '))

if 1 <= mark <= 5:
# Если оценка входит в диапазон от 1 до 5 включительно - выполняется этот блок
    if mark == 5:
        print('Отлично')
    elif mark == 4:
        print('Хорошо')
    elif mark == 3:
        print('Удовлетворительно')
    elif mark == 2:
        print('Неудовлетворительно')
    elif mark == 1:
        print('Ужасно')
else:
    print('Некорректная оценка')

# Определяем кто вы, по возрасту. Неявно прописанные условия - приводят к самому непредсказуемому результату

# age = int(input('Введите ваш возраст: '))

# if age > 200:
#     print('Вы вампир')
# if age > 100:
#     print('Вы долгожитель. Гном?')
# if age > 75:
#     print('Вы старый. Вероятно человек')

# ------ Строки ------
# Строка - это последовательность символов, заключенная в кавычки.
# Это неизменяемый тип данных, т.е. нельзя изменить один символ в строке, можно только создать новую строку.

# string = 'Hello, Monty Python'
# print(string)
# print(string[0])  # H
# string[0] = 'h'  # TypeError: 'str' object does not support item assignment

# ------ Срезы ------
# Срез - это часть строки, которая включает в себя один или несколько символов.
# Срезы создаются с помощью оператора [] и двух индексов, разделенных двоеточием.
# string[start:stop:step] - start - начало среза, stop - конец среза, step - шаг среза

# string = 'Hello, Monty Python'
# print(string[::])  # Hello, Monty Python
# print(string[0:])  # Hello, Monty Python
# print(string[:])  # Hello, Monty Python

# print(string[0:5])  # Hello (по 5й не включая 5й)
# print(string[0:5:2])  # Hlo (по 5й не включая 5й, шаг 2)

# в обратном порядке
# print(string[::-1])  # nohtyP ytnoM ,olleH

# ------ Методы строк ------
# Метод - это функция, которая применяется к объекту определенного типа.
string = 'Hello, Monty Python'
string = string.lower()

print(string)  # hello, monty python

product = input('Введите название товара: ').lower()

if product == 'молоко':
    print('Купить молоко')
