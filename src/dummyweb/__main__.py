import click

from .__about__ import __version__
from .models import db


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__)
def main():
    """Perform dummyweb related operations."""


@main.command("create-db")
def create_db():
    """Create Dummyweb database."""
    click.echo("Create database...")
    db.create_all()


if __name__ == "__main__":
    main()
