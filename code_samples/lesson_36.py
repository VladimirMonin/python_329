"""
Lesson 34
19.11.2023

Класс внутри класса. Вложенные классы.
Похоже на представление базы данных в Django
Метаклассы
"""


def create_class_point(name, base, attrs):
    # name - имя класса
    # base - базовый класс (object)
    # attrs - атрибуты класса
    attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
    return type(name, base, attrs)


class Point(metaclass=create_class_point):
    def get_coords(self):
        return (0, 0)


pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())


class Meta(type):
    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs)
        cls.MAX_COORD = 100
        cls.MIN_COORD = 0


class Point(metaclass=Meta):
    def get_coords(self):
        return 0, 0


pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())
