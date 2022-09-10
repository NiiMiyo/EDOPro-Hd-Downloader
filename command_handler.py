from typing import Optional
from commands.typing import DownloaderCommand
from commands.utils import get_first_word


class CommandHandler:
    """Class to manage the use of commands"""

    commands: dict[str, DownloaderCommand] = dict()
    """Dict of all available commands (maps command name to command).

    If you add a command you should put it here using
    `CommandHandler.add_command` and adding the import on `commands/setup.py`.
    """

    @staticmethod
    def find_command(user_input: str) -> Optional[DownloaderCommand]:
        """Gets the `DownloaderCommand` that matches user_input. For example,
        `force` command for `"/force /allcards"` input.
        """

        if not user_input:  # If empty string or None
            return None

        command_used = get_first_word(user_input)
        if command_used.startswith("/"):
            return CommandHandler.commands.get(command_used[1:])
        else:
            return None

    @staticmethod
    def add_command(command: DownloaderCommand):
        """Adds a DownloaderCommand to be available to use on user input"""

        CommandHandler.commands[command.name] = command
