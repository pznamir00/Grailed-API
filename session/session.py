import json
from pprint import pprint
from typing import Dict, Optional
from requests import Response, Session
from exceptions import HttpError


class GrailedSession(Session):
    def get(self, *args, verbose=False, **kwargs):
        kwargs["verbose"] = verbose
        return super().get(*args, **kwargs)

    def post(self, *args, verbose=False, **kwargs):
        kwargs["verbose"] = verbose
        return super().post(*args, **kwargs)

    def request(self, method, url, *args, **kwargs):
        headers, data = kwargs.get("headers", {}), kwargs.get("data")

        kwargs.update(
            {
                "headers": self.__add_needed_headers(headers),
                "data": self.__stringify_data_if_needed(data),
                "timeout": 30,
            }
        )

        if kwargs["verbose"]:
            self.__debug_request(method, url, **kwargs)

        del kwargs["verbose"]
        response = super().request(method, url, *args, **kwargs)
        self.__capture_error(response)

        return response

    def __debug_request(self, method: str, url: str, headers: Dict, data: Dict, **_):
        print("HTTP Request:")
        pprint(
            {
                "method": method,
                "url": url,
                "headers": headers,
                "data": data,
            }
        )

    def __capture_error(self, response: Response):
        if response.status_code < 400:
            return

        raise HttpError(response)

    def __stringify_data_if_needed(self, data: Optional[Dict]):
        return json.dumps(data) if data else None

    def __add_needed_headers(self, headers: dict):
        headers.update(
            {
                "accept": "*/*",
                "content-type": "application/x-www-form-urlencoded",
                "x-algolia-api-key": "bc9ee1c014521ccf312525a4ef324a16",
                "x-algolia-application-id": "MNRWEFSS2Q",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                      AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
                "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                "sec-ch-ua-mobile": "?0",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
            }
        )
        return headers
