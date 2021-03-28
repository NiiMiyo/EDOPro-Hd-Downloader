card_cache_path = "./hd_cards_downloader_tracker"
field_cache_path = "./hd_fields_downloader_tracker"

def __get_cached(is_artwork: bool):
    """Reads tracker file and returns a list of ids
    that already were downloaded"""

    cache = field_cache_path if is_artwork else card_cache_path
    cache_file = open(cache, mode="r+", encoding="utf8")
    cards = [c.strip() for c in cache_file.readlines()]
    cache_file.close()
    return cards

def already_downloaded(card_id: int, is_artwork: bool = False):
    """Returns True if card with id 'card_id' was
    already downloaded"""

    cards_downloaded = __get_cached(is_artwork)
    return str(card_id) in cards_downloaded

def mark_as_downloaded(card_id: int, is_artwork: bool = False):
    """Opens tracker file to add an id to the downloaded list"""

    cache = card_cache_path if not is_artwork else field_cache_path

    cache_file = open(cache, mode="a+", encoding="utf8")
    cache_file.write(f"{card_id}\n")
    cache_file.close()
