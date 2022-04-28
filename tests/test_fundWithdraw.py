from brownie import accounts, network, exceptions
from pytest import skip
from scripts.common_scripts import getAccount, LOCAL_BLOCKCHAIN_ENVS
from scripts.deploy import deploy_fund_me
import pytest

def test_FondearRetirar():
    account = getAccount()
    contrato = deploy_fund_me()
    tx = contrato.fund({"from":account, "value":100000000000})
    tx.wait(1)
         
    assert(contrato.addressToAmountFunded(account.address) == 100000000000)

    tx = contrato.withdraw({"from":account})
    tx.wait(1)
    assert(contrato.addressToAmountFunded(account.address) == 0)

def test_SoloExtraeOwner():
    if (network.show_active() not in LOCAL_BLOCKCHAIN_ENVS):
        pytest.skip("solo para prueba local")

    account = getAccount()
    contrato = deploy_fund_me()
    accountTrucha = accounts.add()
    
    with pytest.raises(exceptions.VirtualMachineError):
        contrato.withdraw({"from":accountTrucha})

