import typer

from git_flow_wrapper import git_commands

app = typer.Typer()
new_app = typer.Typer()
app.add_typer(new_app, name="new")


@new_app.command("feature")
def new_feature(name: str):
    """
    Creates a new feature
    :param name: name
    :return:
    """
    feature = git_commands.create_new_feature(name)
    typer.echo(f"Feature `{feature}` created.")


@new_app.command("hotfix")
def new_hotfix(name: str):
    """
    Creates a new hotfix
    :param name: name
    :return:
    """
    hotfix = git_commands.create_new_hotfix(name)
    typer.echo(f"Hotfix `{hotfix}` created.")


@new_app.command("release")
def new_release(version: str):
    """
    Creates a new release
    :param version: x.x
    :return:
    """
    release = git_commands.create_new_release(version)
    typer.echo(f"Release `{release}` created.")


@app.command()
def publish():
    """Publishes the current branch"""
    branch = git_commands.publish_remote()
    typer.echo(f"Branch `{branch}` published.")


def main():
    app()
