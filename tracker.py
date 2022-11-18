from commands.typing import DownloadCard
from constants import CARD_CACHE_PATH, FIELD_CACHE_PATH


def __get_cached(is_artwork: bool):
    """Reads tracker file and returns a list of ids
    that already were downloaded"""

    cache = FIELD_CACHE_PATH if is_artwork else CARD_CACHE_PATH
    with open(cache, mode="r+", encoding="utf8") as cache_file:
        cards = [c.strip() for c in cache_file.readlines()]
    return cards

def already_downloaded(card: DownloadCard):
    """Returns True if card with id 'card.card_id' was
    already downloaded"""

    cards_downloaded = __get_cached(card.artwork)
    return str(card.card_id) in cards_downloaded

def mark_as_downloaded(card: DownloadCard):
    """Opens tracker file to add an id to the downloaded list"""

    cache = FIELD_CACHE_PATH if card.artwork else CARD_CACHE_PATH

    with open(cache, mode="a+", encoding="utf8") as cache_file:
        cache_file.write(f"{card.card_id}\n")
