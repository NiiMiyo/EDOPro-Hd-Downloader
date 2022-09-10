def get_args(user_input: str) -> str:
    """Receives an user input and returns everything after the first
    space character replacing double spaces with single spaces
    """

    args = [
        a for a in user_input.split(" ")
        if a
    ]

    return " ".join(args[1:])


def get_first_word(user_input: str) -> str:
    """Receives an user input and returns everything before the first
    space character
    """

    if not user_input:
        return ""

    return user_input.split(" ")[0]
