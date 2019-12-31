"""CLI for custom syntax."""

import click

import syntactic.app


@click.group()
def cli(**kwargs):
    """Commands for custom syntax."""


@cli.command()
@click.argument("file", type=click.File(mode="rb"))
def show(file):
    """Show the transformed code in a Python file."""
    click.echo(syntactic.app.decode(file.read())[0])


if __name__ == "__main__":
    cli()
