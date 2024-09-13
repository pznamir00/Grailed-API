from unittest.mock import MagicMock
from services.brands_list_service import BrandsListService
from settings import BRANDS_URL


class TestBrandsListService:
    def test_parse_response_returns_hits(self):
        response = MagicMock(json=lambda: {"facetHits": [{"facet": 1}]})
        service = BrandsListService()
        data = service.parse_response(response)
        assert data == [{"facet": 1}]

    def test_send_request_calls_session_post(self):
        service = BrandsListService()
        service._session.post = MagicMock(  # pylint: disable=protected-access
            return_value=None
        )
        service.send_request(query="q", verbose=True)
        service._session.post.assert_called_with(  # pylint: disable=protected-access
            BRANDS_URL, data={"facetQuery": "q"}, verbose=True
        )
