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
