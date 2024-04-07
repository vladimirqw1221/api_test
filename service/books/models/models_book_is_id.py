from pydantic import BaseModel, field_validator
from service.books.models.booking_date import BooksDate


class ParamBookId(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BooksDate
    additionalneeds: str

    @classmethod
    @field_validator(
        'firstname',
        'lastname',
        'totalprice',
        'depositpaid',
        'bookingdates',
        'additionalneeds'
    )
    def empy_all_fields(cls, value):
        if value == "" or value is None:
            raise ValueError("This fields is none ")
        else:
            return value
