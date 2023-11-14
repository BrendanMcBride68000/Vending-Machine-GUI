import pytest
from vending_machine_BM import VendingMachine, WaitingState, AddCoinsState, DeliverProductState, CountChangeState

@pytest.fixture
def test_VendingMachine():
    machine = VendingMachine()
    machine.add_state(WaitingState())
    machine.add_state(AddCoinsState())
    machine.add_state(DeliverProductState())
    machine.add_state(CountChangeState())
    machine.go_to_state('waiting')
    return machine

def test_initial_amount(test_VendingMachine):
    assert test_VendingMachine.amount == 0

def test_add_nickel(test_VendingMachine):
    test_VendingMachine.add_coin('Nickel (5¢)')
    assert test_VendingMachine.amount == 5

def test_add_dime(test_VendingMachine):
    test_VendingMachine.add_coin('Dime (10¢)')
    assert test_VendingMachine.amount == 10

def test_add_quarter(test_VendingMachine):
    test_VendingMachine.add_coin('Quarter (25¢)')
    assert test_VendingMachine.amount == 25
    
def test_add_quarter(test_VendingMachine):
    test_VendingMachine.add_coin('Loonie ($1)')
    assert test_VendingMachine.amount == 100

def test_add_quarter(test_VendingMachine):
    test_VendingMachine.add_coin('Toonie ($2)')
    assert test_VendingMachine.amount == 200
