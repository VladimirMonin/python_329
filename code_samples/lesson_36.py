"""
Lesson 34
19.11.2023

Класс внутри класса. Вложенные классы.
Похоже на представление базы данных в Django
Метаклассы
"""


class МetaWomen(type):
    #
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            setattr(self, key, value)

    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs
        cls.__init__ = МetaWomen.create_local_attrs


class Women(metaclass=МetaWomen):
    title = 'заголовок'
    content = 'контент'
    photo = 'путь к фото'


w = Women()
print(w.__dict__)
