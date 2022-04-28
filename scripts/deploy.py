from http.client import NETWORK_AUTHENTICATION_REQUIRED
from unittest import mock
from brownie import accounts, config, FundMe, network, MockV3Aggregator
from scripts.common_scripts import getAccount, deployarMockPrecioETH, LOCAL_BLOCKCHAIN_ENVS
from scripts.fund_and_withdraw import fund



def deploy_fund_me():
    account = getAccount()
    print (f"Account: {account}")
    #0x8A753747A1Fa494EC906cE90E9f37563A8AF630e Address de Chainlink Rinkeby
    if(network.show_active() not in LOCAL_BLOCKCHAIN_ENVS):
        addressOracle = config["networks"][network.show_active()]["ETH_USD"]
    else:       
        deployarMockPrecioETH()
        addressOracle = MockV3Aggregator[-1].address



    fund_me = FundMe.deploy(addressOracle,{"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"contrato deployado cuya address es  {fund_me.address}")

    return fund_me
    
def main():
    deploy_fund_me()