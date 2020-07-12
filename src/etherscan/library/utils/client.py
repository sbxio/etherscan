import json
import requests

from ..models.errors import ApiError


class ApiMixin:

    def request(self, verb: str, params: object = {}):
        if verb == "GET":
            try:
                res = requests.get(
                    self.base_uri,
                    params={**params, **{"apikey": self.apikey}},
                )
            except requests.RequestException:
                raise
        else:
            raise NotImplementedError
        return self._parse_json(res.content.decode("utf-8"))

    def _parse_json(self, json_data):
        try:
            data = json.loads(json_data)
            if data["status"] == 0:
                raise ApiError(data["message"])
            return data
        except:
            raise


class Client(ApiMixin):

    def __init__(self, apikey: str, base_uri: str):
        self.base_uri = base_uri
        self.apikey = apikey
