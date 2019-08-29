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
        self._api_key = config.get_api_keys('NASA')

    def feed(self, start_date: datetime.date, end_date: datetime.date, detailed=True) -> dict:
        """Retrieve a list of Asteroids based on their closest approach date to Earth."""
        @self._get_request('feed',
                           start_date=start_date,
                           end_date=end_date,
                           detailed=detailed)
        def inner(response):
            return response

        return inner

    def feed(self, detailed=True) -> dict:
        """Find Near Earth Objects for today"""
        @self._get_request('feed/today',
                           detailed=detailed)
        def inner(response):
            return response

        return inner

    def lookup(self, id) -> dict:
        """Lookup a specific Asteroid based on its NASA JPL small body (SPK-ID) ID"""
        @self._get_request('neo/{}'.format(id))
        def inner(response):
            return response

        return inner

    def browse(self) -> dict:
        """Browse the overall Asteroid data-set"""
        @self._get_request('neo/browse')
        def inner(response):
            return response

        return inner

    def sentry(self, is_active=True, page=0, size=50) -> dict:
        """Retrieve Sentry (Impact Risk) Near Earth Objects"""
        @self._get_request('neo/sentry',
                           is_active=str(is_active), page=str(page), size=str(size))
        def inner(response):
            return response

        return inner

    def sentry_by_id(self, id) -> dict:
        """Retrieve Sentry (Impact Risk) Near Earth Objectby ID"""
        @self._get_request('neo/sentry/{}'.format(id))
        def inner(response):
            return response

        return inner

    def stats(self) -> dict:
        """Get the Near Earth Object data set totals"""
        @self._get_request('stats')
        def inner(response):
            return response

        return inner


