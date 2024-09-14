from grailed_api.exceptions.http_error import HttpError
from grailed_api.exceptions.wrong_enum_type_error import (
    WrongCategoryTypeError,
    WrongSizeTypeError,
)
import pytest
from grailed_api.client import Client
from grailed_api.enums.categories import Tops
from grailed_api.enums import Locations, Conditions, Markets


class TestClient:
    def test_find_brands_returns_brands_matching_query(self):
        client = Client()
        brands = client.find_brands(query="elem")
        assert brands
        matching = ["e" in brand["value"].lower() for brand in brands]
        assert all(matching)

    def test_find_product_by_id_returns_product_with_id(self):
        client = Client()
        product = client.find_product_by_id(id="66849368")
        assert product["id"] == 66849368

    def test_find_products_throws_error_if_wrong_category_is_provided(self):
        with pytest.raises(WrongCategoryTypeError):
            client = Client()
            client.find_products(categories=(Tops,))

    def test_find_products_throws_error_if_wrong_size_is_provided(self):
        with pytest.raises(WrongSizeTypeError):
            client = Client()
            client.find_products(sizes=(Tops.sizes,))

    def test_find_products_returns_products_matching_filters(self):
        client = Client()
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
