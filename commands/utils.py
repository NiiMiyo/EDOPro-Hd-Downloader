from commands.typing import DownloaderCommand


def command_matches(user_input: str, command: DownloaderCommand) -> bool:
    first_word = user_input.split(" ")[0]
    return first_word == ("/" + command.name)


def get_args(user_input: str) -> str:
    args = [
        a for a in user_input.split(" ")
        if a
    ]

    return " ".join(args[1:])
