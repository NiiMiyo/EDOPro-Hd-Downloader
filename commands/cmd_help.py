from commands.typing import CommandReturn, DownloaderCommand
from command_handler import CommandHandler


def __cmd_help_action(_: str) -> CommandReturn:
    cmd_column_len = 0
    lines: list[tuple[str, str]] = list()

    command_list = sorted(
        CommandHandler.commands.values(),
        key=lambda cmd: cmd.name
    )

    for cmd in command_list:
        sn = cmd.get_shown_name()

        lines.append((sn, cmd.help_text))
        cmd_column_len = max(cmd_column_len, len(sn))

    print("\n".join(
        f"/{sn.ljust(cmd_column_len)} - {ht}"
        for sn, ht in lines
    ))

    return []


COMMAND_HELP = DownloaderCommand(
    name="help",
    help_text="see this text",
    action=__cmd_help_action
)
