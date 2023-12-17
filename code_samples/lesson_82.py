"""
Lesson 82
17.12.2023

- Категории паттернов проектирования
- Паттерн "Абстрактная фабрика" - Abstract Factory
- Паттерн "Строитель" - Builder
- Паттерн "Фабричный метод" - Factory Method
- Паттерн "Стратегия" - Strategy
- Паттерн "Наблюдатель" - Observer
"""

from typing import List

"""
Паттерн "Наблюдатель" (Observer) является одним из ключевых поведенческих паттернов проектирования. 
Он предназначен для установления отношения "один-ко-многим" между объектами, таким образом, 
что при изменении состояния одного объекта (издателя или субъекта) все зависимые объекты (наблюдатели) 
автоматически уведомляются и обновляются.
 
"""


class EventListener:
    def notify(self, event):
        raise NotImplementedError


class EmailAlertListener(EventListener):
    def notify(self, event):
        print(f"Отправка уведомления на электронную почту: {event}")


class LoggingListener(EventListener):
    def notify(self, event):
        print(f"Логирование события: {event}")


class TelegramAlertListener(EventListener):
    def notify(self, event):
        print(f"Отправка уведомления в телеграм: {event}")


class EventManager:
    def __init__(self):
        self.listeners = []

    def subscribe(self, listener):
        self.listeners.append(listener)

    def unsubscribe(self, listener):
        self.listeners.remove(listener)

    def notify(self, event):
        for listener in self.listeners:
            listener.notify(event)


# Пример использования
event_manager = EventManager()
email_listener = EmailAlertListener()
logging_listener = LoggingListener()
telegram_listener = TelegramAlertListener()

event_manager.subscribe(email_listener)
event_manager.subscribe(logging_listener)
event_manager.subscribe(telegram_listener)
event_manager.notify("Пользователь вошел в систему")

event_manager.unsubscribe(email_listener)
event_manager.notify("Пользователь вышел из системы")
