"""
Lesson 34
19.11.2023

Класс внутри класса. Вложенные классы.
Похоже на представление базы данных в Django
Метаклассы
"""


class Meta(type):
    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs)
        cls.MAX_COORD = 100
        cls.MIN_COORD = 0


# Аналог метакласса Meta - только с изменением на этапе __new__ а не __init__
class Meta2(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        # Изначальный вариант с type - тоже работает
        # return type.__new__(cls, name, base, attrs)
        return super().__new__(cls, name, base, attrs)


class Point(metaclass=Meta2):
    def get_coords(self):
        return (0, 0)


pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())


class Point(metaclass=Meta):
    def get_coords(self):
        return 0, 0


pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())
