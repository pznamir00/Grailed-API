from unittest.mock import MagicMock, patch
from enums.categories import Bottoms, Tops
from services.products_list_service import ProductsListService
from settings import SEARCH_URL


class TestProductsListService:
    def test_parse_response_returns_hits(self):
        response = MagicMock(
            json=lambda: {
                "results": [{"hits": [{"hit": 1}, {"hit": 2}]}, {"hits": [{"hit": 3}]}]
            }
        )
        service = ProductsListService()
        data = service.parse_response(response)
        assert data == [{"hit": 1}, {"hit": 2}, {"hit": 3}]

    def test_send_request_calls_session_post(self):
        service = ProductsListService()
        service._session.post = MagicMock(  # pylint: disable=protected-access
            return_value=None
        )
        service.send_request(data={}, verbose=True)
        service._session.post.assert_called_with(  # pylint: disable=protected-access
            SEARCH_URL, data={}, verbose=True
        )

    def test_get_all_facets_returns_all_facets(self):
        service = ProductsListService()
        facets = service.get_all_facets()
        assert len(facets) == 9

    @patch("services.products_list_service.warnings.warn")
    def test_validate_categories_and_sizes_shows_warning_if_size_does_not_match_to_category(
        self, warn: MagicMock
    ):
        service = ProductsListService()
        service.validate_categories_and_sizes(
            [Bottoms.CASUAL_PANTS],
            [Tops.sizes.L, Bottoms.sizes._27],  # pylint: disable=protected-access
        )
        warn.assert_called_once()
        info = warn.call_args[0][0]
        assert "tops.l" in info
        assert "bottoms.27" not in info

    def test_get_payload_requests_returns_requests(self):
        service = ProductsListService()
        res = service.get_payload_requests(sold=True, on_sale=False, params="params")
        assert res == [{"indexName": "Listing_sold_production", "params": "params"}]
