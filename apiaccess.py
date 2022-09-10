from http.client import HTTPResponse as __HTTPResponse
from urllib import request as __request
from json import loads as __loads

API_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
"""Base API URL for YGOProDeck"""

API_HEADER = {
    "User-Agent": "NiiMiyo-EDOPro-HD-Downloader/2.0.1"
}
"""Header JSON to be used in an API request"""

def __get_ids_from_api_response(response: __HTTPResponse) -> list[int]:
    """Returns only the ids of the cards requested"""

    data = __loads(response.read()).get("data")
    ids: list[int] = list()

    for card in data:
        for image in card.get("card_images"):
            ids.append(image.get("id"))

    return ids


def get_all_cards() -> list[int]:
    """Returns the ids of all Yu-Gi-Oh! cards in
    `db.ygoprodeck.com` database"""

    try:
        request = __request.Request(API_URL, headers=API_HEADER)
        response = __request.urlopen(request)
    except Exception as e:
        print(f"Error fetching db.ygoprodeck.com: {e}")
        return list()
    else:
        return __get_ids_from_api_response(response)


def get_all_fields() -> list[int]:
    """Returns the ids of all Yu-Gi-Oh! Field Spell cards in
    `db.ygoprodeck.com` database"""

    try:
        params = r"?type=spell%20card&race=field"
        request = __request.Request(API_URL + params, headers=API_HEADER)
        response = __request.urlopen(request)
    except Exception as e:
        print(e)
        return list()
    else:
        return __get_ids_from_api_response(response)
