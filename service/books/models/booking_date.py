from datetime import datetime

from pydantic import BaseModel, field_validator
from pydantic.types import PastDate


class BooksDate(BaseModel):
    checkin: PastDate
    checkout: datetime

    @classmethod
    @field_validator('checkin', 'checkout')
    def empty_all_date(cls, value):
        if value == "" or value is None:
            raise ValueError("this date is None")
        else:
            return value
