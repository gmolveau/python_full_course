# Python basics

Python was conceived in the late 1980s by [Guido van Rossum](https://twitter.com/gvanrossum/status/1017546023227424768).
Python 3.0 final was released on December 3rd, 2008.

So please use python3 ;-) #nomorepython2

Its name is based on the "Monty Python".

Python is :
- an interpreted language
- [strongly typed and dynamically typed](https://wiki.python.org/moin/Why%20is%20Python%20a%20dynamic%20language%20and%20also%20a%20strongly%20typed%20language)
    - note : python can also be statically typed through [`type hinting`](https://www.python.org/dev/peps/pep-0484/)
    - Note: some languages are weakly typed (JavaScript), some are strongly typed (Python) and some are statically typed (Go, Rust). Being strongly typed means you can't perform operations inappropriate to the type, so for example: in Python you can't add a number typed variable with a string typed variable.
- garbage collected

### ZEN of python

A collection of 19 principles that influence the conception and usage of the language.

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

### CPython

CPython ? What is that ?

> CPython is the reference implementation of the Python programming language. Written in C and Python, CPython is the default and most widely used implementation of the Python language.

CPython can be defined as both an interpreter and a compiler as it compiles Python code into bytecode before interpreting it.
> -- [Wikipedia](https://en.wikipedia.org/wiki/CPython)

/!\ **Everything in Python is an object.**

## Comments

Single line comments start with a `#` : `# this is a comment`

Multiline comments can be written using triple single-quotes ou double-quotes :

```python
''' ok so this is
    a multiline comment
'''

""" and this is
    another one
    dj khaled
"""
```

We usually use triple-quotes to write documentation, also called [docstrings](https://www.python.org/dev/peps/pep-0257/#id5).

## Variables

You don't need to declare a variable before using it, nor its type.

A variable stores a piece of data, and gives it a specific name.

```python
username = "greg"
```

### naming

The name of a variable should use the `snake_case` convention.

```python
# wrong
dictOfHashes = ['abcedf123' ...]
# right
dict_of_hashes = ['abcedf123' ...]
```

Reading a variable name should give you a hint about its meaning.

```python
# wrong
a = "https://myapi.heroku.com/api/v1/register"
# right
register_url = "https://myapi.heroku.com/api/v1/register"
```

You should not put the type of the variable in its name.

```python
# wrong
list_of_username = ["greg", "alex"]
# right
usernames = ["greg", "alex"]
```

Finally, you should **NOT** use reserved keywords for a variable name (eg. `dict`, `from`)

### Memory management (under the hood)

TODO

<https://realpython.com/pointers-in-python/>

<https://pythontutor.com/render.html#code=a%20%3D%20%22yes%22%0Ab%20%3D%20%22no%22%0Al%20%3D%20%5Ba,b%5D%0Al.append%283%29&cumulative=true&curInstr=4&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false>

## primitive/native data types

the most common types are :

- numbers : integers ; floating point numbers (floats) ; complex
- string
- list
- dict
- tuple
- boolean (bool) : `True` and `False`
    - `None`, 0, and empty strings/lists/dicts/tuples all evaluate to `False`

but there's a lot of other special ones :

- iterators
- range
- bytes ; bytearray ; memoryview
- frozenset

remember when we said that everything in python is an object ? all these types are objects, represented by a class.

```python
>>> b = True
>>> type(b)
<class 'bool'>
```

more about what's a `class` later ;-)

Note : all native types are available [here](https://docs.python.org/fr/3.7/library/stdtypes.html)

### casting / converting a type to another one

a variable can be converted to another type, for example :

```python
>>> num = "3"
>>> type(num)
<class 'str'>
>>> num = int(num)
>>> type(num)
<class 'int'>
```

### operators

Python comes with a lot of operators that you can use and combine.

You can use them with variables of the same type, and also with variables of different types.

But be careful, some operations don't exist and will raise an Exception and crash your app.

```python
>>> a = 1
>>> b = 2
>>> d = a / b # a division always gives a float even if the division is perfect
>>> print(type(d))
<class 'float'>
>>> print(3 // 2) # euclidean division rounds down the result of the division
1
>>> print(7 % 3) # modulo operator
1
>>> print(2 ** 6) # exponential operator (also called power)
64
>>> c = a + b
>>> c += 1 # equivalent to c = c + 1 # not all languages have this notation
>>> print(c)
4
>>> s = "username"
>>> p = "greg"
>>> print(s + ": " + p)
username: greg
>>> o = p * 3
>>> print(o)
greggreggreg
>>> l = [1,2,3]
>>> ll = l * 2
>>> print(ll)
[1, 2, 3, 1, 2, 3]
>>> lll = l + ll
>>> print(lll)
[1, 2, 3, 1, 2, 3, 1, 2, 3]
# boolean operators
>>> print(a == b)
False
>>> print(a != b)
True
>>> a = not True # negation operation
>>> print(a)
False
>>> a == b and b == c or c != d
False
# python alse let's you chain operators nicely for example for range
>>> a < b < c
True
```

### `is` keyword

`is` keyword can be a little confusing and can lead to error later if not properly used.

`is` checks that two variables refer to the same `object` (memory address).

`==` checks if two `objects` have the same `value`.

See the difference here ?

```python
>>> a = [1, 2, 3, 4]
>>> b = a # make `b` points to the same 'place' as `a`
>>> b is a
True
>>> b = [1, 2, 3, 4]  # re-use `b` to create a new list
>>> b is a
False # even if the two lists have the same values, they dont have the same address
>>> b == a
True
```

We can dig deeper with the help of the `id` function, which returns the memory address of an object.

```python
>>> id(a)
4454500352
>>> id (b)
4454506560
```

### None

`None` is an object. Always use `is` to compare a variable to `None`.

### mutability

some `sequences` (`tuples` and `strings` for example) are `immutable` which means that you can't edit them after creation.

```python
>>> s = "hello"
>>> s[0] = "a"
TypeError: 'str' object does not support item assignment
>>> t = (1, 2, 3)
>>> t[0] = 4
TypeError: 'tuple' object does not support item assignment
```

If you wan't to edit them, you need to reassign them.

```python
>>> s = "hello"
>>> s = "a" + s[1:]
>>> print(s)
"aello"
```

### type hinting

[PEP 484](https://www.python.org/dev/peps/pep-0484/)

## functions (intro)

quick explanation about functions, we're not going to too much into details here but we need to address the subject a little.

definition - def f()

call - f()

TODO

- Signature
- Arguments positionnels vs. Arguments mots clés
- Attention au nommage
- DRY / YAGNI
- fonction vs procedure : fonction renvoie une valeur et une procédure exécute uniquement des commandes
- LGI : Lorsque Python rencontre une variable, il va traiter la résolution de son nom avec des priorités particulières. D'abord il va regarder si la variable est locale, puis si elle n'existe pas localement, il vérifiera si elle est globale et enfin si elle n'est pas globale, il testera si elle est interne

- `def f(arg: type) -> None:`

- `ts("obama", False, 20, True)`
`twitter_search(username=‘@obama’, retweets=False, numtweets=20, unicode=True)`

- attention aux arguments par défaut

```python
def oops(l = []):
    l.append("ok")
    return l

print(oops())
print(oops())
# ["ok"]
# ["ok", "ok"]
```

- visualize memory here : <https://pythontutor.com/render.html#code=def%20oops%28l%20%3D%20%5B%5D%29%3A%0A%20%20%20%20l.append%28%22ok%22%29%0A%20%20%20%20return%20l%0A%0Aprint%28oops%28%29%29%0Aprint%28oops%28%29%29&cumulative=true&curInstr=11&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false>

## built-in functions

dir()
help()

## classes (intro)

wait, isn't it only the beginning of the course ? sorry again, we need to address this subject too :)

TODO

### methods

TODO

### magic methods

TODO

`__len__`

## printing

TODO

### f-string

TODO

## Lists

A list is a `sequence object` that stores an ordered sequence of objects, which can be of different types (even lists, yes).

```python
>>> alist = ["lion", 1, False, ["o", "k"]]
```

Each element of a list can be accessed by its index (which begins at 0).

```python
>>> alist[0]
"lion"
>>> alist[3]
False
```

Trying to access an invalid index results in an Exception `IndexError` being raised.

```python
>>> alist[4]
Traceback (innermost last):
  File "<stdin>", line 1, in ?
IndexError: list index out of range
```

One of the under-rated feature of python is its negative index !
If you want to access the last element of a list without having to calculate its size, use the `-1` index !

```python
l = [1, 2, 3]
#    0  1  2   ---> positive index
#   -3 -2 -1   ---> negative index
```

also works for string obviously :

```python
+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
  0   1   2   3   4   5   6
 -6  -5  -4  -3  -2  -1
```

### Slicing

Slicing is used to get a part of a `sequence`. A lot of tricks can be done with slicing.

The syntax of a slice is as followed : `[<start>:<stop>:<step>]`.

```python
>>> l = [1, 2, 3, 4]
>>> print(l[0:3:1])
[1, 2, 3, 4]
# copy a list
>>> o = l[:] # [:] is equivalent to [0 : len(l)-1 : 1]
# create a copy of the list in reverse order
>>> r = l[::-1] # this is a real nice trick
>>> print(r)
[4, 3, 2, 1]
```

### Common list methods

- `.append(<value>)` adds an element at the end of the list
- `.pop()` *removes* the last element of the list and returns it
- `.remove(<value>)` removes the first occurence of a value (or raises a `ValueError` if the value can't be found)
- `.insert(<index>, <value>)` adds an element at the given index
- `.index(<value>)` returns the index of the first occurence of a value (or raises a `ValueError` if the value can't be found)
- `.sort()` *modify* the list to sort it ascendingly
- `.reverse()` *modify* the list to put it in reverse order
- `.count(<value>)` returns the number of occurence of a value in the list

```python
>>> l = [1,2,3]
>>> l.append(4)
>>> print(l)
[1, 2, 3, 4]
>>> l.pop()
4
>>> print(l)
[1, 2, 3]
>>> l.remove(1)
>>> print(l)
[2, 3]
>>> l.insert(0, 1)
>>> print(l)
[1, 2, 3]
>>> l.index(2)
1
>>> l + [0]
>>> print(l)
[1, 2, 3, 0]
>>> l.reverse()
>>> l
[0, 3, 2, 1]
>>> l.count(1)
1 # there is 1 occurence of the value `1`
>>> l.sort()
>>> l
[0, 1, 2, 3]
```

### `list` built-in function

the `list` function converts an object to a list.

```python
>>> s = "hello"
>>> type(s)
<class 'str'>
>>> l = list(s)
>>> l
['o', 'k']
```

### `in` keyword

The in keyword has two purposes:
1. check if a value is present in a `sequence` (list, range, string etc.).
2. iterate through a sequence in a `for` loop

```python
>>> l = [1, 2, 3]
# checking the presence of a value
>>> 3 in l
True
>>> 55 in l
False
# iterating
>>> for elem in l:
...     print(elem)
...
1
2
3
```

### `len` built-in function

the `len` function returns the length of a `sequence`

```python
>>> l = [1,2,3,4]
>>> len(l)
4
```

### `del` keyword

use the `del` keyword to delete an element with its index

```python
>>> l = [1, 2 ,3]
>>> del l[1]
>>> print(l)
[1, 3]
>>> del l[49] # deleting an index that does not exist for this list raises an Exception
IndexError: list assignment index out of range
```

### common built-in functions used with lists

- `max(<list>)` returns the maximum value in a list
- `min(<list>)` returns the minimum value in a list

```python
>>> l = [1,2,3]
>>> min(l)
1
>>> max(l)
3
```

## strings (again!)

a `string` can be seen as a `list` of characters (because it is a `sequence`) ! You can access each of its characters via their index. You can also loop on it.

```python
>>> s = "hello"
>>> print(s[0])
"h"
>>> for letter in s:
...     print(letter)
...
"h"
"e"
"l"
"l"
"o"
```

Two or more string _literals_ (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

```python
>>> 'Py' 'thon'
'Python'
```

This feature is particularly useful when you want to break long strings:

```python
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```

### common string methods

- `<string>.join(<list>)` creates a new string with each element of `<list>`, separated by `<string>`
- `.upper()` returns the string entirely in ALL CAPS
- `.lower()` returns the string entirely in lowercase
- `.capitalize()` returns the string with a Uppercase at the beginning
- `.split(<separator>)` splits the string using the separator and returns a list of string
- `.startswith(<value>)` checks if the string starts with the value
- `.endswith(<value>)` checks if the string ends with the value
- `.replace(<old>, <new>, [count=-1])` returns a copy of the string where the `<old>` part is replaced by the `<new>` part. By default, `count` is at `-1` meaning that all occurences of `<old>` will be replaced. If you want only the first occurence of `old` to be replaced, then set `count` as `1`
- `.find(<sub>)` returns the first index where the `sub` string is found

```python
>>> s = ".".join(["hello", "world"])
>>> s
"hello.world"
>>> s = "hello"
>>> s.upper()
"HELLO"
>>> s.lower()
"hello"
>>> s.capitalize()
"Hello"
>>> sp = "127.0.0.1"
>>> sp.split(".")
['127', '0', '0', '1']
>>> sp.startswith("127")
True
>>> sp.endswith("8")
False
>>> sp.find('0')
# string 127.0.0.1
# index  012345678
4 # index 4 ;)
```

### ellipsis

`...` in python is called `ellipsis`. It is a string literal.

One of its main purpose is placeholding (just like `pass`). For example if you declare a class without attribute (like a custome Exception for example), you can use the `ellipsis` as a placeholder.

```python
class CustomException:
    ...

class CustomeException:
    pass
```

But the `no-op` instruction `pass` is prefered and much older than the `ellipsis` so use `pass` instead :)

## tuples

`Tuples` are like `lists` but are immutable and are written with parenthesis.

```python
>>> t = (1, 2, 3)
>>> type(t)
<class 'tuple'>
# if you want to create a tuple of one element, you need to add a comma after the element
>>> t = (1,)
>>> len(t)
1
```

### unpacking

a `sequence` can be unpacked into variables.

Unpacking is powerful tool !

```python
>>> a, b, c = (1, 2, 3)
>>> print(a, b ,c)
1 2 3
# extended unpacking is defined by an asterisk
>>> a, *b, c = (1, 2, 3, 4)
>>> print(a, b, c)
1 [2, 3] 4
# you can also use unpacking to init some variables
d, e, f = 4, 5, 6
# a neat trick with unpacking is to swap variables (commonly used in math algorithm implementation)
>>> d, e = 1, 2
>>> e, d = d, e
>>> print(d, e)
2 1
```

## dictionaries / dict

A `dict` is a key/value datastructure, created by placing a sequence of elements within curly braces `{}`.

Keys of a `dict` needs to be immutable (int, float, string, tuple). But a `dict` is not immutable.

You can access an element using square brackets and the key. `[<key>]`

When the element is nested, combined multiple square brackets.

To add or edit an element, also use square brackets + the `=` assign operator.

```python
>>> empty_dict = {}
>>> d = {"one": 1, "two": 2}
>>> d["one"]
1
>>> d["three"] = 3
>>> print(d)
{'one': 1, 'two': 2, 'three': 3}
>>> d["four"] = ["rowenta", "bosch"]
>>> print(d["four"][0])
"rowenta"
>>> d["unknown"] # accessing an unknown key raises a KeyError exception
KeyError: 'ok'
# in most cases, you should use the `.get()` method rather accessing directly via []
```

### common dict methods

- `.keys()` returns a list of all the keys
- `.values()` returns a list of all the values
- `.items()` returns a list of tuples which are the couples <key>, <value>
- `.get(<key>, [default])` returns an element for a key, if the key does not exist, `None` is returned, except if a `default` is provided
- `.setdefault(<key>, <value>)` set a default value for a key if it's not already set
- `.update({"four":4})` merges two dictionaries

```python
>>> d = {"one": 1, "two": 2}
>>> d.keys()
dict_keys(['one', 'two'])
>>> d.values()
dict_values([1, 2])
>>> d.items()
dict_items([('one', 1), ('two', 2)])
>>> d.get("one")
1
>>> d.get("three")
None
>>> d.get("three", "default data 3")
"default data 3"
>>> d.setdefault("three", 3) # "three" key is not configured, so the default value is set
>>> d["three"]
3
>>> d.setdefault("three", "default 3") # "three" key is already configured
>>> d["three"]
3
>>> d.update({"four":4})
>>> d
{'one': 1, 'two': 2, 'three': 3, 'four': 4}
```

### `in` keyword

the `in` keyword can be used to check if an element is a key of a dict.

```python
>>> d = {"one": 1, "two": 2}
>>> "one" in d # is equivalent to "one" in d.keys()
True
```

### `del` keyword

you can use the `del` keyword to delete a key in a dict.

trying to delete a key that doesn't exist raises a `KeyError` exception.

```python
>>> d = {"one": 1, "two": 2}
>>> del d["one"]
>>> d
{'two': 2}
>>> del d["one"]
KeyError: 'one'
```

### unpacking (again!)

Since python 3.5, you can now unpack elements in a dict, resulting in a `merge` or an `addition` !

```python
>>> d = {'a': 1, **{'b': 2}} # addition because the key 'b' is not set
>>> print(d)
{'a': 1, 'b': 2}
>>> d = {'a': 1, **{'a': 2}} # merge because the key 'a' is already defined so its overwritten
>>> print(d)
{'a': 2}
```

## sets

a `set` is a collection of *unique* elements. You can add multiple times the same element, but there will be only one occurence of this element in the set.

a `set` can be instancied with the function `set` or with curly braces (like a dict) `{}`.

a `set` can contain only immutable elements (strings, tuples, ints...) (like the keys of a dict).

```python
>>> empty_set = set()
>>> s = {1,2,3,4}
>>> s.add(1) # here we try to add 1 to the set
>>> print(s)
{1, 2, 3, 4} # as we can see, 1 was already in the set so the addition didn't do anything
```

Like a mathematical `set`, we can do mathematical operations such as intersection `&`, union `|`, difference `-` ...

```python
>>> s1 = {1,2,3,4}
>>> s2 = {2,3}
>>> s1 & s2 # intersection
{2, 3}
>>> s3 = {5,6}
>>> s1 | s3 # union
{1, 2, 3, 4, 5, 6}
>>> s1 - s2 # difference
{1, 4}
```
### `in` keyword

the `in` keyword can be used to check if an element exists in a `set`, and to iterate.

```python
>>> s1 = {1,2,3,4}
>>> 1 in s1
True
>>> 5 in s1
False
>>> for i in s1: # iterating
...     print(i)
...
1
2
3
4
```

## pointers, pass-by-value, pass-by-reference

We **need** to talk about how python variables are passed between functions etc...

**Python is "pass-by-object-reference"**

This is equivalent to “object references are passed by value".

The variable is not the object.

Let's dig deeper. Take a look at the following examples and try to guess the answer :

```python
>>> a = [1,2,3]
>>> b = [1,2,3]
>>> a == b # ? True or False ?
True
# remember that the `==` operator check that both sides have the same *values*
>>> a is b # ? True of False ?
False
# remember, the `is` keywork check if both sides are the same *objects* (if they have the same address)
# we can verify this claim by using the `id` function
>>> id(a) ; id(b)
4419606336
4419608320
# we can see that `a` and `b` don't have the same address
```

now what about this example :

```python
>>> a = [1,2,3]
>>> b = a
>>> a == b # ? True or False ?
True
>>> a is b # ? True or False ?
True
>>> id(a) ; id(b)
4419606336
4419606336
```

but what if we want `b` to be a copy of `a` and not a `reference` to it ? ;-)

we can use the `.copy()` method (or use a trick with slicing)

```python
>>> a = [1,2,3]
>>> b = a.copy()
>>> a is b
False
>>> b = a[:] # remember, in slicing, the `[:]` is equal to [0 : len(<elem>)-1 : 1]
```

but be careful, with a "simple" `copy` like this, we don't clone the elements in the list, we just make new pointers to them.

if you modify the new list, elements in the old list will be affected too ! this is called a `shallow copy`.

```python
>>> a = [[1,2,3],[4,5,6],[7,8,9]]
>>> b = a.copy()
>>> b
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> b[0][0] = "RIP"
>>> a
[['RIP', 2, 3], [4, 5, 6], [7, 8, 9]]
>>> b
[['RIP', 2, 3], [4, 5, 6], [7, 8, 9]]
```

if we really want to clone the entire list, we must create a `deep copy` with the `copy` module and its function `deepcopy()` :

```python
>>> import copy
>>> a = [[1,2,3],[4,5,6],[7,8,9]]
>>> b = copy.deepcopy(a)
>>> b[0][0] = "RIP"
>>> a
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> b
[['RIP', 2, 3], [4, 5, 6], [7, 8, 9]]
# yay !
```

but what does it all mean ? well, you must remember that when you pass a `list` to a `function`, you pass the `address` of this list, so it can be modified by the `function`. And sometimes you don't want that.

Here's an example :

```python
def reassign(l):
  l = [0, 1]

>>> l = [1,2,3]
>>> reassign(l) # here we pass the `l` variable to the function `reassign`
# what's the value of `l` now ?
# 1: [0, 1]
# 2: [1,2,3]
>>> l
[1, 2, 3] # answer 2 !
# yes we pass the list `l` by reference, but we reassign the local variable to something else
```

the previous example can be confusing because the `local variable` of the `function` has the same name as the the other variable (`l`).

we can rewrite it for more clarity :

```python
def reassign(local_l):
  local_l = [0, 1]

>>> l = [1,2,3]
>>> reassign(l)
```

BUT when you don't know how python works, you can think that this list will not be modified simply because it doesn't have the same name (not true !)

so here's the final ~straw~ example :-)

```python
def do_smth(local_l):
  local_l.append(4)

>>> l = [1,2,3]
>>> do_smth(l) # here we pass the `l` variable to the function `do_smth`
>>> print(l)
# what's the value of `l` now ?
# answer 1. [1, 2, 3, 4]
# answer 2. [1, 2, 3]
[1, 2, 3, 4]
```
- you choosed answer 2, well done !
- answer 1, yikes ! please read this chapter again :) (or drop an email)

source :
- https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/

## `range` built-in function

`range` is a powerful function, which can be used in various ways :

- generate a sequence of numbers from 0 to `<stop>-1` with `range(<stop>)`
- generate a sequence of numbers from `<start>` to `<stop>` (with an optional `<step>`) with `range(<start>, <stop>, [step])`

```python
>>> list(range(0, 5)) # will generate a list of numbers from 0 to 4 (5-1)
[0, 1, 2, 3, 4]
>>> list(range(5, 10, 2)) # will generate a list of numbers from 5 to 9 (10-1) 2-by-2
[5, 7, 9]
```

(Want to see its source code ? <https://github.com/python/cpython/blob/5fcfdd87c9b5066a581d3ccb4b2fede938f343ec/Objects/rangeobject.c#L76>)

## conditions

TODO
If / elif / else
break
continue


## loops

TODO ok

For
    la clause else # equivalent to a `if no break`
    Si objet séquentiel
    Si vous utilisez les index, cest que vous le faites surement pas bien
    range function
    enumerate function
While

exercice : create a program which takes in input a number of lines, and print a pyramid.

```python
# example of a pyramid of 4 lines
   *
  ***
 *****
*******
```


### dict

loop over keys
```python
for key in d:
       print(key)
```

loop over key and value
```python
for k, v in d.items():
    print(f"{k} --> {v}")
```

cornercase avec cette façon de faire ?
On ne peut pas muter un dict lorsque l’on itère dessus

```python
d = {"ok": 0, "nok": -1}
for k in d:
    if k == "ok":
        del d[k]
```

préférer :

```python
d = {"ok": 0, "nok": -1}
for k in d.keys():
    if k == 'ok':
        del d[k]
```

## functions (again!)

### `*args` and `**kwargs`

When a final formal parameter of the form `**name` is present, it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form *name (described in the next subsection) which receives a tuple containing the positional arguments beyond the formal parameter list. (`*name` must occur before `**name`.) For example, if we define a function like this:

```python
def foo(bar, *args, **kwargs):
    print(bar)
    print("-" * 20)
    for arg in args:
        print(f"arg : {arg}")
    print("-" * 20)
    for k in kwargs:
        print(f"kwarg: {k} => {kwargs[k]}")
```

It could be called like this:

```python
foo("a", "b", "c", k1="v1", k2="v2")
```

and of course it would print:

```
a
--------------------
arg : b
arg : c
--------------------
kwarg: k1 => v1
kwarg: k2 => v2
```

### type annotation

Function annotations are completely optional metadata information about the types used by user-defined functions.

Annotations are stored in the **annotations** attribute of the function as a dictionary and have no effect on any other part of the function.

```python
def foo(bar: str) -> str:
    print(bar)
    return "ok"
```

## comprehension

TODO
dict `{k:k**2 for k in range(10)}`

```
[i for i in range(10)]
[i for i in range(1, 20) if i % 2 == 0]
L = []

```

## modules/packages/libraries

TODO

    __name__ == "__main__"

## file handling

TODO

## Bonnes pratiques

TODO

### PEP8

### Google styling guide

- [Google Python Styling Guide](https://google.github.io/styleguide/pyguide.html)

### Documentation

TODO
peut etre merge avec commentaires ? pour parler doctstring etc ?

### DRY

### YAGNI

# Advanced

## protocol

TODO

In Python a protocol is an informal interface. Protocols are either known as an accepted truth or defined in documentation and not strictly in code1. For example, any class that implements the `__container__()` special method is said to follow the "container protocol." While this is an accepted truth, there is no syntax in the Python language that declares a class as following a protocol. Python classes can also implement multiple protocols.

## decorators

TODO

## iterators

TODO

## context manager

TODO

## exceptions - try/except

Analogy : Imagine that you order something on the web, and during the delivery you're not at home. `Error handling` in this context means that the delivery company should be able to deliver your package another time/place so you can have it.

TODO

## generators

TODO

## OOP

TODO

## functional

TODO

## Design patterns

TODO

> a design pattern is a general repeatable solution to a commonly occurring problem in software design. A design pattern isn't a finished design that can be transformed directly into code. It is a description or template for how to solve a problem that can be used in many different situations.

- <https://python-patterns.guide/>
- <https://github.com/faif/python-patterns>

## Threading

TODO

GIL

## Testing

TODO

## env

TODO

## RESTE A FAIRE

affichage
    print
        signature d'une fonction
        help() function
        `__dir__` method
    fstring

conditions
    if /elif / else
    ==
    !=
    >
    >=
    <
    <=
    continue
        saute à l’itération suivante
    break
        stoppe la boucle

    exercice :
        jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
            de lundi a jeudi : travail
            vendredi : soon le w-e
            samedi dimanche : BBQ

boucle
    si vous utilisez des index, cest que vous le faites probablement pas bien
    for
        for i in range(len(colors)):
            print(colors[i])

        for i in range(len(colors)-1, -1, -1)
            print(colors[i])

        enumerate + for/else

            def find(seq, target):
                found = False
                for i, value in enumerate(seq):
                    if value == target:
                        found = True
                        break
                if not found:
                    return -1
                return i

            def find(seq, target):
                for i, value in enumerate(seq):
                    if value == seq:
                        break
                else:
                    return -1
                return i
        zip
            2 listes

        for n in range(2, 10):
            for x in range(2, n):
                if n % x == 0:
                    print(n, 'equals', x, '*', n//x)
                    break
            else:
                # loop fell through without finding a factor
                print(n, 'is a prime number')

    valeur sentinel

        from functools import partial
        from random import randint

        pull_trigger = partial(randint, 1, 6)

        print('Starting a game of Russian Roulette...')
        print('--------------------------------------')

        for i in iter(pull_trigger, 6): #iter prend en argument une fonction ne renvo
            print('I am still alive, selected', i)
        print('Oops, game over, I am dead! :(')

        #partial() est utilisé pour une application de fonction partielle
        qui "gèle" une portion des arguments et/ou mots-clés d'une fonction
        donnant un nouvel objet avec une signature simplifiée.

    while
    range
    iter

dir()
help() - how to use it + how does it work (docstrings)
sorted() - sorted(, key)

fonction (vs procedure)
    signature
    portée
        LGI
    anonyme
    DRY
    passage d'arguments
    renvoi de résultats
    arguments positionnels vs. arguments par mots clés
        twitter_search("@obama", False, 20, True)
        twitter_search("@obama", retweets=False, numtweets=20, popular=True)

tuples
    NamedTuples (subclass of tuple)
    unpacking :
        p = 'pommes', 30, 1
        produit, quantite, prix = p

dictionnaires
    fundamental
    relationships, linking, counting, grouping

    for k in d:
        print(k)

    cant mutate a dict while youre iterating over it

    for k in d.keys():
        if k.startswith('non'):
            del d[k]

    for k in d: #non
        print(f"{k} --> {d[k]}")

    for k, v in d.items():
        print(f"{k} --> {v}")

    colors = ["red", "green"]
    d = {}
    for color in colors:
        if color not in d: #raise an error but its a not so no problem
            d[color] = 0
        d[color] += 1

    d = {}
    for color in colors:
        d[color] = d.get(color, 0) + 1

    defaultdict # too advanded but it exists ;)

    grouping :
        d = {}
        for name in names:
            key = len(name)
            d.setdefault(key, []).append(name)

        d = defaultdict(list)
        for name in names:
            key = len(name)
            d[key].append(name)

    linking :
        collections.ChainMap

fichier
binaire
modules / package
    docstring

iterators

context manager
    with

    try: #wrong way to do it
        os.remove('somefile.tmp')
    except OSError:
        pass

    from contextlib import suppress
    with suppress(FileNotFoundError):
        os.remove('somefile.tmp')

    from contextlib import contextmanager

    @contextmanager
    def open_db(filename: str):
        try:
            con = sqlite3.connect(filename)
            yield con
        except sqlite3.DatabaseError as err:
            logger.error(err    )
        finally:
            con.close()

one liner : 1 ligne de code = 1 phrase en francais

bonnes pratiques
    pep8 (syntaxe)
    pep257
    pep20

python : everything is an object

decorateurs
try except
comprehension
generateurs
magic methods

DRY
YAGNI

classes
interfaces
conventions (snake case, globals in all-caps)
    "pythonic" code
    https://www.python.org/dev/peps/pep-0008/
    https://google.github.io/styleguide/pyguide.html


Voici quelques conseils pour vous aider à concevoir un script Python.
- Réfléchissez avec un papier, un crayon... et un cerveau (voire même plusieurs) ! Reformulez avec des mots en français (ou en anglais) les consignes qui vous ont été données ou le cahier des charges qui vous a été communiqué. Dessinez ou construisez des schémas si cela vous aide.
- Découpez en fonctions chaque élément de votre programme. Vous pourrez ainsi tester chaque élément indépendamment du reste. Pensez à écrire les docstrings en même temps que vous écrivez vos fonctions.
- Quand l’algorithme estc omplexe, commentez votre code pour expliquer votre raisonnement. Utiliser des fonctions(ou méthodes) encore plus petites peut aussi être une solution.
- Documentez-vous. L’algorithme dont vous avez besoin existe-t-il déjà dans un autre module ? Existe-t-il sous la forme de pseudo-code ? De quels outils mathématiques avez-vous besoin dans votre algorithme ?
- Si vous créez ou manipulez une entité cohérente avec des propriétés propres, essayez de construire une classe.
- Utilisez des noms de variables explicites, qui signifient quelquechose. En lisant votre code, on doit comprendre ce que vous faites. Choisir des noms de variables pertinents permet aussi de réduire les commentaires.
- Quand vous construisez une structure de données complexe (par exemple une liste de dictionnaires contenant d’autres objets), documentez et illustrez l’organisation de cette structure de données sur un exemple simple.
- Testez toujours votre code sur un jeu de données simple pour pouvoir comprendre rapidement ce qui se passe. Par exemple, une séquence de 1000 bases est plus facile à gérer que le génome humain ! Cela vous permettra également de retrouver plus facilement une erreur lorsque votre programme ne fait pas ce que vous souhaitez.
- Lorsque votre programme « plante », lisez le message d’erreur. Python tente de vous expliquer ce qui ne va pas. Le numéro de la ligne qui pose problème est aussi indiqué.
- Discutez avec des gens. Faites tester votre programme par d’autres. Les instructions d’utilisation sont-elles claires ?
- Si vous distribuez votre code :
- Rédigez une documentation claire.
- Testez votre programme (jetez un œil aux tests unitaires 10).
- Précisez une licence d’utilisation. Voir par exemple le site Choose an open source license