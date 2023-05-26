from constants import ID_CONVERSION

def convert_id(card_id: int) -> int:
	"""
	Converts cards id from YGOProDeck database to EDOPro database

	See https://github.com/NiiMiyo/EDOPro-Hd-Downloader/issues/8
	"""

	return ID_CONVERSION.get(card_id, card_id)
