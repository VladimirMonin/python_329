"""
Lesson 28
29.10.2023

Тема: Наследование в ООП

- Концепция наследования в ООП
- Наследуются и поля и методы
- Расширение функционала родительского класса в дочернем классе
- Расширение атрибутов родительского класса в дочернем классе
- Как пишется документация к классу и методу (pep 257)
(https://peps.python.org/pep-0008/#documentation-string)
- Как посмотреть документацию к классу __doc__
- Как посмотреть аттрибуты класса __dict__ и __dir__
- Переопределение родительских полей и методов
- Многоуровневое наследование
- Множественное наследование
"""


# Множественное наследование - это когда дочерний класс наследует атрибуты и методы
# сразу от нескольких родительских классов

class Login:
    """
    Основной класс для логина на сайте, который
    описывает общие поля и методы для всех типов логинов
    """

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def input_user_name(self):
        print(f'Ввел имя пользователя {self.login}')

    def input_password(self):
        print(f'Ввел пароль {self.password}')

    @staticmethod
    def click_login_button():
        print('Нажал на кнопку логин')


class PinLoginMixin:
    """
    Миксин для логина по пин-коду
    """

    def __init__(self, pin: str):
        self.pin = pin

    def input_pin(self):
        print(f'Ввел пин-код {self.pin}')

    @staticmethod
    def click_submit_pin_button():
        print('Нажал на кнопку подтвердить пин')


class TwoFactorAuthMixin:
    """
    Миксин для логина с двухфакторной аутентификацией
    """

    def __init__(self, code: str):
        self.code = code

    def input_code(self):
        print(f'Ввел код {self.code}')

    @staticmethod
    def click_submit_code_button():
        print('Нажал на кнопку подтвердить код')


class LoginPin(Login, PinLoginMixin):
    """
    Класс для логина по пин-коду
    """

    def __init__(self, login: str, password: str, pin: str):
        Login.__init__(self, login, password)
        PinLoginMixin.__init__(self, pin)


class LoginTwoFactorAuth(Login, TwoFactorAuthMixin):
    """
    Класс для логина с двухфакторной аутентификацией
    """

    def __init__(self, login: str, password: str, code: str):
        Login.__init__(self, login, password)
        TwoFactorAuthMixin.__init__(self, code)


class Controller(LoginTwoFactorAuth):
    """
    Класс который запускает всю программу используя LoginTwoFactorAuth
    """

    def __init__(self, login: str, password: str, code: str):
        LoginTwoFactorAuth.__init__(self, login, password, code)

    def run(self):
        self.input_user_name()
        self.input_password()
        self.click_login_button()
        self.input_code()
        self.click_submit_code_button()


# Запуск программы
def main():
    pin_login = LoginPin('user', '123', '1234')
    pin_login.input_user_name()  # Метод input_user_name находится в классе Login
    pin_login.input_password()  # Метод input_password находится в классе Login
    pin_login.click_login_button()  # Метод click_login_button находится в классе Login
    pin_login.input_pin()  # Метод input_pin находится в классе PinLoginMixin
    pin_login.click_submit_pin_button()  # Метод click_submit_pin_button находится в классе PinLoginMixin


if __name__ == '__main__':
    main()

# Второй вариант запуска программы
if __name__ == '__main__':
    controller = Controller('user', '123', '1234')
    controller.run()