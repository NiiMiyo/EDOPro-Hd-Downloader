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
    shown_name: Optional[str] = None

    def get_shown_name(self) -> str:
        if self.shown_name is None:
            return self.name
        else:
            return self.shown_name
