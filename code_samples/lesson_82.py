"""
Lesson 82
17.12.2023

- Категории паттернов проектирования
- Паттерн "Абстрактная фабрика" - Abstract Factory
- Паттерн "Строитель" - Builder
- Паттерн "Фабричный метод" - Factory Method
- Паттерн "Стратегия" - Strategy
- Паттерн "Наблюдатель" - Observer
- Паттерн "Фасад" - Facade
"""

from typing import List

"""
Паттерн "Фасад" (Facade) — это структурный паттерн проектирования, используемый в программировании для 
создания простого интерфейса для взаимодействия с одной или несколькими более сложными системами. 

Этот паттерн часто применяется для облегчения работы с большими и сложными кодовыми библиотеками или API.
 
"""


# Сложная система (подсистемы)
class SubsystemOne:
    def operation(self):
        return "SubsystemOne: Ready!"


class SubsystemTwo:
    def operation(self):
        return "SubsystemTwo: Go!"


# Фасад
class Facade:
    def __init__(self):
        self._subsystem_one = SubsystemOne()
        self._subsystem_two = SubsystemTwo()

    def operation(self):
        return f"{self._subsystem_one.operation()}\n{self._subsystem_two.operation()}\nFacade: Finished!"


# Клиентский код
facade = Facade()
print(facade.operation())


# Подсистемы
class Engine:
    def start(self):
        return "Engine is starting"


class AirConditioner:
    def turn_on(self):
        return "AirConditioner is on"


class Radio:
    def play_music(self):
        return "Playing music"


# Фасад
class Car:
    def __init__(self):
        self.engine = Engine()
        self.ac = AirConditioner()
        self.radio = Radio()

    def turn_on_everything(self):
        return f"{self.engine.start()}\n{self.ac.turn_on()}\n{self.radio.play_music()}"


# Клиентский код
car = Car()
print(car.turn_on_everything())
