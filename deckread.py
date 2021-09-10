from os.path import exists as __exists, join as __join

deck_folder_path = "./deck/"


def __filter_card_id(cards: list[str]):
    """Filters an list with card ids to remove
    repeating ones and non-ids"""

    ids = list()
    for c in cards:
        try:
            int(c)
        except ValueError:
             continue
        else:
            if c not in ids:
                ids.append(c)
    return ids


def get_deck(deck_name: str):
    """Reads a deck file and returns the
    ids of the cards in it"""

    deck_path = __join(deck_folder_path, f"{deck_name}.ydk")
    deck_exists = __exists(deck_path)
    if not deck_exists:
        return None
    deck = open(deck_path, mode="r", encoding="utf8")
    cards = __filter_card_id([l.strip() for l in deck.readlines()])
    return cards
