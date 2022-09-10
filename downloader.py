from urllib import request as __request
from os.path import join as __join

from commands.typing import DownloadCard

def download_image(card: DownloadCard):
    """Downloads the card image or artwork and
    puts in the specified folder"""

    img_url = "https://storage.googleapis.com/ygoprodeck.com/pics"
    if not card.artwork:
        img_url += f"/{card.card_id}.jpg"
        store_at = "./pics/"
    else:
        img_url += f"_artgame/{card.card_id}.jpg"
        store_at = "./pics/field/"

    file_path = __join(store_at, f"{card.card_id}.jpg")
    try:
        __request.urlretrieve(img_url, file_path)
        return True

    except Exception as e:
        print(f"Error downloading '{card.card_id}': {e}")
        return False
