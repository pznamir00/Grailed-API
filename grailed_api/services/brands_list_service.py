from typing import List
from requests import Response
from grailed_api.models import Brand
from grailed_api.settings import BRANDS_URL
from .api_service import ApiService


class BrandsListService(ApiService):
    """
    Brands service that provides brands list http lookup utils
    """

    def parse_response(self, response: Response) -> List[Brand]:
        return super().parse_response(response)["facetHits"]

    def send_request(  # pylint: disable=arguments-differ
        self, query: str, verbose: bool
    ) -> Response:
        return self._session.post(
            BRANDS_URL, data={"facetQuery": query}, verbose=verbose
        )
