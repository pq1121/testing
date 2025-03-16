from main1 import DiscountCalculator
import pytest


@pytest.fixture()
def discount_calc():

    return {
        "calc": DiscountCalculator(),
        "price": 10000
    }


@pytest.mark.discount_calculator
@pytest.mark.parametrize("amount, expected_result",
                         [
                             (15, 8500),
                             (30, 7000),
                             (75, 2500),
                             (15.15, 8485),
                         ])
def test_logger_positive(discount_calc, amount, expected_result):

    assert discount_calc['calc'].apply_discount(discount_calc["price"], amount) == expected_result


@pytest.mark.discount_calculator
@pytest.mark.parametrize("amount, expected_result",
                         [
                             (-10, ValueError),
                             ("10", TypeError),
                             ("", TypeError)
                         ])
def test_logger_negative(discount_calc, amount, expected_result):

    with pytest.raises(expected_result):
        discount_calc['calc'].apply_discount(discount_calc["price"], amount)


@pytest.mark.discount_calculator
@pytest.mark.parametrize("amount, expected_result",
                         [
                             (0, ValueError),
                             (100, ValueError),
                             (101, ValueError)
                         ])
def test_logger_bound(discount_calc, amount, expected_result):

    with pytest.raises(expected_result):
        discount_calc['calc'].apply_discount(discount_calc["price"], amount)