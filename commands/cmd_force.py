from commands.typing import CommandReturn, DownloadCard, DownloaderCommand
from commands.utils import get_args
from input_handler import handle_input

def __cmd_force_action(user_input: str) -> CommandReturn:
    args = get_args(user_input)
    cards = handle_input(args)
    if cards is None:
        return None

    return [
        DownloadCard(c.card_id, c.artwork, True)
        for c in cards
    ]

COMMAND_FORCE = DownloaderCommand(
    name="force",
    shown_name="force <input>",
    help_text="executes <input> ignoring trackers (example: /force /allcards)",
    action=__cmd_force_action
)
