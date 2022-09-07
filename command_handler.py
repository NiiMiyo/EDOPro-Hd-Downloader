from typing import Optional
from commands.typing import DownloaderCommand
from commands.utils import command_matches


class CommandHandler:
    """Class to manage the use of commands"""

    commands: list[DownloaderCommand] = list()
    """List of all available commands. If you add a command you should put it
    here using `CommandHandler.add_command`."""

    @staticmethod
    def get_command(user_input: str) -> Optional[DownloaderCommand]:
        """Gets the `DownloaderCommand` that matches user_input. For example,
        `force` command for `"/force /allcards"` input.
        """

        if not user_input:  # If empty string or None
            return None

        for cmd in CommandHandler.commands:
            if command_matches(user_input, cmd):
                return cmd
        return None

    @staticmethod
    def add_command(command: DownloaderCommand):
        """Adds a DownloaderCommand to be available to use on user input"""

        CommandHandler.commands.append(command)
        CommandHandler.commands.sort(key=lambda cmd: cmd.name)
