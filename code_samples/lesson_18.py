# Lambda - анонимные функции
# Функция, которая не имеет имени, записывается в одну строку
# Содержит в себе одно выражение и возвращает результат его выполнения автоматически
"""
Лямбда-функции в Python имеют несколько ограничений, которые делают их подходящими
только для относительно простых операций.

Вот полный список ограничений для лямбда-функций в Python:

1. **Одно выражение:**
Лямбда-функция может содержать только одно выражение.
Она не может содержать блоки кода или множество операторов.

2. **Нет операторов присваивания:**
В лямбда-функции нельзя использовать операторы присваивания, такие как `=`.

3. **Ограниченный доступ к глобальным переменным:**
Лямбда-функции могут использовать глобальные переменные,
но только для чтения, а не для записи. Им не разрешается изменять значения глобальных переменных.

4. **Ограниченный доступ к внешним переменным (замыкания):**
Лямбда-функции могут использовать переменные из внешней области видимости (замыкание),
но только для чтения. Они не могут изменять значения этих переменных без использования ключевого слова `nonlocal`.

5. **Неявное возвращаемое значение:**
Лямбда-функции не требуется использовать ключевое слово `return`.
Они автоматически возвращают результат выражения, которое находится справа от двоеточия `:`.

6. **Ограниченная читаемость:**
Лямбда-функции предназначены для коротких и простых выражений.
Из-за их сжатого синтаксиса они могут быть менее читаемыми, чем именованные функции.

7. **Ограниченная возможность документации:**
Лямбда-функции не поддерживают многострочные строки документации (docstrings),
что делает их менее удобными для документирования кода.

8. **Нет возможности использования аннотаций типов:**
В Python 3.0 и более поздних версиях, лямбда-функции не могут содержать аннотации типов (type hints).

9. **Ограниченный набор операторов:**
Лямбда-функции могут содержать только ограниченный набор операторов,
такие как арифметические операторы, операторы сравнения и некоторые другие.

10. **Нельзя создавать классы или объекты:**
Лямбда-функции не могут создавать экземпляры классов или выполнять другие сложные операции, связанные с объектами.

"""
from pprint import pprint


def summ(int1, int2):
    return int1 + int2


summ2 = lambda int1, int2: int1 + int2

print(summ(1, 2))
print(summ2(1, 2))

# Можно сразу вызывать лямбду и передавать в нее аргументы
print((lambda int1, int2: int1 + int2)(1, 2))

# TODO
# Напишите функцию, которая принимает строку и возвращает
# ее в обратном порядке
# Пример: "Hello world" -> "dlrow olleH"
# Пример: "123456789" -> "987654321"

reversed = lambda string: string[::-1]
is_reversed = lambda string: string.lower() == string[::-1].lower()
is_palindrome = lambda string: string.lower().replase(' ', '') == string[::-1].lower().replase(' ', '')
print(reversed("Hello world"))
print(is_reversed("Hello world"))

# Тернарный оператор - условие в одну строку
# Синтаксис:
# value1 if condition else value2
# Пример:
# print("Hello") if 5 > 2 else print("Bye")

# Тернарный оператор в лямбда функции
# функция которая принимает число и возвращает
# True если оно четное и False если нечетное

is_even = lambda number: True if number.isdigit() and int(number) % 2 == 0 else False

# TODO
# Попробуйте написать лямбду, которая
# интует если это число, и вернет None если это не число
# Пример:
# is_int("123") -> 123
# is_int("123a") -> None
is_int = lambda number: int(number) if number.isdigit() else None

user_nums_input = input("Введите числа через пробел: ").split()

# map - применяет функцию к каждому элементу итерируемого объекта
# map - возвращает итератор, который можно преобразовать в список (не изменяет исходный объект)
# map - синтаксис:
# map(function, iterable, ...)
user_nums_input = list(map(lambda number: int(number) if number.isdigit() else None, user_nums_input))

# однострочный вариант с интом
user_nums_input = list(
    map(lambda number: int(number) if number.isdigit() else None, input("Введите числа через пробел: ").split()))


def check_num(num: list) -> int | None:
    """
    Функция проверяет, что введенное число является числом
    :param num:
    :return:
    """
    for num in user_nums_input:
        if num.isdigit():
            return int(num)
        else:
            return None


ages = (('Иван', 20), ('Петр', 30), ('Анна', 25))
# Пройдем по кортежу и выведем имя и возраст в лямбде map
# Пример: Иван - 20
print(list(map(lambda age: f"{age[0]} - {age[1]}", ages)))
names = ('Иван', 'Петр', 'Анна', 'Аня', 'Эн', 'Н', 'Мария', 'Алексей', 'Ву')
ages_ = (20, 30, 25)

# Напишем аналог на цикле
for index in range(len(names) if len(names) < len(ages_) else len(ages_)):
    print(f"{names[index]} - {ages_[index]}")

# Пройдем по кортежу и выведем имя и возраст в лямбде map
# Пример: Иван - 20
print(list(map(lambda name, age: f"{name.upper()} - {age + 100}", names, ages_)))

# zip - объединяет два итерируемых объекта в один
new_dict = dict(zip(names, ages_))
# Тестируем функцию
print(is_int("в"))

# Пишем аналог zip на map и lambda
names = ('Иван', 'Петр', 'Анна', 'Аня', 'Эн', 'Н', 'Мария', 'Алексей', 'Ву')
ages_ = (20, 30, 25)

var = lambda key, value: {key: value}
result_row = map(var, names, ages_)
result = list(result_row)

# А теперь в одну строку
print(list(map(lambda key, value: {key: value}, names, ages_)))

# Пример от Виталия
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = list(map(lambda x, y: [x, y], tuple1, tuple2))
print(result)

# Filter - фильтрует итерируемый объект по заданному условию
# Синтаксис:
# filter(function, iterable)
# Пример:

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# переменная лябмда с условием положительное число
positive_nums = lambda x: x > 0
# фильтруем список по условию
filtered_nums = filter(positive_nums, nums)
filtered_nums = filter(lambda x: x > 0, nums)
filtered_nums = [num for num in nums if num > 0]

# TODO
# Попробуйте написать функцию, которая будет фильтровать список по углеводам

# Список продуктов с углеводами
sugar_bombs = ['конфеты', 'печенье', 'пирожное', 'торт', 'мороженое', 'пончик', 'булочка', 'блинчик', 'пончик']
menu = ['печенье', 'омлет', 'кофе', 'сыр']

# Получить список меню без углеводов (с помощью filter и lambda отфильтровать список menu от содержания sugar_bombs)

no_shugar = lambda product: product not in sugar_bombs
no_sugar_menu = filter(no_shugar, menu)

print(list(filter(lambda product: product not in sugar_bombs, menu)))

persons_dict = {
    'Иван': 20,
    'Петр': 30,
    'Анна': 25,
    'Аня': 25,
}
# Фильтр по ключам словаря
name = 'Иван'
age = 25
filtered_dict = dict(filter(lambda x: x[0] == name, persons_dict.items()))
filtered_dict = dict(filter(lambda x: x[1] == age, persons_dict.items()))

# filtered_dict = {key: value for key, value in persons_dict.items() if value == age}

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# четные значения ключей словаря (делятся на 2 без остатка)

# {'b': 2, 'd': 4}

# TODO
# Попробуйте написать filter + lambda , которая вернет имена где 2 буквы нн

# Решение
filtered_dict = filter(lambda x: 'нн' in x[0].lower(), persons_dict.items())
print(list(filtered_dict))

# Фильтр по значениям словаря
age = 30
# Возвращаем значение меньше 30
filtered_dict = filter(lambda x: x < age, persons_dict.values()) # TODO можно переписать на правильный варинат с items

# Работаем со списком словарей
persons_lst = [{
    'name': 'Иван',
    'age': 20,
    'langs': ['python', 'java', 'c++'],
    'city': 'Москва'},
    {
        'name': 'Петр',
        'age': 30,
        'langs': ['c', 'js'],
        'city': 'Санкт-Пeтербург'},
    {
        'name': 'Анна',
        'age': 25,
        'langs': ['go', 'typescript'],
        'city': 'Санкт-Пeтербург'}]

# фильтруем тех, кто знает go
filtered_dict = filter(lambda x: 'go' in x['langs'], persons_lst)

# фильтруем тех, кто моложе 25 и знает пайтон
filtered_dict = filter(lambda x: x['age'] < 25 and 'python' in x['langs'], persons_lst)

print(list(filtered_dict))

# TODO
# Попробуйте написать функцию, которая вернет список людей, которые знают go и живут в Санкт-Петербурге

# Решение
filtered_dict = filter(lambda x: 'go' in x['langs'] and x['city'] == 'Санкт-Пeтербург', persons_lst)

# Сортировка. Sort и Sorted
# Sort - является методом списка и сортирует список на месте, при этом изменяя исходный список.
# Работает при этом только со списками

# Sorted - является функцией и возвращает новый отсортированный список, не изменяя исходный.
# Работает со всеми итерируемыми объектами

# Синтаксис:
# sort - list.sort(key=None, reverse=False)
# sorted(iterable, key=None, reverse=False)

# 1. Мы можем передавать в ключ встроеенные функции Python
# - len
# - str.lower
# - str.upper
# - sum
# - max
# - min

# 2. Можем делать самописные функции с одним критерием сортировки или несколькими

simple_lst = [3, 2, 1, 4, 5, 6, 7, 8, 9]
# Сортируем список
simple_lst.sort()
print(simple_lst)

# Сортируем список в обратном порядке
simple_lst.sort(reverse=True)
print(simple_lst)

names_lst = ['Иван', 'Петр', 'Анна', 'Аня', 'Эн', 'Н', 'Мария', 'Алексей', 'Ву']
# Сортируем список по длине имени
names_lst.sort(key=len)
print(names_lst)

names_lst.sort(key=min, reverse=True)
print(names_lst)

# Key - может быть встроенной функцией или функцией, которую мы напишем сами.

# Список кортежей с информацией о книгах: (название, автор, год издания)
students = [
    ('Анюнин', 'HW12', 12),
    ('Анюнин', 'HW11', 15),
    ('Данилов', 'HW10', 4),
    ('Сергиенко', 'HW1', 5),
    ('Яколвлев', 'HW1', 1)
]


# Функция для сортировки по номеру в базе (3 элемент) а потом по домашней работе (2 элемент)
def sort_students(student):
    return (student[1]), student[2]


# Сортируем список по функции
students.sort(key=sort_students)

pprint(students)

# А теперь с лямбдой
students.sort(key=lambda student: (student[1], student[2]))

pprint(students)

pprint(students)
films_ratings = [
    {
        'title': 'Крепкий орешек',
        'rating': 7.5,
        'year': 1988
    },
    {
        'title': 'Назад в будущее',
        'rating': 8.5,
        'year': 1988
    },
    {
        'title': 'Таксист',
        'rating': 9.3,
        'year': 1976
    },
    {
        'title': 'Крепкий орешек 2',
        'rating': 9.9,
        'year': 1990
    },
    {
        'title': 'Назад в будущее 3',
        'rating': 10.0,
        'year': 1999
    },
    {
        'title': 'Таксист 6',
        'rating': 9.3,
        'year': 1999
    }
]

# Сортируем по году выпуска
films_ratings.sort(key=lambda film: film['year'])

# Cортируем по рейтингу
films_ratings.sort(key=lambda film: film['rating'], reverse=True)

# TODO
# Найдем фильмы 1988 года выпуска и отсортируем по рейтингу
# Фильтруем по году выпуска и потом сортируем по рейтингу

result = list(filter((lambda film: film['year'] == 1999), films_ratings))
result.sort(key=lambda film: film['rating'], reverse=True)
print(result)

films_db = {
    1: {
        'title': 'Крепкий орешек',
        'rating': 7.5,
        'year': 1988
    },
    2: {
        'title': 'Назад в будущее',
        'rating': 8.5,
        'year': 1988
    },
    3: {
        'title': 'Таксист',
        'rating': 9.3,
        'year': 1976
    },
    4: {
        'title': 'Крепкий орешек 2',
        'rating': 9.9,
        'year': 1990
    },
    5: {
        'title': 'Назад в будущее 3',
        'rating': 10.0,
        'year': 1990
    },
    6: {
        'title': 'Таксист 6',
        'rating': 9.3,
        'year': 1988

    }
}

# Найдем ID фильмов 1988 с рейтингом больше 8.0
# Результат в словарь
result = dict(filter(lambda film: film[1]['year'] == 1988 and film[1]['rating'] > 8.0, films_db.items()))
print(result)

# Сортируем результат по рейтингу и возвращаем список
result = list(sorted(result.items(), key=lambda film: film[1]['rating'], reverse=True))
print(result)

# TODO
# Напишите код сортировки словаря по названию фильма

# Решение
result = list(sorted(films_db.items(), key=lambda film: film[1]['title']))

# Map - применяет функцию к каждому элементу итерируемого объекта
# Возвращает итератор, который можно преобразовать в список (не изменяет исходный объект)
# Синтаксис:
# map(function, iterable)

# Интуем пользовательский ввод если это число
user_input = ['1', '2', '3', '4', '5']
user_input = list(map(int, user_input))


# Через лямбду с проверкой на число
# user_input = list(map(lambda item: int(item) if item.isdigit() else None, user_input))


# Перезапишем год выпуска всех фильмов 1988 на 2023
# Исходный словарь меняется! Не забываем про копию.
# Изменения происходят, так как мы используем ссылку на объект и изменяем его внутри функции map

# Решение с функцией
def update_year(film):
    film.update({'year': 2023})
    return film


list(map(update_year, films_db.values()))

print(films_db)
# Решение с лямбдой

# res =list(map(lambda film: film.update({'year': 2023}), films_db.values())) # Список None
# # res = list(map(lambda film: {**film, 'year': 2023}, films_db.values()))
# print(res)
#

# TODO HW
from data.marvel import full_dict

# Фильтруем и сортируем фильмы
result = sorted(filter(lambda film: film['title'].startswith('Ч'), full_dict.values()), key=lambda film: film['year'])

# Вывод результата
for film in result:
    print(f"{film['title']} ({film['year']})")

# Фильтруем film['title'].startswith('Ч') и получаем словарь словарей
result_dict = dict(filter(lambda film: film[1]['title'].startswith('Ч'), full_dict.items()))

"""
Код, который я предоставил:

```python
result = sorted(filter(lambda film: film['title'].startswith('Ч'), full_dict.values()), key=lambda film: film['year'])
```

работает следующим образом:

1. `full_dict.values()`: Это выражение возвращает все значения из словаря `full_dict` в виде списка. В данном случае, это будут словари, представляющие фильмы.

2. `filter(lambda film: film['title'].startswith('Ч'), full_dict.values())`: Здесь мы используем функцию `filter()`, чтобы отфильтровать фильмы, у которых название (`'title'`) начинается с буквы 'Ч'. Лямбда-функция `lambda film: film['title'].startswith('Ч')` принимает каждый фильм (словарь) и проверяет, начинается ли его название с 'Ч'. `filter()` возвращает итератор, содержащий только фильмы, которые удовлетворяют этому условию.

3. `sorted(...)`: Мы затем используем функцию `sorted()`, чтобы отсортировать фильмы. Она принимает два аргумента:
   - Первый аргумент — итерируемый объект, который в данном случае представляет отфильтрованные фильмы.
   - Второй аргумент — ключ (`key`), который указывает, по какому критерию сортировать элементы. Мы используем `lambda film: film['year']` в качестве ключа, чтобы сортировать фильмы по году выпуска.

Таким образом, `result` будет содержать отфильтрованные и отсортированные фильмы по году выпуска, где фильмы начинаются с буквы 'Ч'.
"""
# Отфильтровать фильмы, у которых название начинается с 'Ч'
filtered_films = filter(lambda film: film['title'].startswith('Ч'), full_dict.values())

# Отсортировать отфильтрованные фильмы по году выпуска
result = sorted(filtered_films, key=lambda film: film['year'])

# set comprehension из full_dict director
directors = {film['director'] for film in full_dict.values()}
print(directors)

# Превращаем в строку film['year']


result = {id: {**film, 'year': str(film['year'])} for id, film in full_dict.items()}


# Фильтруем film['title'].startswith('Ч') и получаем словарь словарей
result_dict = dict(filter(lambda film: film[1]['title'].startswith('Ч'), full_dict.items()))