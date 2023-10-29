"""
Lesson 28
29.10.2023

Тема: Наследование в ООП

- Концепция наследования в ООП
- Наследуются и поля и методы
- Расширение функционала родительского класса в дочернем классе
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
    # Новый метод
    def make_jump(self):
        print(f'{self.model} прыгает')


# Создаем экземпляр класса Bike и Transport вызываем методы

transport: Transport = Transport('BMW', 'red', 200)
transport.move()
transport.stop()

bike: Bike = Bike('BMX', 'black', 40)
bike.move()
bike.make_jump()


