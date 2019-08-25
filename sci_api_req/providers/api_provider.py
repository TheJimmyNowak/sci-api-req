from functools import wraps

import requests


class ApiProvider(object):
    """Parent class for api requesters"""
    __slots__ = ['_api_url']

    def __init__(self):
        self._api_url = None

    @property
    def api_url(self) -> str:
        return self._api_url

    """Access key to api"""
    @property
    def api_key(self) -> str:
        return "Hasn\'t set yet"

    """Make GET request to api and inject response to response kwarg"""
    def _get_request(self, endpoint: str, **parameters):
        def inner_function(f):
            @wraps(f)
            def wrapper():
                param_string = ""
                for i in parameters:
                    param_string += i + "=" + str(parameters[i]) + "&"

                url = "{}{}?{}api_key={}".format(self.api_url, endpoint, param_string, self.api_key)
                response = requests.get(url)

                if response.content:
                    response = response.json()
                else:
                    print("WARNING!!! Api returned empty response. That could cause exception")

                return f(response=response)

            return wrapper()

        return inner_function
