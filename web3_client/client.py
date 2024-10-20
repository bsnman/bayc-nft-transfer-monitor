from web3 import Web3
from web3.contract import Contract
from django.conf import settings
from web3_client.minimal_abi import minimal_abi

INFURA_URL = "https://mainnet.infura.io/v3/" + settings.INFURA_API_KEY

web3 = Web3(Web3.HTTPProvider(INFURA_URL))


def get_contract(contract_address: str) -> Contract:
    return web3.eth.contract(address=contract_address, abi=minimal_abi)
