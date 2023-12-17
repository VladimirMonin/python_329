"""
Lesson 82
17.12.2023

- Категории паттернов проектирования
- Паттерн "Абстрактная фабрика" - Abstract Factory
- Паттерн "Строитель" - Builder
- Паттерн "Фабричный метод" - Factory Method
- Паттерн "Стратегия" - Strategy
"""

from typing import List

"""
 Паттерн "Стратегия" – это один из фундаментальных шаблонов проектирования, 
 который позволяет определить семейство алгоритмов, 
 инкапсулировать каждый из них и сделать их взаимозаменяемыми. 
 
 Этот паттерн позволяет изменять алгоритмы независимо от клиентов, которые их используют.
"""


class Strategy:
    def execute(self, data):
        raise NotImplementedError


class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return sum(data)


class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return max(data)

class ConcreteStrategyС(Strategy):
    def execute(self, data):
        return min(data)


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.execute(data)


# Пример использования
data = [1, 2, 3, 4, 5]
context = Context(ConcreteStrategyA())
result = context.execute_strategy(data)
print("Результат ConcreteStrategyA:", result)

context.set_strategy(ConcreteStrategyB())
result = context.execute_strategy(data)
print("Результат ConcreteStrategyB:", result)

context.set_strategy(ConcreteStrategyС())
result = context.execute_strategy(data)
print("Результат ConcreteStrategyС:", result)


