from os.path import exists
from time import sleep
from traceback import print_exc

from commands.cmd_help import COMMANDS
from commands.typing import CommandReturn, DownloadCard
from commands.utils import command_matches
from deckread import get_deck
from downloader import download_image
from tracker import (already_downloaded, card_cache_path, field_cache_path,
                     mark_as_downloaded)

# String that appears at user input
INPUT_STRING = "Insert deck name (without .ydk) or command: "

# Creates tracker files if they do not exist and introduces the program
def initialize():
    global card_cache_path, field_cache_path
    for i in card_cache_path, field_cache_path:
        if not exists(i):
            open(i, "w+").close()

    print("\n".join([
        "EDOPro HD Downloader",
        "Created by Nii Miyo",
        "Type \"/help\" for help"
    ]))


def handle_input(user_input: str) -> CommandReturn:
    """Handles an user input and returns a CommandReturn according to the
    matching command or deck with same name.

    Returns None if couldn't find what do download"""

    for cmd in COMMANDS:
        if command_matches(user_input, cmd):
            return cmd.action(user_input)

    return get_deck(user_input)


def to_download(card: DownloadCard):
    """Handles if a card should be downloaded and downloads it"""
    if (card.force) or (not already_downloaded(card)):
        download_image(card)
        mark_as_downloaded(card)
        sleep(.1)


def main():
    initialize()

    try:
        while True:
            cards = handle_input( input(INPUT_STRING) )

            # If couldn't find what to download
            if cards is None:
                print("Deck or command not found.")
                continue

            total_cards = len(cards)

            # For each card, download
            for index, card in enumerate(cards, 1):
                to_download(card)

                # Prints progress
                raw_progress = f"{index}/{total_cards}"
                percentage   = f"{((index * 100) / total_cards):.2f}%"
                print(f"Downloaded {raw_progress} - {percentage}", end="\r")

            print("\n")

    # In case of interrupting the program with Ctrl+C
    except KeyboardInterrupt: print("\n\nForcing program interruption...")

    # In case of a not expected exception
    except Exception: print_exc()


if __name__ == "__main__": main()
