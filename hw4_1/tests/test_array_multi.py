from main import Array
import pytest


@pytest.mark.parametrize("a, b, c, expected",
                         [
                            (1, 2, 3, 6),
                            (1.2, 2, 3.8, 9.12),
                            (-1, -2, -3, -6),
                            (1, -2, -3, 6)
                         ])
def test_array_multi_positive(a, b, c, expected):
    lst = Array(a, b, c)

    assert lst.multiply() == expected


@pytest.mark.parametrize("a, b, c, d, e, expected",
                         [
                             (1, "2", 3, "4", 5, TypeError),
                             (1, 2, [1, 2], 4, 5, TypeError),
                             (1, 2, False, 4, 5, TypeError)
                         ])
def test_array_multi_negative(a, b, c, d, e, expected):
    lst = Array(a, b, c, d, e)

    with pytest.raises(expected):
        lst.multiply()


def test_array_multi_empty():
    lst = Array()
    expected = 1

    assert lst.multiply() == expected