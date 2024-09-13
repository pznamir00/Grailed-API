import json
from typing import List
from requests import Response
import requests
from settings import BRANDS_URL
from .api_service import ApiService


class BrandsListService(ApiService):
    """
    Brands service that provides brands list http lookup utils
    """

    def parse_response(self, response: Response) -> List:
        return super().parse_response(response)["facetHits"]

    def send_request(self, query: str) -> Response:  # pylint: disable=arguments-differ
        return requests.post(
            BRANDS_URL,
            data=json.dumps({"facetQuery": query}),
            headers={
                "accept": "*/*",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
                "content-type": "application/x-www-form-urlencoded",
                "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                "sec-ch-ua-mobile": "?0",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "x-algolia-api-key": "bc9ee1c014521ccf312525a4ef324a16",
                "x-algolia-application-id": "MNRWEFSS2Q",
            },
            timeout=30,
        )
