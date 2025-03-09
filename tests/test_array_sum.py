from main import Array
import pytest


@pytest.mark.parametrize("a, b, c , d ,e , expected",
                         [
                            (1, 2, 3, 4, 5, 15),
                            (1.2, 2, 3.8, 4, 5, 16),
                            (-1, -2, -3, -4, -5, -15),
                            (1, -2, -3, 4, 5, 5)
                         ])
def test_array_sum_positive(a, b, c , d , e, expected):

    lst = Array(a, b, c, d, e)

    assert lst.sum() == expected


@pytest.mark.parametrize("a, b, c , d ,e , expected",
                         [
                             (1, "2", 3, "4", 5, TypeError),
                             (1, 2, [1, 2], 4, 5, TypeError),
                             (1, 2, False, 4, 5, TypeError)
                         ])
def test_array_sum_negative(a, b, c, d, e, expected):
    lst = Array(a, b, c, d, e)
    with pytest.raises(expected):

        lst.sum()


def test_array_sum_empty():

    lst = Array()
    expected = 0
    assert lst.sum() == expected