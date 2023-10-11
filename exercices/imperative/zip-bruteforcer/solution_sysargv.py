import logging
import os
import sys
import zipfile
from collections import namedtuple


class UnkownFlagException(Exception):
    pass


class MissingArgumentException(Exception):
    pass


class FileNotFoundException(Exception):
    pass


Args = namedtuple("Args", ["input_filepath", "verbose_mode", "passwords_filepath"])


def configure_logging(loglevel=logging.INFO):
    logging.basicConfig(level=loglevel)


def check_file_exists(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundException(f"{filepath} does not exist")


def parse_args():
    # Initialize variables for file paths and verbose mode
    input_filepath = None
    verbose_mode = False
    passwords_filepath = None

    # Parse command-line arguments
    args = sys.argv[1:]

    while args:
        arg = args.pop(0)
        if arg in ("-f", "--file"):
            # Check if there are more arguments after the flag
            if not args:
                print("Error: Missing input file path.")
                raise MissingArgumentException
            input_filepath = args.pop(0)
            check_file_exists(input_filepath)
        elif arg in ("-v", "--verbose"):
            verbose_mode = logging.DEBUG
        elif arg in ("-w", "--words"):
            # Check if there are more arguments after the flag
            if not args:
                print("Error: Missing passwords file path.")
                raise MissingArgumentException
            passwords_filepath = args.pop(0)
            check_file_exists(passwords_filepath)
        else:
            raise UnkownFlagException

    return Args(input_filepath, verbose_mode, passwords_filepath)


def main(protected_zip_path, wordlist_path):
    with zipfile.ZipFile(protected_zip_path) as z:
        with open(wordlist_path) as wordlist_file:
            for password_line in wordlist_file:
                password = password_line.strip()
                try:
                    z.extractall(pwd=password.encode("utf-8"))
                    logging.info(f"password found: {password}")
                    break
                except zipfile.BadZipFile as e:
                    logging.error(f"the zip file is invalid - {e}")
                    raise e
                except RuntimeError as e:
                    logging.debug(f"bad password: {password}")


if __name__ == "__main__":
    args = parse_args()
    configure_logging(args.verbose_mode)
    main(args.input_filepath, args.passwords_filepath)
