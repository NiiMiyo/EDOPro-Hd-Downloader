from typing import Callable, NamedTuple


class DownloadCard(NamedTuple):
    card_id: int
    artwork: bool
    force: bool


CommandReturn = list[DownloadCard]
CommandAction = Callable[[str], CommandReturn]


class DownloaderCommand(NamedTuple):
    name: str
    help_text: str
    action: CommandAction
