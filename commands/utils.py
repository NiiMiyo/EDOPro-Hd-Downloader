from commands.typing import DownloaderCommand


def command_matches(user_input: str, command: DownloaderCommand) -> bool:
    first_word = user_input.split(" ")[0]
    return first_word == ("/" + command.name)
