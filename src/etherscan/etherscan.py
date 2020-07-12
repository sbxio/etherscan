from .library.utils.client import Client
from .library.account import Account
from .library.contract import Contract


MAINNET = "https://api.etherscan.io/api"


class Etherscan():

    def __init__(self, apikey: str, base_uri: str = MAINNET):
        self.set_clients(apikey, base_uri)

    def set_clients(self, apikey: str, base_uri: str = MAINNET):
        client = Client(apikey, base_uri)
        self.account = Account(client)
        self.contract = Contract(client)
