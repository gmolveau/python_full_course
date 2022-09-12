# bank.py
class BankAccount:
    def __init__(self, holder: str, balance: int = 0):
        if balance < 0:
            raise ValueError
        self._balance = balance
        self.holder = holder

    def deposit(self, amount: int):
        if amount < 0:
            raise ValueError
        self._balance += amount

    def withdraw(self, amount: int):
        if amount > self._balance:
            raise ValueError
        self._balance -= amount

    def transfer(self, amount: int, receiver: "BankAccount"):
        if amount > self._balance or amount < 0:
            raise ValueError
        self.withdraw(amount)
        receiver.deposit(amount)


account = BankAccount("esna")
account.deposit(100)
account.withdraw(30)
print(account._balance)

receiver = BankAccount("gregouz")
account.transfer(70, receiver)
print(account._balance)
print(receiver._balance)
