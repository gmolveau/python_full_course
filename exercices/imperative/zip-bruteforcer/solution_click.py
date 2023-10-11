# password = 'a' or 'xiphihumeralis'

import logging
import zipfile

import click


def configure_logging(loglevel):
    logging.basicConfig(level=loglevel)


@click.command(help="zip bruteforcer")
@click.option(
    "-v",
    "--verbose",
    help="Enable verbose mode",
    is_flag=True,
    default=False,
)
@click.option(
    "-f",
    "--file",
    "protected_zip_path",
    help="Path of the protected zip file",
    type=click.Path(exists=True),
    required=True,
)
@click.option(
    "-w",
    "--wordlist",
    "wordlist_path",
    help="Path of the wordlist file",
    type=click.Path(exists=True),
    required=True,
)
def main(verbose, protected_zip_path, wordlist_path):
    loglevel = logging.DEBUG if verbose else logging.INFO
    configure_logging(loglevel)
    main(protected_zip_path, wordlist_path)


def bruteforce_zip(protected_zip_path, wordlist_path):
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
    main()
