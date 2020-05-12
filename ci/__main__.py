import click
import subprocess
from subprocess import check_call

DEFAULT_PYTHON_VERSION = "3.6"
PYTHON_VERSIONS = ["3.6"]

CORE_DEPS = []

DOCS_DEPS = ["sphinx==1.8.5-6"]

DEV_DEPS = []

PIP_DEPS = []


@click.group()
def cli():
    pass


python_version_option = click.option(
    "--python-version",
    default=DEFAULT_PYTHON_VERSION,
    type=click.Choice(PYTHON_VERSIONS),
    show_default=True,
    help="Python version for the environment",
)


@cli.command(name="build-env", help="Creates the execution environment")
@python_version_option
def build_env(python_version):
    env_name = get_env_name(python_version)
    check_call(
        [
            "edm",
            "environments",
            "remove",
            "--purge",
            "--force",
            "--yes",
            env_name,
        ]
    )
    check_call(
        [
            "edm",
            "environments",
            "create",
            "--version",
            python_version,
            env_name,
        ]
    )

    check_call(
        ["edm", "install", "-e", env_name, "--yes"]
        + CORE_DEPS
        + DEV_DEPS
        + DOCS_DEPS
    )

    if len(PIP_DEPS):
        check_call(
            ["edm", "run", "-e", env_name, "--", "pip", "install"] + PIP_DEPS
        )


@cli.command(help="Builds the documentation")
@python_version_option
def docs(python_version):

    env_name = get_env_name(python_version)

    click.echo("Generating HTML")
    returncode = edm_run(env_name, ["make", "html"], cwd="docs")
    if returncode:
        raise click.ClickException(
            "There were errors while building HTML documentation."
        )


def get_env_name(python_version):
    return "force-py{}".format(remove_dot(python_version))


def remove_dot(python_version):
    return "".join(python_version.split("."))


def edm_run(env_name, cmd, cwd=None):
    return subprocess.call(["edm", "run", "-e", env_name, "--"] + cmd, cwd=cwd)


if __name__ == "__main__":
    cli()
