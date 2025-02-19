import time

from web3 import Web3
from web3.eth import Eth

headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
        }

w3 = Web3(
    provider=Web3.HTTPProvider(
        endpoint_uri='https://testnet-rpc.monad.xyz',
        request_kwargs={'headers': headers} # 'proxy': proxy,
    ),
    modules={'eth': Eth},
    middleware=[]
)

def get_balance(address: str):
    address = Web3.to_checksum_address(address.strip())
    balance = w3.eth.get_balance(account=address) / 10 ** 18
    return address, balance

def main():
    result = {}
    non_zero = 0
    with open('wallets.txt') as f:
        wallets = f.readlines()

    for wallet in wallets:
        address, balance = get_balance(wallet)
        result[address] = balance
        time.sleep(.5)
        print(f"Address: {address}, balance {balance} MON")
        if balance != 0:
            non_zero += 1

    print(f'\n\n\n')
    print(f"Found total {non_zero} non zero balances on wallets:")
    for address, balance in result.items():
        if balance != 0:
            print(f"Address: {address}, balance {balance} MON")


if __name__ == '__main__':
    main()
