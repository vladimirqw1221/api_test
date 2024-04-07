import os
import requests
from dotenv import load_dotenv


load_dotenv()


class Cookie:
    HOST = "https://restful-booker.herokuapp.com"

    @property
    def init_auth(self):
        headers = {'Content-Type': 'application/json'}
        data = {
            "username": os.getenv('USER_NAME'),
            "password": os.getenv('PASSWORD')
        }
        response = requests.post(
            url=f"{self.HOST}/auth",
            json=data,
            headers=headers
        )
        assert response.status_code == 200
        assert response.text not in "Bad Request"
        token = response.json()
        return token
