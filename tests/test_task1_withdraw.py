from main1 import BankAccount
import pytest


@pytest.fixture()
def bank_account():
    return BankAccount(50000)


@pytest.mark.bank_account
@pytest.mark.parametrize("amount, expected_result",
                         [
                             (20000, 30000),
                             (500, 49500),
                             (2000, 48000)
                         ])
def test_withdraw_positive(bank_account, amount, expected_result):

    assert bank_account.withdraw(amount) == expected_result


@pytest.mark.bank_account
@pytest.mark.parametrize("amount, expected_result",
                         [
                             (56000, ValueError),
                             ("1231", TypeError)
                         ])
def test_withdraw_negative(bank_account, amount, expected_result):

    with pytest.raises(expected_result):
        bank_account.withdraw(amount)


@pytest.mark.bank_account
@pytest.mark.parametrize("amount, expected_result",
                         [
                             (0, ValueError),
                             (-1000, ValueError)
                         ])
def test_withdraw_bound(bank_account, amount, expected_result):

    with pytest.raises(expected_result):
        bank_account.withdraw(amount)