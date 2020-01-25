# sci-api-req
![GitHub watchers](https://img.shields.io/github/watchers/miki164/sci-api-req?label=Watch&style=social)
![GitHub stars](https://img.shields.io/github/stars/miki164/sci-api-req?style=social)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/miki164/sci-api-req?sort=semver)
![PyPI](https://img.shields.io/pypi/v/sci-api-req)
![GitHub issues](https://img.shields.io/github/issues/miki164/sci-api-req?color=green&style=flat)
![GitHub repo size](https://img.shields.io/github/repo-size/miki164/sci-api-req)
![GitHub](https://img.shields.io/github/license/miki164/sci-api-req)


Sci-api-req is library facilitating use of the most popular scientific apis.
With this tool you could make requests to NASA apis e.g. "Astronomy picture of the day"

```python
from sci_api_req import config
from sci_api_req.providers.NASA.neows_provider import NeoWsProvider

#Set your NASA API key
config.set_api_keys(('NASA', 'Your NASA API KEY'))
provider = NeoWsProvider()

#Retrieve a list of Asteroids based on 
#their closest approach date to Earth.
print(provider.feed())
#Retrieve Sentry (Impact Risk ) Near Earth Objects
print(provider.sentry())
```
If you want try install it via PyPi:
```
pip install sci-api-req
```
List of all APIs you can now use with the library:
* NeoWs (Near Earth Object Web Service)
* Astronomy Picture of the Day
* Space Weather Database Of Notifications, Knowledge, Information (DONKI)
* OpenAQ
