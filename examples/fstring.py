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
print(f"{face!a}")  # == convert to ascii
print(f"{face!r}")  # == repr(face)
