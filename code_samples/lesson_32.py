"""
Lesson 32
12.11.2023

Тема: Абстрактные классы. Полиморфизм
- Разбор ДЗ службы доставки
- Потребность в абстрактных классах
- Абстрактные методы
- Практика с ABC На примере классов чтения данных из файлов

Магический метод __bool__
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass

"""
__bool__ - магический метод, который позволяет определить, как будет вести себя объект в условных конструкциях
"""

# Dataclass - данные по человеку, bool возвращает True если человек не работает и доступен для найма


@dataclass
class Person:
    name: str
    age: int
    position: str | None
    salary: int
    citizenship: str

    def __bool__(self):
        return self.position is None and self.citizenship == 'Россия'


# Создаем 3 товарищей для проверки с работой, без работы гражданство Казахстан и Россия

person1 = Person(name='Иван', age=30, position='Программист', salary=100000, citizenship='Россия')
person2 = Person(name='Андрей', age=30, position=None, salary=100000, citizenship='Россия')
person3 = Person(name='Николай', age=30, position=None, salary=100000, citizenship='Казахстан')

# Проверяем работу магического метода __bool__
print(bool(person1))
print(bool(person2))
print(bool(person3))

if person1:
    print(f'Можно нанимать {person1.name}')

if person2:
    print(f'Можно нанимать {person2.name}')

if person3:
    print(f'Можно нанимать {person3.name}')