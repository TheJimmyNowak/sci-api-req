from datetime import date

from sci_api_req import config
from ..api_provider import ApiProvider


class APODProvider(ApiProvider):
    """
    Astronomy picture of the day. Requires NASA api key.
    For more informations see https://api.nasa.gov/api.html#apod
    """
    def __init__(self):
        super(ApiProvider).__init__()
        self._api_url = "https://api.nasa.gov/planetary/apod"

    @property
    def api_key(self) -> str:
        return config.get_api_keys('NASA')

    def get_apod(self, date=date.today(), hd=False):
        @self._get_request('', date=date, hd=hd)
        def inner(response):
            return response

        return inner

