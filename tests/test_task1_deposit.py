from main1 import BankAccount
import pytest


@pytest.fixture()
def bank_account():
    return BankAccount()


@pytest.mark.bank_account
@pytest.mark.parametrize("amount, expected_result",
                         [
                             (50000, 50000),
                             (1000, 1000),
                             (10000, 10000)
                         ])
def test_deposit_positive(bank_account, amount, expected_result):

    assert bank_account.deposit(amount) == expected_result


@pytest.mark.bank_account
@pytest.mark.parametrize("amount, expected_result",
                         [
                             (-1000, ValueError),
                             ("0", TypeError)
                         ])
def test_deposit_negative(bank_account, amount, expected_result):

    with pytest.raises(expected_result):
        bank_account.deposit(amount)


@pytest.mark.bank_account
@pytest.mark.parametrize("amount, expected_result",
                         [
                             (0, ValueError)
                         ])
def test_deposit_bound(bank_account, amount, expected_result):

    with pytest.raises(expected_result):
        bank_account.deposit(amount)