import argparse


def db():
    print("db command run")


def main():
    parser = argparse.ArgumentParser(description="autocompletion helper script")
    subparsers = parser.add_subparsers(dest="command")
    db_parser = subparsers.add_parser(
        "db",
        description="db command",
        help="manage the db",
    )
    db_parser.add_argument("--url", help="database url")
    args = parser.parse_args()
    commands = {
        "db": db,
    }
    commands[args.command]()


if __name__ == "__main__":
    main()
