from functools import wraps

import requests


class ApiProvider(object):
    """Parent class for api requesters"""
    __slots__ = ['_api_url', '_api_key']

    def __init__(self):
        self._api_url = None
        self._api_key = None

    def _get_request(self, endpoint: str, **parameters):
        """Make GET request to api and inject response to response kwarg"""
        def inner_function(f):
            @wraps(f)
            def wrapper():
                if self._api_key:
                    parameters['api_key'] = self._api_key

                response = requests.get(self._api_url + endpoint, params=parameters)

                if response.content:
                    response = response.json()
                else:
                    print("WARNING!!! Api returned empty response. That could cause exception")

                return f(response=response)

            return wrapper()

        return inner_function
