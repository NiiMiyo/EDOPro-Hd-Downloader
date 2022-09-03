from typing import Callable, NamedTuple, Optional


class DownloadCard(NamedTuple):
    card_id: int
    artwork: bool
    force: bool = False


CommandReturn = Optional[list[DownloadCard]]
CommandAction = Callable[[str], CommandReturn]


class DownloaderCommand(NamedTuple):
    name: str
    help_text: str
    action: CommandAction
