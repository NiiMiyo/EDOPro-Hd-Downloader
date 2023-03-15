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
from pprint import pprint

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

def down_loop(cards, total_cards, progression, stopper):
    # For each card, download
    for index, card in enumerate(cards, 1):
        # If KeyboardInterrupt
        stop = stopper.get()
        if stop:
            stopper.put(True)
            break
        # We have to put it back in Queue so the Programm doesn't freeze
        stopper.put(False)

        progress = progression.get()
        to_download(card)

        # Prints progress
        progress += 1
        progression.put(progress)
        percentage   = f"{((progress * 100) / total_cards):.2f}%"
        print(f"Downloaded {progress}/{total_cards} - {percentage}", end="\r")

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

            # Put the progression variable in a Queue so the threads can safely manipulate it while running
            progress = Queue()
            progress.put(0)

            # For the KeyboardInterrupt
            stopper = Queue()
            stopper.put(False)

            thread1 = Thread(target=down_loop, args=(cards1, total_cards, progress, stopper,))
            thread2 = Thread(target=down_loop, args=(cards2, total_cards, progress, stopper,))
            thread3 = Thread(target=down_loop, args=(cards3, total_cards, progress, stopper,))

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

        try:
            stopper.put(True)
        except:
            print("No Downloads to stop")

        quit()
    # In case of a not expected exception
    except Exception: print_exc()


if __name__ == "__main__": main()
