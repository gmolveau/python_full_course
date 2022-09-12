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
