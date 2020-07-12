from .utils.client import Client


class Contract():

    def __init__(self, client: Client):
        self.request = client.request

    def get_contract_abi(self, address: str) -> object:
        # Get Contract ABI for Verified Contract Source Codes

        params = {
            "module": "contract",
            "action": "getabi",
            "address": address
        }
        res = self.request("GET", params=params)
        return res["result"]
