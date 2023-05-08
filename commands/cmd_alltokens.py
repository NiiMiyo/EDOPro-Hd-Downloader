from commands.typing import DownloadCard, DownloaderCommand, CommandReturn
from web_access.ygoprodeck_api import get_all_fields

def __cmd_all_tokens_action(_: str) -> CommandReturn:
    return [
        DownloadCard(c, True)
        for c in get_all_tokens()
    ]


COMMAND_ALLTOKENS = DownloaderCommand(
    name="alltokens",
    help_text="downloads all tokens",
    action=__cmd_all_tokens_action
)
