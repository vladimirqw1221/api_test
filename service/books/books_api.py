import allure
import requests
from service.books.endpount import Endpoint
from config.cookie import Cookie
from config.headers import Headers
from service.books.payloads import Payloads
from utils.hellper import Helper
from service.books.models.models_books import ModelBooks
from service.books.models.models_book_is_id import ParamBookId
from service.books.models.create_books_models import CreateBooks
from pydantic import BaseModel


class BooksApi(Helper):

    def __init__(self):
        super().__init__()
        self.endpoint = Endpoint()
        self.cookie = Cookie()
        self.headers = Headers()
        self.payloads = Payloads()

    @allure.step("Get all books list")
    def get_all_books(self) -> BaseModel:
        response = requests.get(
            url=self.endpoint.booking,
            headers=self.headers.basic,

        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = ModelBooks(**response.json()[0])
        return model

    @allure.step("Get param for one  book")
    def one_param_book(self) -> BaseModel:
        response = requests.get(
            url=self.endpoint.get_booking_by_id(self.create_book().bookingid),
            headers=self.headers.basic
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = ParamBookId(**response.json())
        return model

    @allure.step("Create book")
    def create_book(self) -> BaseModel:
        response = requests.post(
            url=self.endpoint.booking,
            headers=self.headers.basic,
            json=self.payloads.create_book
        )
        assert response.status_code == 200, response.json()
        with allure.step("Create book data"):
            self.attach_response(response.json())
        model = CreateBooks(**response.json())
        return model

    @allure.step("Update book")
    def update_books_by_id(self) -> BaseModel:
        response = requests.put(
            url=self.endpoint.get_booking_by_id(self.create_book().bookingid),
            headers=self.headers.basic,
            cookies=self.cookie.init_auth,
            json=self.payloads.create_book

        )
        assert response.status_code == 200, response.status_code
        self.attach_response(response.json())
        model = ParamBookId(**response.json())
        return model

    @allure.step("Update author")
    def update_author(self) -> BaseModel:
        response = requests.patch(
            url=self.endpoint.get_booking_by_id(self.create_book().bookingid),
            headers=self.headers.basic,
            cookies=self.cookie.init_auth,
            json=self.payloads.update_author

        )
        assert response.status_code == 200, response.status_code
        self.attach_response(response.json())
        model = ParamBookId(**response.json())
        return model

    @allure.step("Delete book by id ")
    def delete_books(self) -> None:
        response = requests.delete(
            url=self.endpoint.get_booking_by_id(self.create_book().bookingid),
            headers=self.headers.basic,
            cookies=self.cookie.init_auth

        )
        assert response.status_code == 201
        self.attach_response(response.text)
