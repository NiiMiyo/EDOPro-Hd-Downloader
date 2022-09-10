from commands.typing import CommandReturn, DownloaderCommand
from command_handler import CommandHandler


def __cmd_all(_: str) -> CommandReturn:
    allcards = CommandHandler.commands.get("allcards")
    allfields = CommandHandler.commands.get("allfields")

    return allcards.action(_) + allfields.action(_)  # type: ignore


CommandHandler.add_command(DownloaderCommand(
    name="all",
    help_text="downloads all cards images and all fields artworks",
    action=__cmd_all
))
