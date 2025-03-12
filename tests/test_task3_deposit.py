from main1 import BankAccount
import pytest

@pytest.mark.parametrize("amount, expected_result",
                         [
                             (50000, 50000),
                             (1000, 1000),
                             (10000, 10000)
                         ])
def test_deposit_positive(amount, expected_result):
    acc = BankAccount()
    acc.deposit(amount)
    assert acc.get_balance() == expected_result

@pytest.mark.parametrize("amount, expected_result",
                         [
                             (-1000, ValueError),
                             ("0", TypeError)
                         ])
def test_deposit_negative(amount, expected_result):
    acc = BankAccount()
    with pytest.raises(expected_result):
        acc.deposit(amount)

@pytest.mark.parametrize("amount, expected_result",
                         [
                             (0, ValueError)
                         ])
def test_deposit_bound(amount, expected_result):
    acc = BankAccount()
    with pytest.raises(expected_result):
        acc.deposit(amount)