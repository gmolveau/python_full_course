# fstring

`fstring` or `f-string` ? `¯\_(ツ)_/¯`

fstrings are available since `python 3.6`.

fstrings are used to format a string (before using/printing it).

fstrings are `evaluated`.

To create a `fstring` simply put the `f` letter before your string (your `double-quotes ""` if you prefer).

A `fstring` can contain a variable, an expression or a function.

We can also use the `:` operator to specify the formatting of the expression in the `{}`.

The formatting is linked to the type of the variable.

For example, `:.2f` means that we want this float variable printed with only 2 decimals.

`:%Y-%m-%d` will format a date to `year-month-day`

Finally if we want to use literal `curly braces {}` we need to double them.

Be careful when using `single-quote` or `double-quotes` to not use the same as the f-string. You can always use triple-quotes to avoid problems if you want.

Remember that a string in python automatically converts backslash caracter (for example `\n` will be a new line). If you want to keep the raw string, add a `r` after the `f` of the `fstring`.

Oh, and f-strings are faster than `.format` and `%` ! ;-)

## Example

```python
# literal curly braces
print(f"{{ok}}")

# variable
username = "test"
print(f"user is {username} - with braces > {{{username}}}")
prop = 1/3
print(f"{prop} - {prop:.3f}")

# expression
print(f"{2 * 2}")
print(f"user has a {'short' if len(username) < 5 else 'long'} username")

# function
def connect_status(username):
    return "connected"

log = f"user: {username} is {connect_status(username)}"
print(log)

# multiline print
print(
    f"1"
    f"2"
    f"3"
)

# using single and double quotes
print(f'''je fais ce'que'je "veux" ok''')

# raw f-string
print(f'this is a not a phase \nmom')
print(fr'this is a not a phase \n mom')

# cool trick using the = operator
print(f"{username=}")

# the ! operator
face = "hmmm 🤔"
print(f"{face}")
print(f"{face!a}") # == convert to ascii
print(f"{face!r}") # == repr(face)
```

### resources

https://youtu.be/BxUxX1Ku1EQ - Python f-strings can do more than you thought. f'{val=}', f'{val!r}', f'{dt:%Y-%m-%d}' - mCoding
https://he-arc.github.io/livre-python/fstrings/index.html
https://python.sdv.univ-paris-diderot.fr/03_affichage/#322-prise-en-main-des-f-strings
https://realpython.com/python-f-strings/#multiline-f-strings