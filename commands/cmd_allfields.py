from command_handler import CommandHandler
from commands.typing import DownloadCard, DownloaderCommand, CommandReturn
from apiaccess import get_all_fields


def __cmd_all_fields_action(_: str) -> CommandReturn:
    return [
        DownloadCard(c, True)
        for c in get_all_fields()
    ]


CommandHandler.add_command(DownloaderCommand(
    name="allfields",
    help_text="downloads all fields artworks",
    action=__cmd_all_fields_action
))
