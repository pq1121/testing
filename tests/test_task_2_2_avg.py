from main1 import average
import pytest

@pytest.mark.parametrize("lst, expected_result",
                         [
                             ([1, 2, 3, 4, 5], 3),
                             ([1, 2, 1, 2, 4], 2),
                             ([1, 1, 1, 1, 1], 1)
                         ])
def test_avg_positive(lst, expected_result):

    assert average(lst) == expected_result

@pytest.mark.parametrize("lst, expected_result",
                         [
                             (["1", 2, 3, 4, 5], TypeError),
                             ([1, 2, "1", 2, 4], TypeError),
                             ([1, None, 1, "", 1], TypeError)
                         ])
def test_avg_negative(lst, expected_result):
    with pytest.raises(expected_result):
        average(lst)

@pytest.mark.parametrize("lst, expected_result",
                         [
                             ([], ValueError),
                             ([''], ValueError)
                         ])
def test_avg_bound(lst, expected_result):
    with pytest.raises(expected_result):
        average(lst)