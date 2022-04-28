from brownie import accounts, config, FundMe, network, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
PRECIO_ETH = 280000000000
LOCAL_BLOCKCHAIN_ENVS = ["development", "ganache-fh"]
FORKED_LOCAL_ENVS = ["mainnet-fork", "mainnet-fork-dev"] 

def getAccount():
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVS or network.show_active() in FORKED_LOCAL_ENVS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deployarMockPrecioETH():
    if (len(MockV3Aggregator)<=0):
            print(f"Deployando mocks, porque la Active Network {network.show_active()} es local")
            MockV3Aggregator.deploy(DECIMALS,PRECIO_ETH,{"from":getAccount()})
        
    