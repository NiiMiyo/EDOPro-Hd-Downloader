from commands.cmd_allcards import CMD_ALL_CARDS
from commands.cmd_allfields import CMD_ALL_FIELDS
from commands.cmd_exit import CMD_EXIT
from commands.typing import CommandReturn, DownloaderCommand


def __cmd_help_action(_: str) -> CommandReturn:
    cmd_column_len = 0
    for cmd in COMMANDS:
        n = len(cmd.name)
        if n > cmd_column_len:
            cmd_column_len = n

    output = "\n".join([
        f"/{cmd.name.ljust(cmd_column_len)} - {cmd.help_text}"
        for cmd in COMMANDS
    ])

    print(output)
    return []


CMD_HELP = DownloaderCommand(
    name="help",
    help_text="see this text",
    action=__cmd_help_action
)

# here due to circular import (/help needs to import this and this needs /help)
COMMANDS: list[DownloaderCommand] = [
    CMD_ALL_CARDS, CMD_ALL_FIELDS, CMD_EXIT, CMD_HELP
]
