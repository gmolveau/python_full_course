# password = 'a' or 'xiphihumeralis'

import argparse
import logging
import os
import zipfile


def configure_logging(loglevel):
    logging.basicConfig(level=loglevel)


def file_exists(filepath):
    if not os.path.isfile(filepath):
        raise argparse.ArgumentTypeError(f"{filepath} does not exist")
    return filepath


def parse_args():
    parser = argparse.ArgumentParser(description="zip bruteforcer")
    parser.add_argument(
        "-v",
        "--verbose",
        help="enable verbose mode",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.INFO,
    )
    parser.add_argument(
        "-f",
        "--file",
        dest="protected_zip_path",
        help="path of the protected zip file",
        type=file_exists,
        required=True,
    )
    parser.add_argument(
        "-w ",
        "--wordlist",
        dest="wordlist_path",
        help="path of the wordlist file",
        type=file_exists,
        required=True,
    )
    return parser.parse_args()


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
    configure_logging(args.loglevel)
    main(args.protected_zip_path, args.wordlist_path)
