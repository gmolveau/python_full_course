#!/usr/bin/env python3
import argparse
import random


def convert(text: str) -> str:
    text = text.lower()
    converted_text = ""
    for letter in text:
        if random.random() < 0.5:
            letter = letter.upper()
            converted_text += letter
        else:
            converted_text += letter
    return converted_text


def parse_args():
    parser = argparse.ArgumentParser("spongebob meme generator")
    parser.add_argument(
        "-t", "--text", required=True, dest="sentence", help="text to be converted"
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    converted_sentence = convert(args.sentence)
    print(converted_sentence)


if __name__ == "__main__":
    main()
