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
