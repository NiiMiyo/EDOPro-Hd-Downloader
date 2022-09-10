from command_handler import CommandHandler
from commands.typing import CommandReturn
from deckread import get_deck

def handle_input(user_input: str) -> CommandReturn:
    """Handles an user input and returns a `CommandReturn` according to the
    matching command or deck with same name.

    Returns `None` if couldn't find what do download
    """

    command = CommandHandler.find_command(user_input)
    if command is None:
        return get_deck(user_input)
    else:
        return command.action(user_input)
