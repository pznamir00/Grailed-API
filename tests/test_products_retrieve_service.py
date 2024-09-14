from unittest.mock import MagicMock
from services.products_retrieve_service import ProductsRetrieveService
from grailed_api.settings import LISTINGS_API


class TestProductsRetrieveService:
    def test_parse_response_returns_data(self):
        response = MagicMock(json=lambda: {"data": {"product": {}}})
        service = ProductsRetrieveService()
        data = service.parse_response(response)
        assert data == {"product": {}}

    def test_send_request_calls_session_get(self):
        service = ProductsRetrieveService()
        service._session.get = MagicMock(  # pylint: disable=protected-access
            return_value=None
        )
        service.send_request(key="12345", verbose=True)
        service._session.get.assert_called_with(  # pylint: disable=protected-access
            f"{LISTINGS_API}/12345", verbose=True
        )
