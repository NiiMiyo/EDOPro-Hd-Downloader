from commands.typing import DownloaderCommand


def command_matches(user_input: str, command: DownloaderCommand) -> bool:
    """Tests if the `user_input` corresponds to the call of `command`

    For example, an input `"/allcards"` matches with `allcards` command.
    """

    if not user_input: return False

    first_word = user_input.split(" ")[0]
    return first_word == ("/" + command.name)


def get_args(user_input: str) -> str:
    """Receives an user input and returns everything after the first
    space character replacing double spaces with single spaces
    """

    args = [
        a for a in user_input.split(" ")
        if a
    ]

    return " ".join(args[1:])
