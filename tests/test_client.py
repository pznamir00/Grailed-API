import pytest
from client import Client
from enums.categories import Tops
from enums import Locations, Conditions, Markets


class TestClient:
    @pytest.fixture(scope="session")
    def x_alg_api_key(self, pytestconfig):
        return pytestconfig.getoption("x_algolia_api_key")

    @pytest.fixture(scope="session")
    def x_alg_app_id(self, pytestconfig):
        return pytestconfig.getoption("x_algolia_app_id")

    def test_find_brands_returns_brands_matching_query(
        self, x_alg_api_key: str, x_alg_app_id: str
    ):
        client = Client(x_alg_api_key, x_alg_app_id)
        brands = client.find_brands(query="elem")
        assert brands
        matching = ["e" in brand["value"].lower() for brand in brands]
        assert all(matching)

    def test_find_product_by_id_returns_product_with_id(
        self, x_alg_api_key: str, x_alg_app_id: str
    ):
        client = Client(x_alg_api_key, x_alg_app_id)
        product = client.find_product_by_id(id="66849368")
        assert product["id"] == 66849368

    def test_find_products_returns_products_matching_filters(
        self, x_alg_api_key: str, x_alg_app_id: str
    ):
        client = Client(x_alg_api_key, x_alg_app_id)
        products = client.find_products(
            sold=False,
            query_search="xx",
            categories=[Tops.BUTTON_UPS, Tops.JERSEYS],
            sizes=[Tops.sizes.L, Tops.sizes.M, Tops.sizes.S],
            price_from=100,
            price_to=200,
            conditions=[Conditions.IS_GENTLY_USED, Conditions.IS_NEW],
            markets=[Markets.BASIC, Markets.GRAILED],
            locations=[Locations.ASIA, Locations.EUROPE],
            hits_per_page=5,
        )

        for product in products:
            assert not product["sold"]
            assert product["category_path"] in ("tops.button_ups", "tops.jerseys")
            assert product["category_size"] in ("tops.s", "tops.m", "tops.l")
            assert product["condition"] in ("is_gently_used", "is_new")
            assert product["marketplace"] in ("basic", "grailed")
            assert product["location"] in ("Europe", "Asia")
            assert 100 <= product["price"] <= 200
