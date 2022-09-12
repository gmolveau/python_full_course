import argparse


def main():
    parser = argparse.ArgumentParser(description="cli example with a boolean arg")
    parser.add_argument(
        "-v",
        "--verbose",
        help="Common top-level parameter",
        action="store_true",
        required=False,
    )
    subparsers = parser.add_subparsers(dest="command")
    db_parser = subparsers.add_parser(
        "db", description="db command", help="manage the db"
    )
    db_parser.add_argument("--url", help="database url")
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
