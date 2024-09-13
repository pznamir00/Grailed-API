from json import JSONDecodeError
import json
from requests import Response


class HttpError(Exception):
    def __init__(self, response: Response):
        code = response.status_code

        try:
            # format content string as json object if possible
            content = json.dumps(response.json(), indent=4)
        except JSONDecodeError:
            content = response.content

        super().__init__(f"Http returned an error. Status {code}; Content: {content}")
