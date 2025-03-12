from main1 import Library
import pytest

@pytest.mark.parametrize("book, expected",
                         [
                             ("book1", False),
                             ("book2", False),
                             ("Not Book1", False)
                         ])
def test_remove_book_positive(book, expected):
    lib = Library()
    lib.add_book(book)
    lib.remove_book(book)
    assert lib.find_book(book) == expected

@pytest.mark.parametrize("book, expected",
                         [
                             (312323, ValueError),
                             (None, ValueError),
                             (["book5"], TypeError),
                             ([], TypeError)
                         ])
def test_remove_book_negative(book, expected):
    lib = Library()

    with pytest.raises(expected):
        lib.remove_book(book)

@pytest.mark.parametrize("book, expected",
                         [
                             ("", ValueError)
                         ])
def test_removed_book_bound(book, expected):
    lib = Library()

    with pytest.raises(expected):
        lib.remove_book(book)