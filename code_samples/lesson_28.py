"""
Lesson 28
29.10.2023

Тема: Наследование в ООП

- Концепция наследования в ООП
"""


# Наследуется все, включая конструктор __init__ и все методы

class Parent:  # Базовый класс
    def __init__(self, name):
        self.name = name
        print('Parent __init__')

    def get_name(self):
        return self.name


class Child(Parent):  # Производный класс наследует от базового класса Parent
    pass


parent: Parent = Parent('John')
child: Child = Child('Smith')

# Методы родителя доступны и в дочернем классе
print(parent.get_name())
print(child.get_name())
