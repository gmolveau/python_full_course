# bank.py
from typing import Self


class BankAccount:
    def __init__(self, holder: str, balance: int = 0):
        if balance < 0:
            raise ValueError
        self._balance = balance
        self.holder = holder

    def deposit(self, amount: int) -> int:
        if amount <= 0:
            raise ValueError
        self._balance += amount
        return self._balance

    def withdraw(self, amount: int) -> int:
        if amount > self._balance:
            raise ValueError
        self._balance -= amount
        return self._balance

    def transfer(self, amount: int, receiver: Self) -> int:
        if amount > self._balance or amount < 0:
            raise ValueError
        self.withdraw(amount)
        receiver.deposit(amount)
        return self._balance


account = BankAccount("esna")
account.deposit(100)
account.withdraw(30)
print(account._balance)

receiver = BankAccount("gregouz")
account.transfer(70, receiver)
print(account._balance)
print(receiver._balance)
