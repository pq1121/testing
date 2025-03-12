from main1 import is_palindrome
import pytest

@pytest.mark.parametrize("s, expected_result",
                         [
                             ('строкаакортс', True),
                             ('tyyt', True),
                             ('неттен', True)
                         ])
def test_task1_palindrome_positive(s, expected_result):

    assert is_palindrome(s) == expected_result

@pytest.mark.parametrize("s, expected_result",
                         [
                             ('42342342', False),
                             ('ffw', False),
                             ('нетт', False)
                         ])
def test_task1_palindrome_negative(s, expected_result):

    assert is_palindrome(s) == expected_result

@pytest.mark.parametrize("s, expected_result",
                         [
                             ('', False),
                             ('1', True),
                             ('b', True)
                         ])
def test_task1_palindrome_bound(s, expected_result):

    assert is_palindrome(s) == expected_result