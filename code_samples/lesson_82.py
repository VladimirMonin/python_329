"""
Lesson 82
17.12.2023

- Категории паттернов проектирования
- Паттерн "Абстрактная фабрика" - Abstract Factory
"""

from abc import ABC, abstractmethod

"""
Цель паттерна "Абстрактная Фабрика" — предоставить интерфейс для создания семейств взаимосвязанных или взаимозависимых 
объектов без указания их конкретных классов. 

Этот паттерн особенно полезен, когда система должна быть независимой от способа создания, 
компоновки и представления её продуктов.
"""

class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class WindowsButton(Button):
    def render(self) -> None:
        print("Рендеринг кнопки в стиле Windows")


class MacOSButton(Button):
    def render(self) -> None:
        print("Рендеринг кнопки в стиле MacOS")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()


class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()


# Клиентский код
def application(factory: GUIFactory) -> None:
    button = factory.create_button()
    button.render()


# Эмуляция выбора ОС
current_os = "Windows"
if current_os == "Windows":
    factory = WindowsFactory()
elif current_os == "MacOS":
    factory = MacOSFactory()

application(factory)
