from commands.typing import CommandReturn, DownloaderCommand

def __cmd_exit_action(_: str) -> CommandReturn:
    print("Bye bye <3")
    exit(0)

CMD_EXIT = DownloaderCommand(
    name="exit",
    help_text="closes the program",
    action=__cmd_exit_action
)
