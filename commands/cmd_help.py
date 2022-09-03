from commands.typing import CommandReturn, DownloaderCommand
from commands.utils import COMMANDS

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
    return None

CMD_HELP = DownloaderCommand(
    name="help",
    help_text="see this text",
    action=__cmd_help_action
)
