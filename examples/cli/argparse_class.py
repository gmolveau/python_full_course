# source = https://chase-seibert.github.io/blog/2014/03/21/python-multilevel-argparse.html
# archive = https://web.archive.org/web/20220206210318/https://chase-seibert.github.io/blog/2014/03/21/python-multilevel-argparse.html
import argparse
import sys


class FakeGit:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Pretends to be git",
            usage="""git <command> [<args>]

The most commonly used git commands are:
   commit     Record changes to the repository
   fetch      Download objects and refs from another repository
""",
        )
        parser.add_argument("command", help="Subcommand to run")
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print("Unrecognized command")
            parser.print_help()
            sys.exit(1)
        getattr(self, args.command)() # dispatch pattern

    def commit(self):
        parser = argparse.ArgumentParser(description="Record changes to the repository")
        parser.add_argument("--amend", action="store_true")
        args = parser.parse_args(sys.argv[2:])
        print(f"Running git commit, amend={args.amend}")

    def fetch(self):
        parser = argparse.ArgumentParser(
            description="Download objects and refs from another repository"
        )
        parser.add_argument("repository")
        args = parser.parse_args(sys.argv[2:])
        print(f"Running git fetch, repository={args.repository}")


if __name__ == "__main__":
    FakeGit()
