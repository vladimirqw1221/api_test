from faker import Faker

fake = Faker()
class Payloads:


    create_book ={
    "firstname" : fake.first_name(),
    "lastname" : fake.last_name(),
    "totalprice" : 111,
    "depositpaid" : 'true',
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}


    update_author = {
    "firstname" : fake.first_name(),
    "lastname" : fake.last_name()
}