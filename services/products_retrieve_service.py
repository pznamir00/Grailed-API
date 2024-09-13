import requests
from settings import LISTINGS_API
from .api_service import ApiService


class ProductsRetrieveService(ApiService):
    """
    Retrieve service that provides single product lookup utils
    """

    def send_request(self, key: str):  # pylint: disable=arguments-differ
        return requests.get(
            f"{LISTINGS_API}/{key}",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                      AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            },
            timeout=30,
        )

    def parse_response(self, response: requests.Response):
        return super().parse_response(response)["data"]
