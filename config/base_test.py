from service.books.books_api import BooksApi
import pytest

class BaseTest:
    books_api: BooksApi

    @pytest.fixture(autouse=True)
    def setup_model(self, request, book_api):
        request.cls.books_api = BooksApi()
