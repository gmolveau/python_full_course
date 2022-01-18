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
