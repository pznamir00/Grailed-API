import requests
from grailed_api.models import ProductDetails
from grailed_api.settings import LISTINGS_API
from .api_service import ApiService


class ProductsRetrieveService(ApiService):
    """
    Retrieve service that provides single product lookup utils
    """

    def send_request(self, key: str, verbose: bool):  # pylint: disable=arguments-differ
        return self._session.get(f"{LISTINGS_API}/{key}", verbose=verbose)

    def parse_response(self, response: requests.Response) -> ProductDetails:
        return super().parse_response(response)["data"]
