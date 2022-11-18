from requests import Response
from constants import YGOPRODECK_CARDS_URL
from web_access.request_helper import make_request


def _get_ids_from_response(response: Response) -> list[int]:
	"""Returns only the ids of the cards requested"""
	data = response.json().get("data")
	ids: list[int] = list()

	for c in data:
		for img in c.get("card_images"):
			ids.append(img.get("id"))
	return ids

def get_all_cards() -> list[int]:
	"""Returns the ids of all Yu-Gi-Oh! cards in `db.ygoprodeck.com` database"""

	try:
		response = make_request(YGOPRODECK_CARDS_URL)
		return _get_ids_from_response(response)
	except Exception as e:
		print(f"Error fetching db.ygoprodeck.com: {type(e).__name__}\n{e}")

	return list()

def get_all_fields() -> list[int]:
	"""
	Returns the ids of all Yu-Gi-Oh! Field Spell cards in
	`db.ygoprodeck.com` database
	"""

	try:
		response = make_request(
			YGOPRODECK_CARDS_URL,
			params={"type": "spell card","race": "field"}
		)
		return _get_ids_from_response(response)
	except Exception as e:
		print(f"Error fetching db.ygoprodeck.com: {type(e).__name__}\n{e}")

	return list()
