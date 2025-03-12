def is_palindrome(s):
    if not s: return False
    return s == s[::-1]

def average(lst):
    if not lst: raise ValueError("List is empty")
    if len(lst) == 1 and lst[0] == "": raise ValueError("")
    return sum(lst) / len(lst)


class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if isinstance(amount, str): raise TypeError()
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0: raise ValueError()
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


class Library:

    def __init__(self):
        self.__books = {}

    def get_books(self):
        return self.__books

    def add_book(self, book):
        if not isinstance(book, str): raise TypeError
        if book == '': raise ValueError
        if book not in self.__books:
            self.__books[book] = 1
        else:
            self.__books[book] += 1

    def remove_book(self, book):
        if self.find_book(book):
            if book in self.__books:
                self.__books[book] -= 1
                if self.__books[book] == 0:
                    del self.__books[book]
        else:
            raise ValueError

    def find_book(self, book):
        return self.__books.get(book, 0) > 0