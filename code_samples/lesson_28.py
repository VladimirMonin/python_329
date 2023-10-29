"""
Lesson 28
29.10.2023

Тема: Наследование в ООП

- Концепция наследования в ООП
- Наследуются и поля и методы
- Расширение функционала родительского класса в дочернем классе
- Расширение атрибутов родительского класса в дочернем классе
- 10 МИНУТ ПЕРЕРЫВ :)
- Как пишется документация к классу и методу (pep 257)
(https://peps.python.org/pep-0008/#documentation-string)
- Как посмотреть документацию к классу __doc__
- Как посмотреть аттрибуты класса __dict__ и __dir__
"""


# Переопределение родительских полей и методов

class Person:
    def __init__(self, name, surname, age, work):
        self.name = name
        self.surname = surname
        self.__age = age
        self.work = work

    def get_age(self):
        return self.__age

    def __str__(self):
        return f'{self.name} {self.surname} {self.__age}'


class Employee(Person):
    def __init__(self, name, surname, age, work, salary):
        super().__init__(name, surname, age, work)
        self.salary = salary

    def __str__(self):
        return f'{self.name} {self.surname} {self.__age} {self.salary}'