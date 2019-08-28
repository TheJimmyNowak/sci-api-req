from sci_api_req.providers.api_provider import ApiProvider


class OpenaqProvider(ApiProvider):
    """
    Don't require key. Enjoy
    See link for docs https://docs.openaq.org/
    """
    def __init__(self):
        super(ApiProvider).__init__()
        self._api_url = "https://api.openaq.org/v1/"

    def cities(self, **kwargs):
        """
        Provides a simple listing of cities within the platform.
        View https://docs.openaq.org/#api-Cities for more
        :param kwargs: Pass params country, order_by, sort, limit, page
        :return: Response dict
        """

        @self._get_request('cities', **kwargs)
        def inner_function(response):
            return response

        return inner_function

    def countries(self, **kwargs):
        """
        Provides a simple listing of countries within the platform.
        View https://docs.openaq.org/#api-Countries for more

        :param kwargs: Pass params order_by, sort, limit, page
        :return: Response dict
        """

        @self._get_request('countries', **kwargs)
        def inner_function(response):
            return response

        return inner_function

    def fetches(self, **kwargs):
        """
        Providing data about individual fetch operations that are used to populate data in the platform.
        View https://docs.openaq.org/#api-Fetches for more

        :param kwargs: Pass params order_by, sort, limit, page
        :return: Response dict
        """

        @self._get_request('fetches', **kwargs)
        def inner_function(response):
            return response

        return inner_function

    def latest(self, **kwargs):
        """
        Provides the latest value of each available parameter for every location in the system.
        View https://docs.openaq.org/#api-Latest for more

        :param kwargs: Params city, country, location,
        parameter, has_geo, coordinates, radius, order_by, sort, limit, page
        :return: response dict
        """

        @self._get_request('latest', **kwargs)
        def inner_function(response):
            return response

        return inner_function

    def locations(self, **kwargs):
        """
        Provides a list of measurement locations and their meta data.
        View https://docs.openaq.org/#api-Locations for more
        :param kwargs: Params city, country, location,
        parameter, has_geo, coordinates, radius, order_by, sort, limit, page
        :return: response dict
        """

        @self._get_request('locations', **kwargs)
        def inner_function(response):
            return response

        return inner_function

    def measurements(self, **kwargs):
        """
        Provides data about individual measurements
        View https://docs.openaq.org/#api-Measurements for more
        :param kwargs: Params city, country, location,
        parameter, has_geo, coordinates, radius, value_from,
        value_to, date_from, date_to, order_by, sort, include_fields,
        limit, page, format
        :return: response dict
        """

        @self._get_request('measurements', **kwargs)
        def inner_function(response):
            return response

        return inner_function

    def parameters(self, **kwargs):
        """
        Provides a simple listing of parameters within the platform.
        View https://docs.openaq.org/#api-Parameters for more
        :param kwargs: Params order_by, sort
        :return: Response dict
        """

        @self._get_request('parameters', **kwargs)
        def inner_function(response):
            return response

        return inner_function

    def sources(self, **kwargs):
        """
        Provides a list of data sources.
        :param kwargs: Params order_by, sort, limit, page
        :return: Response dict
        """

        @self._get_request('sources', **kwargs)
        def inner_function(response):
            return response

        return inner_function
