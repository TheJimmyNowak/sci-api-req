# sci-api-req
Sci-api-req is library facilitating use of the most popular apis.

```python
from sci_api_req import config
from sci_api_req.providers.NASA.neows_provider import NeoWsProvider


config.set_api_keys(('NASA', 'Your NASA API KEY'))
requester = NeoWsProvider()

print(requester.feed())
print(requester.sentry())
```
If you want try install it via TestPyPi:
pip install -i https://test.pypi.org/simple/ sci-api-req
