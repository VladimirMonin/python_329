"""
Lesson 82
17.12.2023

- Категории паттернов проектирования
- Паттерн "Абстрактная фабрика" - Abstract Factory
- Паттерн "Строитель" - Builder
- Паттерн "Фабричный метод" - Factory Method
"""

from typing import List

"""
Цель паттерна "Строитель" заключается в предоставлении способа конструирования сложного объекта пошагово. 
Этот паттерн отделяет конструкцию сложного объекта от его представления, 
так что один и тот же процесс конструирования может привести к созданию различных представлений.
"""


class Burger:
    def __init__(self):
        self.ingredients: List[str] = []

    def add_ingredient(self, ingredient: str) -> None:
        self.ingredients.append(ingredient)


class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_lettuce(self) -> None:
        self.burger.add_ingredient("салат")

    def add_tomato(self) -> None:
        self.burger.add_ingredient("помидор")

    def add_cheese(self) -> None:
        self.burger.add_ingredient("сыр")

    def get_burger(self) -> Burger:
        return self.burger


# Клиентский код
builder = BurgerBuilder()
builder.add_cheese()
builder.add_lettuce()
burger = builder.get_burger()
print(burger.ingredients)


class Document:
    def __init__(self):
        self.pages: List[str] = []

    def add_page(self, page: str) -> None:
        self.pages.append(page)


class DocumentBuilder:
    def __init__(self):
        self.document = Document()

    def add_title(self, title: str) -> None:
        self.document.add_page(f"Заголовок: {title}")

    def add_paragraph(self, paragraph: str) -> None:
        self.document.add_page(f"Абзац: {paragraph}")

    def add_footer(self, footer: str) -> None:
        self.document.add_page(f"Подвал: {footer}")

    def get_document(self) -> Document:
        return self.document


# Клиентский код
doc_builder = DocumentBuilder()
doc_builder.add_title("Документация на Python")
doc_builder.add_paragraph("Python - мощный язык программирования.")
doc_builder.add_footer("Конец документа")
document = doc_builder.get_document()
print("\n".join(document.pages))
