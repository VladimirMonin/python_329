"""
Lesson 28
29.10.2023

Тема: Наследование в ООП

- Концепция наследования в ООП
- Наследуются и поля и методы
- Расширение функционала родительского класса в дочернем классе
- Расширение атрибутов родительского класса в дочернем классе
- Как пишется документация к классу и методу (pep 257)
(https://peps.python.org/pep-0008/#documentation-string)
- Как посмотреть документацию к классу __doc__
- Как посмотреть аттрибуты класса __dict__ и __dir__
- Переопределение родительских полей и методов
- Многоуровневое наследование
"""


# Многоуровневое наследование

class A:
    def __init__(self):
        print('Вызов __init__ класса A')

    def a_method(self):
        print(f'Вызов метода a_method класса {self.__class__.__name__}')


class B(A):
    def __init__(self):
        print(f'Вызов __init__ класса {self.__class__.__name__}')
        super().__init__()

    def b_method(self):
        print(f'Вызов метода b_method класса {self.__class__.__name__}')


class C(B):
    def __init__(self):
        print(f'Вызов __init__  класса {self.__class__.__name__}')
        super().__init__()


c = C()
c.b_method()
c.a_method()