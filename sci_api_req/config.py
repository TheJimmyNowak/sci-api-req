_api_keys = {
    "NASA": ""
}


def set_api_keys(api_and_key: tuple) -> None:
    if len(api_and_key) > 2:
        raise Exception("Too many args")
    api, key = api_and_key
    _api_keys[api] = key


def get_api_keys(k) -> str:
    return _api_keys[k]