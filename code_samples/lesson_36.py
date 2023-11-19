"""
Lesson 34
19.11.2023

Класс внутри класса. Вложенные классы.
Похоже на представление базы данных в Django
Метаклассы
"""

# TODO
"""
Создайте метакласс, который будет добавлять в классы атрибут class_id
со значением, равным имени класса в нижнем регистре.

Создайте классы A и B с этим метаклассом и проверьте, что у них есть
атрибут class_id.
"""


class IDClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['class_id'] = name.lower()
        return super().__new__(cls, name, bases, attrs)


class A(metaclass=IDClass):
    pass


class B(metaclass=IDClass):
    pass


print(A.class_id)
print(B.class_id)
