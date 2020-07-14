from .library.utils.client import Client
from .library.account import Account
from .library.contract import Contract


MAINNET = "https://api.etherscan.io/api"
ROPSTEN = "https://api-ropsten.etherscan.io/api"


class Etherscan():

    @property
    def account(self) -> Account:
        # account controller
        return self._account

    @property
    def contract(self) -> Contract:
        # contract controller
        return self._contract

    def __init__(self, apikey: str, base_uri: str = MAINNET):
        client = Client(apikey, base_uri)
        self._account = Account(client)
        self._contract = Contract(client)
