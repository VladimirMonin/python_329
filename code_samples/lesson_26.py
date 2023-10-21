"""
Lesson 26
21.10.2023
ООП - инкапсуляция
"""
"""
Создание класса персоны, с приватными полями, а так же проверкой на валидность введенных данных в конструкторе и 
сеттерах
"""


class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError('Имя должно быть строкой')
        self.__name = name

    def set_age(self, age):
        if not isinstance(age, int):
            raise ValueError('Возраст должен быть числом')
        if age < 0:
            raise ValueError('Возраст не может быть отрицательным')
        if age > 150:
            raise ValueError('Он должен быть человеком а не вампиром!')
        self.__age = age

    def __str__(self):
        return (f'Имя: {self.__name}\n'
                f'Возраст: {self.__age}\n')


person = Person('John', 25)
print(person)
person.set_name('Ivan')
# person.set_age(244)
print(person)

