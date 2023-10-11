# Command Line Interface (cli)

## Notes

- positional args
    - optional = `[arg]`
    - required = `<arg>`

```bash
$ curl -h
Usage: curl [options...] <url>
```

- prefer flags (`tool --url="http://"`) over args (`tool <url>`) when building complex cli
- always show something to the user, in addition to the error code

```bash
$ tool login
Successfully logged in !
$ echo $?
0
```

- show progress visually if possible (progress bar if downloading)
- if a command has a side effect, provide a `--dry-run` option
- write to stdout for useful information (and for other programs), stderr for warnings and errors
- use error return codes (not just 0 and 1/-1)
- use trackable, human-readable and actionable errors

```bash
# don't do this
$ tool do_something
something went wrong lol
# do this
$ tool do_something
[ERR34] your token has expired, please reactivate it here > http://...
```

- avoid interactivity, or make it possible to disable it (think about scripting and continuous integration pipelines without user interaction)

- keep security in mind (avoid asking for password as a flag or arg for example)

```bash
# example of docker
$ docker login --username="john" --password="hunter2"
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
```

- commonly used args, be creative, but not for these ones

```
-? | -h --help
-v --verbose
-V --version
```

- output option : nowadays plaintext is not always wanted by the users, if you can, please provide a `--output-format` flag to choose from multiple type of output formats `json, yaml, toml, table`

- use the XDG Base Directory
    - where to put user data, cache data etc...
    - `$XDG_CONFIG_HOME` (defaults to `~/.config/`)
    - `$XDG_DATA_HOME` (defaults to `~/.local/share/`)
    - XDG Base Directory compliant applications should first attempt to read these values from the environment variables, or fallback to the default paths if these variables aren’t set in the runtime environment.
    - example of an issue on the symfony project : https://github.com/symfony/cli/issues/56

- be aware of `option-like arguments` like for example a negative integer. If you want to pass a negative integer as an argument, you need to use `-- ` before the arg. For example to enter `-4`, a user user must use `-- -4`. (https://click.palletsprojects.com/en/6.x/arguments/#option-like-arguments)

## Libs

- argparse (from the stdlib) : https://docs.python.org/3/library/argparse.html
- click : https://click.palletsprojects.com
- typer : <https://typer.tiangolo.com/> + <https://github.com/tiangolo/typer>

- interactive :
  - cmd2 : <https://cmd2.readthedocs.io/en/stable/>
  - pyinquierer : <https://github.com/CITGuru/PyInquirer#documentation>

## How to design a good cli

- https://clig.dev/

## Examples

### the classic `sysargv`

```python
# cli.py
import sys
print(f"This is the name of the script: {sys.argv[0]}")
print(f"Number of arguments: {len(sys.argv)}")
print(f"The arguments are: {str(sys.argv[1:])}")
```

To build a complex cli with it, you'll have to code a lot to parser the args, validate etc...

Please use argparse or click.

### argparse

- example of a parser, a subparser, and an inherited verbose mode


```python
import argparse

def main():
    parser = argparse.ArgumentParser(description='cli example with a boolean arg')
    parser.add_argument('-v', '--verbose', help='Common top-level parameter', action='store_true', required=False)
    subparsers = parser.add_subparsers()
    db_parser = subparsers.add_parser("db", parents=[parser], add_help=False, description="db command", help="manage the db")
    db_parser.add_argument('--url', help="database url")
    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()
```

### click

- a simple example :


```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', required=True, help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
```

- grouping commands


```python
import click

@click.group()
def root():
    pass

@root.group()
def cmd():
    pass

@cmd.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', required=True, help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    root()
```

## Resources

- https://en.wikipedia.org/wiki/Unix_philosophy
- https://danluu.com/cli-complexity/
- http://www.iitk.ac.in/esc101/05Aug/tutorial/essential/attributes/_posix.html
- https://www.ctrl.blog/entry/flatpak-steamcloud-xdg.html
- https://eng.localytics.com/exploring-cli-best-practices/