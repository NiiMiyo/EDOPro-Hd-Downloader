from os.path import exists as __exists, join as __join

from commands.typing import CommandReturn, DownloadCard

deck_folder_path = "./deck/"


def __filter_card_id(cards: list[str]) -> list[int]:
    """Filters an list with card ids to remove
    repeating ones and non-ids"""

    ids: list[int] = list()
    for c in cards:
        try:
            c = int(c)
            if c not in ids:
                ids.append(int(c))
        except ValueError:
             continue
    return ids


def get_deck(deck_name: str) -> CommandReturn:
    """Reads a deck file and returns the
    ids of the cards in it"""

    deck_path = __join(deck_folder_path, f"{deck_name}.ydk")
    deck_exists = __exists(deck_path)
    if not deck_exists:
        return []
    deck = open(deck_path, mode="r", encoding="utf8")
    cards = __filter_card_id([l.strip() for l in deck.readlines()])
    return [
        DownloadCard(c, False)
        for c in cards
    ]
