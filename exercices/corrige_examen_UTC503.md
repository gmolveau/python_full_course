# EXAMEN ESNA 2021 UTC503

## paradigme impératif

### exercice 1

```python
# sponge_input.py
import random


def convert(sentence):
    sentence = sentence.lower()
    r = []
    for carac in sentence:
        if carac.isspace():
            r.append(carac)
        else:
            if random.random() < 0.5:  # 50% chance
                r.append(carac.upper())
            else:
                r.append(carac)
    return ''.join(r)

def main():
    sentence = input("Please enter your meme sentence: ")
    converted_sentence = convert(sentence)
    print(converted_sentence)


if __name__ == "__main__":
    main()
```

### exercice 2

```python
# sponge_cli.py
import random
import click


def convert(sentence):
    sentence = sentence.lower()
    r = []
    for carac in sentence:
        if carac.isspace():
            r.append(carac)
        else:
            if random.random() < 0.5:  # 50% chance
                r.append(carac.upper())
            else:
                r.append(carac)
    return ''.join(r)


@click.command()
@click.argument('sentence')
def meme(sentence):
    '''converts a sentence to a spongebob meme'''
    meme_sentence = convert(sentence)
    print(meme_sentence)


if __name__ == '__main__':
    meme()

# run with: python3 spongebob_cli.py "mais où va le monde"
```

### exercice 3

```python
# sponge_generator.py
pass # xd
```

## paradigme objet

### exercice 4

```python
# bank.py
class BankAccount:
    def __init__(self, holder: str, balance: int=0):
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
```

### exercice 5

```python
# cash.py
class CashRegister:
    def __init__(self):
        self.drawer = [500, 200, 100, 50, 20, 10, 5, 2, 1]

    def make_change(self, owed, tendered):
        difference = tendered - owed
        change = []
        i = 0
        denomination = self.drawer[i]
        while difference > 0:
            if difference < denomination :
                i += 1
                denomination = self.drawer[i]
                continue
            change.append(denomination)
            difference -= denomination
        return change

# le client donne 50€ pour régler 24€ de courses
cash = CashRegister()
change = cash.make_change(24, 50)
print(change)
```

## paradigme fonctionnel

### exercice 6

```python
# functional.py
import functools

def factorial(n):
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1
    else:
        return functools.reduce(lambda x,y: x*y, range(1, n+1))
```

### exercice 7

```python
# palindrome.py
l = ['kayak', 'esna', 'pasoufcetexam', 'ressasser']

# 1.
lamb = list(filter(lambda x: x == x[::-1], l))

# 2.
comp = [x for x in l if x == x[::-1]]

# 3.
l2 = []
def clos(x):
    if x == x[::-1]:
        l2.append(x)

[clos(x) for x in l]
```

### exercice 8

```python
# trace.py
def trace(f):
    def g(x):
        print(f.__name__, x)
        value = f(x)
        return value
    return g

@trace
def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(3))
```

## paradigme logique

### exercice 9

```prolog
% socrate.pl
mortel(X) :- homme(X).
homme(socrate).
/*
?- mortel(X)
X=socrate
*/
```

### exercice 10

```prolog
% beyblade.pl

aime(maximilien,beyblade).
aime(squeezie,X) :- aime(X,beyblade).
mange(X,Y) :- youtubeur(X), aime(X,Y).
youtubeur(squeezie).

/*
mange(X,Y)
X=squeezie
Y=maximilien
*/
```
