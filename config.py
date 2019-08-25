class Config:
    __slots__ = []

    @property
    def api_keys(self) -> dict:
        return {
            'NASA': ""
        }

    @api_keys.setter
    def api_keys(self, api_and_key: tuple) -> None:
        if len(api_and_key) > 2:
            raise Exception("Too many args")

        api, key = api_and_key

        self.api_keys[api] = key
