from json import JSONDecodeError
import json
from typing import Dict
from requests import Response


class HttpError(Exception):
    def __init__(self, response: Response):
        code = response.status_code
        message = ''

        try:
            content = response.json()

            if self.__are_algolia_credentials_missing_or_invalid(content):
                # Invalid Algolia credentials error
                message = f"Your X_ALGOLIA_API_KEY or X_ALGOLIA_APP_ID is invalid or missing"
            else:
                # JSON response, format to show
                message = self.__format_json_content(content)
        except JSONDecodeError:
            message = response.content
        finally:
            super().__init__(f"Http returned an error. Status {code}; Message: {message}")
    
    def __format_json_content(self, content: Dict):
        return json.dumps(content, indent=4)

    def __are_algolia_credentials_missing_or_invalid(self, content: str):
        return content == {
            "message": "Invalid Application-ID or API key",
            "status": 403
        }