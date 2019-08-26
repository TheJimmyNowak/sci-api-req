from datetime import date, timedelta

from sci_api_req import config
from sci_api_req.providers.NASA.donki_provider import DONKIProvider
from sci_api_req.providers.NASA.neows_provider import NeoWsProvider


# Set NASA API key
config.set_api_keys(('NASA', 'CeJOODBdDRDhAbcsB4H89tSIJFkUD0hCkQu760nf'))

# Initialize providers
DONKI_provider = DONKIProvider()
NeoWs_provider = NeoWsProvider()

print("Hello today is: {}".format(date.today()))

# Get DONKI notifications
notifications = DONKI_provider.notifications(date.today() - timedelta(30), date.today())

print("In last 30 days was {} notifications".format(len(notifications)))
# Print type and message
print("It's the last one notification:\n"
      "Type: {}\n"
      "{}".format(notifications[0]['messageType'], notifications[0]['messageBody']))

# Get near close objects for today
neo_feed = NeoWs_provider.feed()
print("It's near earth asteroid id's:")
for i in neo_feed['near_earth_objects'][str(date.today())]:
    print(i['id'])
    print("Does it hazardous?: {}\n".format(i['is_potentially_hazardous_asteroid']))
