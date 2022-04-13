from os.path import exists
from time import sleep
from traceback import format_exc as __format_exc
from typing import Optional

from apiaccess import get_all_cards, get_all_fields
from deckread import get_deck
from downloader import download_image
from tracker import (already_downloaded, card_cache_path, field_cache_path,
                     mark_as_downloaded)

# String that appears at user input
input_string = "Insert deck name (without .ydk) or command: "


# Creates tracker files if they do not exist and introduces the program
def initialize():
    global card_cache_path, field_cache_path
    for i in (card_cache_path, field_cache_path):
        if not exists(i):
            open(i, "w+").close()

    intro = [
        "EDOPro HD Downloader",
        "Created by Nii Miyo",
        "Type \"/help\" for help"
    ]
    print("\n".join(intro))


# Handles what to do with user input
def handle_input(_input: str) -> tuple[Optional[list[int]], bool]:
    """Should return a tuple which the first element is a list with cards to
    download and the second is a boolean indicating if should download only
    the artwork at fields folder"""

    # Downloads all cards images
    if _input == "/allcards":
        return get_all_cards(), False

    # Downloads all field spell cards artworks
    elif _input == "/allfields":
        return get_all_fields(), True

    # Help command
    elif _input == "/help":
        print("Press Ctrl+C while downloading to force-stop the program")
        print("Available commands:")
        print("/allcards  - downloads all cards")
        print("/allfields - downloads all fields artworks")
        print("/exit      - closes the program")
        print("/help      - see this text")

    # Closes the program
    elif _input == "/exit":
        print("Bye bye <3")
        exit(0)

    # Since none of the commands where triggered, searchs for a deck
    # which name equals input
    else:
        return get_deck(_input), False

    # Default return for non-download commands
    return list(), False


# Handles if a card should be downloaded
def to_download(card_id: int, is_artwork: bool = False):
    if not already_downloaded(card_id, is_artwork):
        download_image(card_id, is_artwork)
        mark_as_downloaded(card_id, is_artwork)
        sleep(.1)


def main():
    initialize()

    try:
        while True:
            user_input = input(input_string)
            (cards, is_artwork) = handle_input(user_input)

            # If found what to download
            if cards is not None:
                total_cards = len(cards)

                # For each card, download
                for i in range(total_cards):
                    c = cards[i]
                    to_download(c, is_artwork)

                    # Prints progress
                    print(
                        f"Downloaded {i+1}/{total_cards} -",
                        f"{(((i+1)/total_cards) * 100):.2f}" + "%",
                        end="\r")

                # Help command had 2 newlines at end
                if total_cards > 0:
                    print()

            # If couldn't find what to download
            else:
                print("Deck or command not found.")
            print()

    # In case of interrupting the program with Ctrl+C
    except KeyboardInterrupt:
        print("\n\nForcing program interruption...")

    # In case of a not expected exception
    except Exception:
        print(__format_exc())
        exit()


if __name__ == "__main__":
    main()
