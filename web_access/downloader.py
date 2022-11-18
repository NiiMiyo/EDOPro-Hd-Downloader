import requests
from os.path import join

from commands.typing import DownloadCard
from constants import IMAGES_BASE_URL

def download_image(card: DownloadCard) -> bool:
	"""
	Downloads the card image or artwork and puts in the specified folder.

	Returns `True` if downloads successfully, otherwise returns `False`.
	"""

	url = IMAGES_BASE_URL
	store_at = "./pics/"

	if card.artwork:
		url += "_cropped"
		store_at += "field/"
	url += f"/{card.card_id}.jpg"

	file_path = join(store_at, f"{card.card_id}.jpg")
	try:
		res = requests.get(url)
		with open(file_path, 'wb+') as f:
			f.write(res.content)
		return True
	except Exception as e:
		print(f"Error downloading '{card.card_id}': {type(e).__name__}\n{e}")
		return False
