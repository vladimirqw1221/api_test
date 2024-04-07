from service.books.books_api import BooksApi
import pytest

@pytest.fixture(scope='module', autouse=True)
def book_api():
    return BooksApi()


