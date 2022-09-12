import click


def positive_int(ctx, param, value):
    if value < 0:
        raise click.BadParameter("Should be a positive integer")
    return value


@click.group()
def root():
    pass


@root.group()
def cmd():
    pass


@cmd.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", required=True, help="The person to greet.")
@click.argument("n", type=int, default=1, callback=positive_int)
def hello(count, name, n):
    """Simple program that greets NAME for a total of COUNT times."""
    print(f"{n=}")
    for x in range(count):
        click.echo(f"Hello {name}!")


if __name__ == "__main__":
    root()
