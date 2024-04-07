from pydantic import BaseModel, field_validator
from service.books.models.models_book_is_id import ParamBookId


class CreateBooks(BaseModel):
    bookingid: int
    booking: ParamBookId


    @classmethod
    @field_validator('bookingid', 'booking')
    def empty_date_in_create_book(cls, value):
        if value == "" or value is None:
            raise ValueError("This date is none")
        else:
            return value




