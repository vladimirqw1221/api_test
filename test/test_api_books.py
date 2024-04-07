from config.base_test import BaseTest
import allure
import pytest


@allure.epic("Test Api books")
@allure.feature("E2E test")
class TestApiBooks(BaseTest):

    @allure.title("Get all books")
    @pytest.mark.development
    def test_get_all_books(self):
        self.books_api.get_all_books()

    @allure.title("Get param for one book")
    @pytest.mark.development
    def test_get_one_book(self):
        self.books_api.one_param_book()

    @allure.title("Create new book")
    @pytest.mark.development
    def test_create_book(self):
        self.books_api.create_book()

    @allure.title("Update all info for book")
    @pytest.mark.development
    def test_update_book_by_id(self):
        self.books_api.update_books_by_id()

    @allure.title("Update author info")
    @pytest.mark.development
    def test_update_author_book(self):
        self.books_api.update_author()

    @allure.title("Delete book by ID")
    @pytest.mark.development
    def test_delete_book(self):
        self.books_api.delete_books()
