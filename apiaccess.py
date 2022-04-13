from http.client import HTTPResponse as __HTTPResponse
from urllib import request as __request
from json import loads as __loads

api_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
__headers = {
    "User-Agent": "NiiMiyo-EDOPro-HD-Downloader/1.0"
}


def __get_ids_from_api_response(response: __HTTPResponse) -> list[int]:
    """Returns only the ids of the cards requested"""

    data = __loads(response.read()).get("data")
    ids = [c.get("id") for c in data]
    return ids


def get_all_cards() -> list[int]:
    """Returns the ids of all Yu-Gi-Oh! cards in
    db.ygoprodeck.com database"""

    try:
        request = __request.Request(api_url, headers=__headers)
        response = __request.urlopen(request)
    except Exception as e:
        print(e)
        return list()
    else:
        return __get_ids_from_api_response(response)


def get_all_fields() -> list[int]:
    """Returns the ids of all Yu-Gi-Oh! Field Spell cards in
    db.ygoprodeck.comdatabase"""

    try:
        params = r"?type=spell%20card&race=field"
        request = __request.Request(api_url + params, headers=__headers)
        response = __request.urlopen(request)
    except Exception as e:
        print(e)
        return list()
    else:
        return __get_ids_from_api_response(response)
