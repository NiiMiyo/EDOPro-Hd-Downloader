from commands.typing import DownloaderCommand
from commands.cmd_allcards import CMD_ALL_CARDS
from commands.cmd_allfields import CMD_ALL_FIELDS
from commands.cmd_help import CMD_HELP


COMMANDS: list[DownloaderCommand] = [
    CMD_ALL_CARDS, CMD_ALL_FIELDS, CMD_HELP
]
