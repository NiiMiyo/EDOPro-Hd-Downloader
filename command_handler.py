from typing import Optional
from commands.typing import DownloaderCommand
from commands.utils import command_matches


class CommandHandler:
    commands: list[DownloaderCommand] = list()

    @staticmethod
    def get_command(user_input: str) -> Optional[DownloaderCommand]:
        if not user_input:  # If empty string or None
            return None

        for cmd in CommandHandler.commands:
            if command_matches(user_input, cmd):
                return cmd
        return None

    @staticmethod
    def add_command(command: DownloaderCommand):
        CommandHandler.commands.append(command)
        CommandHandler.commands.sort(key=lambda cmd: cmd.name)
