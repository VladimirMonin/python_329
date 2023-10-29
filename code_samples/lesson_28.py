"""
Lesson 28
29.10.2023

Тема: Наследование в ООП

- Концепция наследования в ООП
- Наследуются и поля и методы
- Расширение функционала родительского класса в дочернем классе
- Расширение атрибутов родительского класса в дочернем классе
"""


class Transport:
    def __init__(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed

    def move(self):
        print(f'{self.model} едет со скоростью {self.max_speed} км/ч')

    def stop(self):
        print(f'{self.model} остановился')


class Bike(Transport):
    def __init__(self, model, color, max_speed, wheels):
        super().__init__(model, color, max_speed)
        self.wheels = wheels

    def move(self):
        print(f'{self.model} едет со скоростью {self.max_speed} км/ч на {self.wheels} колесах')

    def stop(self):
        print(f'{self.model} остановился')


# Создаем экземпляр класса Transport и экземпляр класса Bike
transport = Transport('Tesla', 'red', 200)
bike = Bike('BMX', 'black', 20, 2)
a = 'чебурек'
