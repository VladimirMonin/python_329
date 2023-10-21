"""
Lesson 26
21.10.2023
ООП - инкапсуляция
"""


class Person:
    def __init__(self, name: str, user_name: str, age: int):
        self.name = name
        self.user_name = user_name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name}')

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age in range(1, 100):
            self.age = age
        else:
            print('Неверный возраст')

"""
Проблема в том, что даже при указании аннотации типов, мы можем передать в атрибут класса любое значение.
При этом программа не рассчитана на эти значения.
"""
# Создаем экземпляр класса
person = Person('Иван', 'ivan', 30)
# Напрямую обращаемся к атрибуту класса
print(person.name)
person.age = 300
person.user_name = "$er0gA"
