from pydantic.types import List
from pydantic import BaseModel, field_validator


class ModelBooks(BaseModel):
    bookingid: int


    @classmethod
    @field_validator('bookingid')
    def valid_value(cls, value):
        if value == "" or value is None:
            raise ValueError("Value is None")
        else:
            return value
