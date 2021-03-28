from urllib import request as __request
from os.path import join as __join

def download_image(card_id: int, is_artwork: bool = False):
    """Downloads the card image or artwork and
    puts in the specified folder"""

    img_url = "https://storage.googleapis.com/ygoprodeck.com/pics"
    if not is_artwork:
        img_url += f"/{card_id}.jpg"
        store_at = "./pics/"
    else:
        img_url += f"_artgame/{card_id}.jpg"
        store_at = "./pics/field/"

    file_path = __join(store_at, f"{card_id}.jpg")
    try:
        __request.urlretrieve(img_url, file_path)
        return True

    except Exception as e:
        print(e)
        return False
