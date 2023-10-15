"""
lesson 25
15.10.2023

1. Повторили lesson_24.py
2. Метод __new__ - это метод, который вызывается при создании экземпляра класса.
Посмотрели что именно он создает экземпляр класса
3. Аттрибут класса и @staticmethod. Сделали ID и счетчик матерешек
4. Посмотрели на базовый вариант наследования и super()
5. Посмотрели на @classmethod и вызов инициализатора родительских классов
"""

"""
Давай разберёмся.

### Как работает этот код:

1. **Классы `SmallMatryoshka`, `MediumMatryoshka`, `BigMatryoshka`**:
   Эти классы представляют собой разные типы матрешек: маленькие, средние и большие. Структура наследования указывает
    на то, что `MediumMatryoshka` наследует `SmallMatryoshka`, а `BigMatryoshka` наследует `MediumMatryoshka`.

2. **Атрибут класса `counter`**:
   Это переменная на уровне класса, которая используется для подсчета количества созданных экземпляров 
   каждого типа матрешек. Когда мы создаем новую матрешку, `counter` увеличивается на 1.

3. **Метод `__init__`**:
   Это специальный метод, который автоматически вызывается при создании нового экземпляра класса
    (то есть при инициализации). В этом методе происходит увеличение счетчика `counter` и присвоение уникального ID матрешке.

4. **Метод `super().__init__()`**:
   Этот метод вызывает конструктор родительского класса. Это значит, что при создании 
   `MediumMatryoshka`, например, сначала будет создана `SmallMatryoshka`, и затем `MediumMatryoshka`.

### Что такое метод класса:

В Python существует три основных типа методов:

1. **Обычные методы (instance methods)**:
   Это наиболее часто используемый тип метода. Они принимают параметр `self`,
    который ссылается на экземпляр класса, и обычно используются для работы с атрибутами экземпляра.

2. **Статические методы (`@staticmethod`)**:
   Это методы, которые относятся к классу, но не могут изменять состояние 
   класса или его экземпляра. Они определяются с помощью декоратора `@staticmethod` 
   и не принимают ни `self`, ни `cls` в качестве первого параметра.

3. **Методы класса (`@classmethod`)**:
   Они принимают параметр `cls`, который ссылается на сам класс, а не на его экземпляр.
    Это позволяет им работать с атрибутами класса, а не с атрибутами экземпляра. 
    В нашем коде метод `total_made` является методом класса. Он возвращает значение счетчика для соответствующего класса.

В отличие от обычных методов, методы класса не требуют создания экземпляра класса для вызова.
 Вы можете вызывать их напрямую из класса, как это делается в строке:
```python
print(f"Всего маленьких матрешек: {SmallMatryoshka.total_made()}")
```

Декоратор `@classmethod` перед методом указывает, что данный метод является методом класса.
"""


class SmallMatryoshka:
    counter = 0  # общий счетчик для всех маленьких матрешек

    def __init__(self):
        SmallMatryoshka.counter += 1
        self.id = SmallMatryoshka.counter  # уникальный ID матрешки
        print(f"Создана маленькая матрешка с ID {self.id}!"
              f"Всего маленьких матрешек: {SmallMatryoshka.counter}!")

    @classmethod
    def total_made(cls):
        return cls.counter


class MediumMatryoshka(SmallMatryoshka):
    counter = 0  # общий счетчик для всех средних матрешек

    def __init__(self):
        super().__init__()
        MediumMatryoshka.counter += 1
        self.id = MediumMatryoshka.counter
        print(f"Создана средняя матрешка с ID {self.id}!"
              f"Всего средних матрешек: {MediumMatryoshka.counter}!")

    @classmethod
    def total_made(cls):
        return cls.counter


class BigMatryoshka(MediumMatryoshka):
    counter = 0  # общий счетчик для всех больших матрешек

    def __init__(self):
        super().__init__()
        BigMatryoshka.counter += 1
        self.id = BigMatryoshka.counter
        print(f"Создана большая матрешка с ID {self.id}!"
              f"Всего больших матрешек: {BigMatryoshka.counter}!")

    @classmethod
    def total_made(cls):
        return cls.counter


# Тестирование
big_m = BigMatryoshka()
big_m2 = BigMatryoshka()
big_m3 = BigMatryoshka()

medium_m = MediumMatryoshka()
print("-----")
print(f"Всего маленьких матрешек: {SmallMatryoshka.total_made()}")
print(f"Всего средних матрешек: {MediumMatryoshka.total_made()}")
print(f"Всего больших матрешек: {BigMatryoshka.total_made()}")
