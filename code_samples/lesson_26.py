"""
Lesson 26
21.10.2023
ООП - инкапсуляция
"""
"""
Декоратор @property - это специальный декоратор, 
который позволяет нам обращаться к методу как к атрибуту.

Нам не нужно будет писать круглые скобки после имени метода,
когда мы будем обращаться к нему.

Нам не нужно будет писать по 3 метода для получения, 
изменения и удаления значения атрибута.
"""


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age

    @property  # Декоратор @property - это специальный декоратор, который позволяет нам обращаться к методу как к атрибуту.
    def age(self):
        print('Вызов метода age')
        return self.__age

    @age.setter
    def age(self, value):
        print('Вызов метода age.setter')
        if not self.__is_int(value):
            raise ValueError('Возраст должен быть целым числом')
        if not self.__is_positive(value):
            raise ValueError('Возраст должен быть положительным числом')
        self.__age = value

    @age.deleter
    def age(self):
        print('Вызов метода age.deleter')
        del self.__age

    def __is_int(self, value):
        return isinstance(value, int)

    def __is_positive(self, value):
        return value > 0

    def get_future_age(self, years:int):
        """Метод который принимает число и возвращает возраст человека через X лет"""
        return self.__age + years

    def __str__(self):
        return f'{self.name} {self.surname} {self.__age}'


person = Person('John', 'Smith', 30)
print(person.age)
# person.age = 25
print(person.get_future_age(5))
# Удаляем атрибут age
del person.age

# print(person.age) # AttributeError: 'Person' object has no attribute '_Person__age'

