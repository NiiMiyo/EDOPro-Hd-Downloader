from os.path import exists
from time import sleep
from traceback import print_exc
from commands.setup import setup_commands
from constants import DOWNLOADER_VERSION, INPUT_STRING, SETUP_CREATION_FILES

from input_handler import handle_input
from commands.typing import DownloadCard
from web_access.downloader import download_image
from tracker import (already_downloaded, mark_as_downloaded)


def initialize():
    """Creates tracker files if they do not exist, setups all commands and
    introduces the program
    """

    for f in SETUP_CREATION_FILES:
        if not exists(f):
            with open(f, "w+"):
                # I only need that the files exist
                pass

    setup_commands()

    print("\n".join([
        f"EDOPro HD Downloader v{DOWNLOADER_VERSION}",
        "Created by Nii Miyo",
        "Type \"/help\" for help"
    ]))


def to_download(card: DownloadCard):
    """Handles if a card should be downloaded and downloads it."""

    if (card.force) or (not already_downloaded(card)):
        success = download_image(card)
        if success: mark_as_downloaded(card)
        sleep(.2)


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
