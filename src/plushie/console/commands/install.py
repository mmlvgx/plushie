""""""

from cleo.helpers import argument
from cleo.commands.command import Command

from typing import Final

from ...components import install


class Install(Command):
    """"""

    name = "install"
    description = "This is a Install command"

    arguments = [argument("package", "This is a Package argument")]

    def handle(self) -> None:
        """"""

        package: Final[str] = self.argument("package")

        owner, repo = package.split("/")

        component = install.Install(owner, repo)
        component.handle()
