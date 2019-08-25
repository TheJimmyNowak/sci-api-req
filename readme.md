# sci-api-req
Sci-api-req is library facilitating use of the most popular apis.

```python
import config
from requesters.NASA.neows_provider import NeoWsProvider


config.set_api_keys(('NASA', 'Your NASA API KEY'))
requester = NeoWsRequester()

print(requester.feed())
print(requester.sentry())
```

