from sci_api_req.providers.api_provider import ApiProvider


class Test(ApiProvider):
    def __init__(self):
        super(ApiProvider).__init__()
        self._api_url = "https://sscweb.sci.gsfc.nasa.gov/WS/sscr/2"

    @property
    def api_key(self) -> str:
        return ""

    def a(self):
        @self._post_request("/locations")
        def b(response):
            print(response)

from sci_api_req.providers.openaq_provider import OpenaqProvider


