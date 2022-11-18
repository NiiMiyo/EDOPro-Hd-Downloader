from typing import Any, Optional
import requests
from constants import REQUEST_HEADERS

def make_request(
	url: str,
	params: Optional[dict[Any, Any]] = None
) -> requests.Response:

	return requests.get(url, headers=REQUEST_HEADERS, params=params)
