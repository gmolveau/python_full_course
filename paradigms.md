The imperative approach defines a program as a sequence of statements that change the program's state until it reaches the final state.

Procedural programming is a type of imperative programming where we construct programs using procedures or subroutines. One of the popular programming paradigms known as Object-Oriented Programming (OOP) extends procedural programming concepts.

In contrast, the declarative approach expresses the logic of a computation without describing its control flow in terms of a sequence of statements.

Simply put, the declarative approach's focus is to define what the program has to achieve rather than how it should achieve it. Functional programming is a subset of the declarative programming languages.

> <https://www.baeldung.com/java-functional-programming>

---

source = https://youtu.be/cgVVZMfLjEI

imperative

sum = 0
for i in range(10):
    sum = sum + i

- haskell
sum[1..10]

sum :: [Int] -> Int
    signature
sum [n] = n
sum (n, ns) = n + sum (ns) #recursif

sum [4,5,2]
    4 + sum [5,2]
        5 + sum [2]
            2
    > 11
    definir la fonction avec du pattern matching
    une fonction peut avoir plusieurs definitions en fonction de l'entrée

    pattern matching = maniere de choisir quelle definition appliquer selon la structure de l'entrée

on voit ici entre les 2 "sum" que l'imperative utilise une variable mutable

- https://anandology.com/python-practice-book/functional-programming.html

# Cash Register example

## OOP

```python
class BankAccount:
    def __init__(self):
        self._balance = 0

>>> account = BankAcount()
>>> account.balance
# 0

class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount: int):
        self._balance += amount

    def withdraw(self, amount: int):
        self._balance -= amount

>>> account.deposit(100)
>>> account.withdraw(30)
>>> account._balance
70

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
```

## Functional (Racket)

## Logic Programming (Prolog)

- https://people.cs.ksu.edu/~schmidt/301s11/Lectures/prologS.html
- https://www-apr.lip6.fr/~manoury/Enseignement/2018-19/APS/prolog.pdf
- exercices : https://lipn.univ-paris13.fr/~pagani/TP_Prolog/TP_Prolog.html

- VARIABLES are in CAPS
- constants are in lowercase

facts & clauses :
facts = elementary facts
    syntax : ends with a `dot`
clauses = relationship between facts

state(bretagne).
border(bretagne, normandie).
border(bretagne, paysdelaloire).
border(normandie, idf).

adjacent(X,Y) :- border(X,Y).
// query
?- adjacent(bretagne, normandie)
yes
?- adjacent(normandie, bretagne)
no

what ? we're missing a clause (the invert one)

adjacent(X,Y) :- border(Y,X).

// other example

father(homer, bart).
father(homer, list).
mother(marge, lisa).
mother(marge, bart).

sibling(X, Y) :-
    mother(Z, X),
    mother(Z, Y),
    X \== Y.

sibling(X, Y) :-
    father(Z, X),
    father(Z, Y),
    X \== Y.

// query
?- sibling(X, Y).
X = bart
Y = lisa

// lists

[F | R]
// F = First
// | = "bar"
// R = Rest

// example
[1, 2, 3]
F = 1
R = [2, 3]

_ (s'appelle "meh")

member(X, [X | _ ]).
member(X, [_ | R]) :- member(X, R).

change(amount, coins, change)

change(0, _, []).
change(A, [F | R], [F | X]) :-
    A >= F,
    B is A - F,
    change(B, [F | R], X).
change(A, [_ | R], X) :-
    A > 0,
    change(A, R, X).

## Procedural (Assembly)

