import datetime

from sci_api_req import config
from ..api_provider import ApiProvider


class DONKIProvider(ApiProvider):
    """
    The Space Weather Database Of Notifications, Knowledge, Information (DONKI) is
    a comprehensive on-line tool for space weather forecasters, scientists, and the
    general space science community. DONKI provides chronicles the daily interpretations
    of space weather observations, analysis, models, forecasts, and notifications
    provided by the Space Weather Research Center (SWRC), comprehensive knowledge-base
    search functionality to support anomaly resolution and space science research,
    intelligent linkages, relationships, cause-and-effects between space weather
    activities and comprehensive webservice API access to information stored in DONKI.
    For more information see: https://api.nasa.gov/api.html#DONKI. Requires NASA api key
    """

    def __init__(self):
        super(ApiProvider).__init__()
        self._api_url = "https://api.nasa.gov/DONKI/"

    @property
    def api_key(self) -> str:
        return config.get_api_keys('NASA')

    def coronal_mass_ejection(self, start_date=datetime.date.today() - datetime.timedelta(30),
                              end_date=datetime.date.today()):
        @self._get_request(
            'CME',
            startDate=start_date,
            endDate=end_date)
        def inner(response):
            return response

        return inner

    def coronal_mass_ejection_analysis(
            self, start_date=datetime.date.today() - datetime.timedelta(30),
            end_date=datetime.date.today(), most_accurate_only=True,
            complete_entry_only=True, speed=0, halfAngle=0, catalog="ALL",
            keyword="NONE") -> dict:
        @self._get_request(
            'CMEAnalysis',
            startDate=start_date,
            endDate=end_date,
            mostAccurateOnly=most_accurate_only,
            completeEntryOnly=complete_entry_only,
            speed=speed, halfAngle=halfAngle,
            catalog=catalog,
            keyword=keyword)
        def inner(response):
            return response

        return inner

    def geomagnetic_storm(self, start_date=datetime.date.today() - datetime.timedelta(30),
                          end_date=datetime.date.today()):
        @self._get_request('GST', startDate=start_date, endDate=end_date)
        def inner(response):
            return response

        return inner

    def interplanetary_shock(self, start_date=datetime.date.today() - datetime.timedelta(30),
                             end_date=datetime.date.today(), location="ALL", catalog="ALL"):
        @self._get_request('IPS', startDate=start_date, endDate=end_date, location=location,
                           catalog=catalog)
        def inner(response):
            return response

        return inner

    def solar_flare(self, start_date=datetime.date.today() - datetime.timedelta(30),
                             end_date=datetime.date.today()):
        @self._get_request('FLR', startDate=start_date, endDate=end_date)
        def inner(response):
            return response

        return inner

    def solar_energetic_particle(self, start_date=datetime.date.today() - datetime.timedelta(30),
                             end_date=datetime.date.today()):
        @self._get_request('SEP', startDate=start_date, endDate=end_date)
        def inner(response):
            return response

        return inner

    def magnetopause_crossing(self, start_date=datetime.date.today() - datetime.timedelta(30),
                             end_date=datetime.date.today()):
        @self._get_request('MPC', startDate=start_date, endDate=end_date)
        def inner(response):
            return response

        return inner

    def radiation_belt_enhancment(self, start_date=datetime.date.today() - datetime.timedelta(30),
                             end_date=datetime.date.today()):
        @self._get_request('RBE', startDate=start_date, endDate=end_date)
        def inner(response):
            return response

        return inner

    def hight_speed_stream(self, start_date=datetime.date.today() - datetime.timedelta(30),
                             end_date=datetime.date.today()):
        @self._get_request('HSS', startDate=start_date, endDate=end_date)
        def inner(response):
            return response

        return inner

    def wsa_enlil_simulation(self, start_date=datetime.date.today() - datetime.timedelta(30),
                             end_date=datetime.date.today()):
        @self._get_request('EnlilSimulations', startDate=start_date, endDate=end_date)
        def inner(response):
            return response

        return inner

    def notifications(self, start_date: datetime.date, end_date: datetime.date, type="all"):
        @self._get_request('notifications', startDate=start_date, endDate=end_date, type=type)
        def inner(response):
            return response

        return inner