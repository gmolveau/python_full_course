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
