import allure
import json
from allure_commons.types import AttachmentType
from requests import Response


class Helper:

    def attach_response(self, response: Response | str) -> None:
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)
