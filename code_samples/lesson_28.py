"""
Lesson 28
29.10.2023

Тема: Наследование в ООП

- Концепция наследования в ООП
- Наследуются и поля и методы
- Расширение функционала родительского класса в дочернем классе
- Расширение атрибутов родительского класса в дочернем классе
- 10 МИНУТ ПЕРЕРЫВ :)
- Как пишется документация к классу и методу (pep 257)
(https://peps.python.org/pep-0008/#documentation-string)
- Как посмотреть документацию к классу __doc__
- Как посмотреть аттрибуты класса __dict__ и __dir__
"""


class Transport:
    """
    Класс Transport. Родительский класс для всех транспортных средств
    Имеет методы:
    - move - движение
    - stop - остановка

    Имеет аттрибуты:
    - model - модель
    - color - цвет
    - max_speed - максимальная скорость

    """
    def __init__(self, model: str, color: str, max_speed: int):
        self.model = model
        self.color = color
        self.max_speed = max_speed

    def move(self):
        """
        Метод движение
        :return: None
        """
        print(f'{self.model} едет со скоростью {self.max_speed} км/ч')

    def stop(self):
        """
        Метод остановки
        :return: None
        """
        print(f'{self.model} остановился')


class Bike(Transport):
    """
    Класс Bike. Дочерний класс для класса Transport
    Имеет методы:
    - move - движение
    - stop - остановка

    Имеет аттрибуты:
    - model - модель
    - color - цвет
    - max_speed - максимальная скорость
    - wheels - колеса

    """
    def __init__(self,  model: str, color: str,
                 max_speed: int, wheels: int):

        super().__init__(model, color, max_speed)
        self.wheels = wheels

    def move(self):
        """
        Метод движение
        :return: None
        """
        print(f'{self.model} едет со скоростью '
              f'{self.max_speed} км/ч на {self.wheels} колесах')

    def stop(self):
        """
        Метод остановки
        :return: None
        """
        print(f'{self.model} остановился')


# Создаем экземпляр класса Transport и экземпляр класса Bike
transport = Transport('Tesla', 'red', 200)
bike = Bike('BMX', 'black', 20, 2)
a = 'чебурек'

# Вызываем методы отображающие документацию
print(transport.move.__doc__)

# Вызываем методы отображающие аттрибуты класса
print(transport.__dict__)

# Вызываем методы отображающие аттрибуты класса
print(transport.__dir__())
