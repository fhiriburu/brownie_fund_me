from brownie import accounts, config, FundMe, network
from scripts.common_scripts import getAccount, deployarMockPrecioETH, LOCAL_BLOCKCHAIN_ENVS

def fund():
    contratoFundMe = FundMe[-1]
    account = getAccount()   
    #montoMinimo = contratoFundMe.getEntranceFee()
    #print("el monto minimo es de {montominimo}")
    contratoFundMe.fund({"from":account, "value":100000000000})


def withdraw():
    account = getAccount()
    contratoFundMe = FundMe[-1]
    contratoFundMe.withdraw({"from":account})

def main():
    fund()
    withdraw()