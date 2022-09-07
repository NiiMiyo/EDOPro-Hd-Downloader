from commands.typing import CommandReturn
from commands.utils import command_matches
from commands.cmd_help import COMMANDS
from deckread import get_deck

def handle_input(user_input: str) -> CommandReturn:
    """Handles an user input and returns a CommandReturn according to the
    matching command or deck with same name.

    Returns None if couldn't find what do download"""

    for cmd in COMMANDS:
        if command_matches(user_input, cmd):
            return cmd.action(user_input)

    return get_deck(user_input)
