from os.path import exists
from time import sleep
from traceback import print_exc
from commands.setup import setup_commands
from constants import DOWNLOADER_VERSION, INPUT_STRING, SETUP_CREATION_FILES

from input_handler import handle_input
from commands.typing import DownloadCard
from web_access.downloader import download_image
from tracker import (already_downloaded, mark_as_downloaded)

from threading import Thread
from queue import Queue

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

def down_loop(cards, total_cards, q):
    # For each card, download
    for index, card in enumerate(cards, 1):
        progress = q.get()
        to_download(card)

        # Prints progress
        progress += 1
        q.put(progress)
        percentage   = f"{((progress * 100) / total_cards):.2f}%"
        print(f"Downloaded {progress} - {percentage}", end="\r")

def main():
    initialize()

    try:
        while True:
            cards = handle_input( input(INPUT_STRING) )

            # If couldn't find what to download
            if cards is None:
                print("Deck or command not found.")
                continue

            # Using Threads to download 3 images at once
            total_cards = len(cards)
            one_third = int((total_cards-1)/3)

            cards1 = cards[:one_third]
            cards2 = cards[one_third:one_third*2]
            cards3 = cards[one_third*2:]


            q = Queue()
            progress = 0
            q.put(progress)

            thread1 = Thread(target=down_loop, args=(cards1, total_cards, q,))
            thread2 = Thread(target=down_loop, args=(cards2, total_cards, q,))
            thread3 = Thread(target=down_loop, args=(cards3, total_cards, q,))

            thread1.start()
            thread2.start()
            thread3.start()

            thread1.join()
            thread2.join()
            thread3.join()

            print("\n")

    # In case of interrupting the program with Ctrl+C
    except KeyboardInterrupt:
        print("\n\nForcing program interruption...")
        quit()
    # In case of a not expected exception
    except Exception: print_exc()


if __name__ == "__main__": main()
