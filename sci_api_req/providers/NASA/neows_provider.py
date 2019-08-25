from ..api_provider import ApiProvider
from sci_api_req import config
import datetime


class NeoWsProvider(ApiProvider):
    """
    You can use NeoWs(Near Earth Object Web Service) to search for Asteroids based on
    their closest approach date to Earth, lookup a specific Asteroid with its NASA JPL
    small body id, as well as browse the overall data-set. Requires Nasa Key. For more
    information check that https://api.nasa.gov/api.html#NeoWS
    """
    def __init__(self):
        super(ApiProvider).__init__()
        self._api_url = "https://api.nasa.gov/neo/rest/v1/"

    @property
    def api_key(self) -> str:
        return config.get_api_keys('NASA')

    """Retrieve a list of Asteroids based on their closest approach date to Earth."""
    def feed(self, start_date: datetime.date, end_date: datetime.date, detailed=True) -> dict:
        @self._get_request('feed',
                           start_date=start_date,
                           end_date=end_date,
                           detailed=detailed)
        def inner(response):
            return response

        return inner

    """Find Near Earth Objects for today"""
    def feed(self, detailed=True) -> dict:
        @self._get_request('feed/today', detailed=detailed)
        def inner(response):
            return response

        return inner
    """Lookup a specific Asteroid based on its NASA JPL small body (SPK-ID) ID"""
    def lookup(self, id) -> dict:
        @self._get_request('neo/{}'.format(id))
        def inner(response):
            return response

        return inner

    """Browse the overall Asteroid data-set"""
    def browse(self) -> dict:
        @self._get_request('neo/browse')
        def inner(response):
            return response

        return inner

    """Retrieve Sentry (Impact Risk) Near Earth Objects"""
    def sentry(self, is_active=True, page=0, size=50) -> dict:
        @self._get_request('neo/sentry', is_active=str(is_active), page=str(page), size=str(size))
        def inner(response):
            return response

        return inner

    """Retrieve Sentry (Impact Risk) Near Earth Objectby ID"""
    def sentry_by_id(self, id) -> dict:
        @self._get_request('neo/sentry/{}'.format(id))
        def inner(response):
            return response

        return inner

    """Get the Near Earth Object data set totals"""
    def stats(self) -> dict:
        @self._get_request('stats')
        def inner(response):
            return response

        return inner


