"""
Lesson 34
19.11.2023

Класс внутри класса. Вложенные классы.
Похоже на представление базы данных в Django
"""

"""
В Django вложенные классы часто используются для определения метаданных 
моделей. Например, класс `Meta` внутри модели Django используется для 
задания таких параметров, как порядок сортировки 
объектов модели (`ordering`), названия таблицы в базе данных
 (`db_table`) и прочие конфигурационные настройки. 
 
Это стандартная практика в Django и является исключением из правила,
так как `Meta` служит для конфигурации внешнего класса.
"""


class Outer:
    def __init__(self, data):
        self.data = data
        self.inner = self.Inner(self)

    class Inner:
        def __init__(self, outer_instance):
            self.outer_data = outer_instance.data

        def get_outer_data(self):
            return self.outer_data


# Создаем экземпляр вложенного класса
outer = Outer('data')
inner = outer.inner

# Проверяем, что вложенный класс имеет доступ к данным внешнего класса
print(inner.get_outer_data())

