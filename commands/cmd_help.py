from commands.cmd_allcards import CMD_ALL_CARDS
from commands.cmd_allfields import CMD_ALL_FIELDS
from commands.cmd_exit import CMD_EXIT
from commands.cmd_force import CMD_FORCE
from commands.typing import CommandReturn, DownloaderCommand


def __cmd_help_action(_: str) -> CommandReturn:
    cmd_column_len = 0
    lines: list[tuple[str, str]] = list()

    for cmd in COMMANDS:
        sn = cmd.get_shown_name()

        lines.append((sn, cmd.help_text))
        cmd_column_len = max(cmd_column_len, len(sn))


    print("\n".join(
        f"/{sn.ljust(cmd_column_len)} - {ht}"
        for sn, ht in lines
    ))

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
