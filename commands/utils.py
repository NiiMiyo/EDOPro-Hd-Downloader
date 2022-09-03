from commands.cmd_allcards import CMD_ALL_CARDS
from commands.typing import DownloaderCommand

COMMANDS: list[DownloaderCommand] = [
    CMD_ALL_CARDS
]


def command_matches(user_input: str, command: DownloaderCommand) -> bool:
    first_word = user_input.split(" ")[0]
    return first_word == ("/" + command.name)
