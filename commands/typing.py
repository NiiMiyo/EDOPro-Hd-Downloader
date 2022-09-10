from typing import Callable, NamedTuple, Optional


class DownloadCard(NamedTuple):
    """Represents a card to be downloaded"""

    card_id: int
    artwork: bool
    force: bool = False


CommandReturn = Optional[list[DownloadCard]]
"""Type a `CommandAction` should return"""

CommandAction = Callable[[str], CommandReturn]
"""Type a `DownloaderCommand.action` should be.

Should only return `None` in case the command fails. If the command does not
download cards, return an empty list.
"""


class DownloaderCommand(NamedTuple):
    name: str
    """The name of the command, should be unique"""

    help_text: str
    """Text the command shows on `/help`"""

    action: CommandAction
    """Function that defines command execution"""

    shown_name: Optional[str] = None
    """Name that will be shown on `/help`. If it's `None` then shows `name`"""

    def match_string(self) -> str:
        """Returns `/command.name`"""
        return f"/{self.name}"

    def get_shown_name(self) -> str:
        """Returns `command.shown_name` if it's not None. Otherwise returns
        `command.name`
        """

        if self.shown_name is None:
            return self.name
        else:
            return self.shown_name
