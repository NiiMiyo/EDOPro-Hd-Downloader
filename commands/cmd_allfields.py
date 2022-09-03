from commands.typing import DownloadCard, DownloaderCommand, CommandReturn
from apiaccess import get_all_fields


def __cmd_all_fields_action(_: str) -> CommandReturn:
    return [
        DownloadCard(c, True)
        for c in get_all_fields()
    ]

CMD_ALL_FIELDS = DownloaderCommand(
    name="allfields",
    help_text="downloads all fields artworks",
    action=__cmd_all_fields_action
)
