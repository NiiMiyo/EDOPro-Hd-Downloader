from commands.typing import CommandReturn, DownloadCard, DownloaderCommand
from web_access.ygoprodeck_api import get_all_cards


def __cmd_all_cards_action(_: str) -> CommandReturn:
    return [
        DownloadCard(c, False)
        for c in get_all_cards()
    ]


COMMAND_ALLCARDS = DownloaderCommand(
    name="allcards",
    help_text="downloads all cards",
    action=__cmd_all_cards_action
)
