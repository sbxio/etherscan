from typing import Optional, Sequence

from .utils.client import Client


class Account():

    def __init__(self, client: Client):
        self.request = client.request

    def get_balance(self, address: str) -> object:
        # Get Ether Balance for a single Address

        params = {
            "module": "account",
            "action": "balance",
            "address": address,
            "tag": "latest",
        }
        res = self.request("GET", params=params)
        return res["result"]

    def get_balancemulti(self, addresses: Sequence[str]) -> object:
        # Get Ether Balance for multiple Addresses in a single call

        params = {
            "module": "account",
            "action": "balancemulti",
            "address": addresses,
            "tag": "latest",
        }
        res = self.request("GET", params=params)
        return res["result"]

    def get_txlist(
        self,
        address: str,
        startblock: Optional[int] = None,
        endblock: Optional[int] = None,
        page: Optional[int] = None,
        offset: Optional[int] = None,
        sort: str = "asc",
    ) -> object:
        # Get a list of 'Normal' Transactions By Address

        params = {
            "module": "account",
            "action": "txlist",
            "address": address,
            "sort": sort,
        }

        if startblock:
            params["startblock"] = startblock
        if endblock:
            params["endblock"] = endblock
        if page:
            params["page"] = page
        if offset:
            params["offset"] = offset

        res = self.request("GET", params=params)
        return res["result"]

    def get_txlistinternal(
        self,
        address: str,
        startblock: Optional[int] = None,
        endblock: Optional[int] = None,
        page: Optional[int] = None,
        offset: Optional[int] = None,
        sort: str = "asc",
    ) -> object:
        # Get a list of 'Internal' Transactions by Address

        params = {
            "module": "account",
            "action": "txlistinternal",
            "address": address,
            "sort": sort,
        }

        if startblock:
            params["startblock"] = startblock
        if endblock:
            params["endblock"] = endblock
        if page:
            params["page"] = page
        if offset:
            params["offset"] = offset

        res = self.request("GET", params=params)
        return res["result"]

    def get_txlistinternal_by_txhash(self, txhash: str) -> object:
        # Get "Internal Transactions" by Transaction Hash

        params = {
            "module": "account",
            "action": "txlistinternal",
            "txhash": txhash,
            "tag": "latest",
        }
        res = self.request("GET", params=params)
        return res["result"]

    def get_tokentx(
        self,
        address: str,
        contractaddress: Optional[str] = None,
        startblock: Optional[int] = None,
        endblock: Optional[int] = None,
        page: Optional[int] = None,
        offset: Optional[int] = None,
        sort: str = "asc",
    ) -> object:
        # Get a list of "ERC20 - Token Transfer Events" by Address

        params = {
            "module": "account",
            "action": "tokentx",
            "address": address,
            "sort": sort,
        }

        if contractaddress:
            params["contractaddress"] = contractaddress
        if startblock:
            params["startblock"] = startblock
        if endblock:
            params["endblock"] = endblock
        if page:
            params["page"] = page
        if offset:
            params["offset"] = offset

        res = self.request("GET", params=params)
        return res["result"]

    def get_minedblocks(
        self,
        address: str,
        page: Optional[int] = None,
        offset: Optional[int] = None,
        blocktype: str = "blocks",
    ) -> object:
        # Get list of Blocks Mined by Address

        params = {
            "module": "account",
            "action": "getminedblocks",
            "blocktype": blocktype,
            "address": address,
        }

        if page:
            params["page"] = page
        if offset:
            params["offset"] = offset

        res = self.request("GET", params=params)
        return res["result"]
