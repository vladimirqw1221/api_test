HOST = "https://restful-booker.herokuapp.com"


class Endpoint:
    booking = f"{HOST}/booking/"
    get_booking_by_id = lambda self, id: f"{HOST}/booking/{id}"
