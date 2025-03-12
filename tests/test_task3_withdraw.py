from main1 import BankAccount
import pytest

@pytest.mark.parametrize("balance, amount, expected_result",
                         [
                             (50000, 20000, 30000),
                             (1000, 500, 500),
                             (10000, 2000, 8000)
                         ])
def test_withdraw_positive(balance, amount, expected_result):
    acc = BankAccount()
    acc.deposit(balance)
    acc.withdraw(amount)
    assert acc.get_balance() == expected_result

@pytest.mark.parametrize("balance, amount, expected_result",
                         [
                             (5000, 6000, ValueError),
                             (5000, "1231", TypeError)
                         ])
def test_withdraw_negative(balance, amount, expected_result):
    acc = BankAccount()
    acc.deposit(balance)

    with pytest.raises(expected_result):
        acc.withdraw(amount)

@pytest.mark.parametrize("balance, amount, expected_result",
                         [
                             (5000, 0, ValueError),
                             (5000, -1000, ValueError)
                         ])
def test_withdraw_negative(balance, amount, expected_result):
    acc = BankAccount()
    acc.deposit(balance)

    with pytest.raises(expected_result):
        acc.withdraw(amount)