def print_nouns(nouns: list[str]) -> None:
    for index, noun in enumerate(nouns):
        print(f"{index+1} {noun}")


print_nouns(["greg", "paul", "alexia"])
