import getpass

import click
import sqlalchemy

from sqlalchemy import func

from .__about__ import __version__
from .models import db, User


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__)
def main():
    """Perform dummyweb related operations."""


@main.command("create-db")
def create_db():
    """Create Dummyweb database."""
    click.echo("Create database...")
    db.create_all()


@main.command("reset-pwd")
@click.argument("tagname")
def reset_pwd(tagname):
    """Reset some account password in database and account directory."""
    try:
        user = User.query.filter(User.username == func.upper(tagname)).one()
    except sqlalchemy.orm.exc.NoResultFound:
        click.secho(f"There is no user with tagname '{tagname}'.", fg="red",
                    err=True)
    else:

        attempts = 0

        while attempts < 3:
            password = getpass.getpass(
                f"Enter new password for user {tagname}: ")
            password_confirm = getpass.getpass("Confirm: ")

            if password != password_confirm:
                click.secho("Passwords do not match.", fg="red", err=True)
                attempts += 1
                continue

            user.set_password(password)

            # this works even if the account already exists
            user.create_directory()

            click.secho(f"Password succesfully updated for user {tagname}!",
                        fg="green")
            break
        else:
            click.secho(f"Too many attempts. Exiting.", fg="red", err=True)


if __name__ == "__main__":
    main()
