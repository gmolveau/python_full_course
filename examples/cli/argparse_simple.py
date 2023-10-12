import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="cli example with a boolean arg")
    parser.add_argument(
        "-v",
        "--verbose",
        help="Common top-level parameter",
        action="store_true",
        required=False,
    )
    parser.add_argument("--url", help="example url", required=True)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    print(args)


if __name__ == "__main__":
    main()
