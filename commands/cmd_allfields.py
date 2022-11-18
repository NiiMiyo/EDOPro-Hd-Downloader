from commands.typing import DownloadCard, DownloaderCommand, CommandReturn
from web_access.ygoprodeck_api import get_all_fields

def __cmd_all_fields_action(_: str) -> CommandReturn:
    return [
        DownloadCard(c, True)
        for c in get_all_fields()
    ]


COMMAND_ALLFIELDS = DownloaderCommand(
    name="allfields",
    help_text="downloads all fields artworks",
    action=__cmd_all_fields_action
)