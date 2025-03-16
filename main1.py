class BankAccount:
    """Класс для банковского счёта"""

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        """Пополнение счёта"""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Снятие со счёта"""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
        return self.balance


class Logger1:
    """Простой логгер, который записывает сообщения в файл"""

    def __init__(self, file_path):
        self.file_path = file_path

    def log(self, message):
        """Записывает сообщение в файл"""
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(message + "\n")

    def get_logs(self):
        """Читает все сообщения из файла"""
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.readlines()


class DiscountCalculator:
    """Калькулятор скидок"""

    def apply_discount(self, price, discount):
        """Применяет скидку к цене"""
        if not isinstance(discount, (int, float)): raise TypeError
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if not (0 < discount < 100):
            raise ValueError("Скидка должна быть от 0 до 100")

        return price * (1 - discount / 100)

import json

class DataProcessor:
    """Класс для чтения и обработки JSON-файлов"""

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        """Читает JSON-файл и возвращает данные"""
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_value(self, key):
        """Получает значение по ключу из JSON"""
        data = self.load_data()
        return data.get(key, None)