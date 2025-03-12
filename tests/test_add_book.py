from main1 import Library
import pytest

@pytest.mark.parametrize("book, expected",
                         [
                             ("book1", True),
                             ("book2", True),
                             ("Not Book1", True)
                         ])
def test_add_book_positive(book, expected):
    lib = Library()
    lib.add_book(book)

    assert lib.find_book(book) == expected

@pytest.mark.parametrize("book, expected",
                         [
                             (312323, TypeError),
                             (None, TypeError),
                             (["book5"], TypeError),
                             ([], TypeError)
                         ])
def test_add_book_negative(book, expected):
    lib = Library()

    with pytest.raises(expected):
        lib.add_book(book)

@pytest.mark.parametrize("book, expected",
                         [
                             ("", ValueError)
                         ])
def test_add_book_bound(book, expected):
    lib = Library()

    with pytest.raises(expected):
        lib.add_book(book)