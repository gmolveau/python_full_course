import argparse
import sys


class Make:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Pretends to be git")
        subparsers = parser.add_subparsers(dest="command")
        parser_db = subparsers.add_parser(
            "db",
            description="db command",
            help="manage the db",
        )
        args = parser.parse_args()
        if not hasattr(self, args.command):
            exit(1)
        getattr(self, args.command)()

    def db(self):
        print("db command run")


if __name__ == "__main__":
    Make()
