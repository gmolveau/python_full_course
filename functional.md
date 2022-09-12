# Functional programming

monad
map
reduce
filter

pattern matching

everything is a function
and function are pure (no side effect)
    > consequence = more robust programs
    > deterministe
        > more testable
    in python, only by convention, no guarantee by the language
+ immutable data structures
    string, tuple, collections.namedTuple
lazy evaluation (generator)
preserve state in functions
recursion instead of loops/iteration
closures
functools, itertools, lambda map, filter

freezing
    useful when debugging legacy code
    replace a data structe by a frozen one and python will tell you what code tried to edit the data

    __getitem__
    __setitem__
        raise KeyError
    freeze
        self.__frozen = True
    unfreeze

### disadvantages

recursion is hard (harder than loop)
immutable data structure may increase run times
c compliqué
trouver des bons devs c compliqué

```python
# python 3.10

from abc import ABC

class NotIterable(ABC):
    @classmethod
    def __subclasshook__(cls, C):
        return not hasattr(C, "__iter__")

def f(x):
    match x:
        case NotIterable():
            print(f"{x} is not iterable")
        case _:
            print(f"{x} is iterable")
```


```python
# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13

# There are also anonymous functions
(lambda x: x > 2)(3)                  # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

# There are built-in higher order functions
list(map(add_10, [1, 2, 3]))          # => [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]

# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list which can itself be a nested list
[add_10(i) for i in [1, 2, 3]]         # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

# You can construct set and dict comprehensions as well.
{x for x in 'abcddeef' if x not in 'abc'}  # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```


```python
def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1

>>> it = counter(10)
>>> next(it)
0
>>> next(it)
1
>>> it.send(8)
8
>>> next(it)
9
```

---

In pure functional programming, the program written as a function must only work with its direct inputs, or arguments passed through the parameters. It cannot work with any other sources of information, or program state, including databases.

The key point of the functional paradigm is putting a nice wall around these stateful interactions, and distilling the functionally pure core, which is logically consistent and easy to prove to be correct.

## Resources

- <https://docs.python.org/3/howto/functional.html>
- <https://youtu.be/2OdyPEY77X8> - Learn Advance Python Functional Programming - Episode 6 - AutomationCat
- <https://youtu.be/Ta1bAMOMFOI> - Functional Programming with Python by Mike Müller
- <https://youtu.be/sqV3pL5x8PI> - Programming Paradigms - Computerphile
- <https://youtu.be/eis11j_iGMs> - Lambda Calculus - Computerphile
- <https://youtu.be/xJCPpDlk9_w?list=PLP8GkvaIxJP1z5bu4NX_bFrEInBkAgTMr> - Functional Programming in Python: Immutable Data Structures - Real Python
- <https://github.com/hemanth/functional-programming-jargon>
