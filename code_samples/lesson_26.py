"""
Lesson 26
21.10.2023
ООП - инкапсуляция
"""

# Приватные атрибуты - атрибуты, которые доступны только внутри класса
# Приватные методы - методы, которые доступны только внутри класса
# Защищенные атрибуты - атрибуты, которые доступны только внутри класса и его наследников
# Защищенные методы - методы, которые доступны только внутри класса и его наследников

# _ - Это защищенный атрибут (метод)
# __ - Это приватный атрибут (метод)

class Person:
    def __init__(self, name: str, user_name: str, age: int):
        self.name = name
        self._user_name = user_name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age in range(1, 101):
            self.__age = age
        else:
            print('Неверный возраст')

    def __get_user_name(self):
        return self._user_name

    def __set_user_name(self, user_name):
        self._user_name = user_name

    def _get_name(self):
        return self.name

    def _set_name(self, name):
        self.name = name

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Возраст: {self.__age}\n' \
               f'Имя пользователя: {self._user_name}'


class Employee(Person):
    def __init__(self, name: str, user_name: str, age: int, company: str):
        super().__init__(name, user_name, age)
        self.company = company

    def __str__(self):
        # Обращаемся к классу родителя через super() cls и пробуем вызвать
        # __get_user_name
        # _get_name
        return f'Имя: {super()._get_name()}\n' \
                  f'Возраст: {super().__get_user_name()}\n' \




# Проверка
person = Person('Иван', 'ivan', 30)
print(person)
print(person.name)
print(person._user_name)
# print(person.__age)

employee = Employee('Иван', 'ivan', 30, 'Google')
print(employee)

