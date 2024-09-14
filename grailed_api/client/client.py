from typing import Iterable
from grailed_api.enums import Departments, Conditions, Locations, Markets
from grailed_api.facets import Facets
from grailed_api.services import ProductsListService, ProductsRetrieveService, BrandsListService
from grailed_api.settings import X_ALGOLIA_KEYS


class Client:
    """
    Main Client class that is interface of whole system. It
    provides all functionalities for looking for products and brands
    """

    __products_list_service = ProductsListService()
    __products_retrieve_service = ProductsRetrieveService()
    __brands_list_service = BrandsListService()

    def __init__(self, x_algolia_api_key: str, x_algolia_app_id: str):
        X_ALGOLIA_KEYS.update(
            {
                "API_KEY": x_algolia_api_key,
                "APP_ID": x_algolia_app_id,
            }
        )

    def find_brands(self, query: str, verbose=False):
        """Finds brands by provided query keyword
        and returns them in a list

        Args:
            query (str): keyword to search a brand for
            verbose (bool, optional): show htp request. Defaults to False.

        Returns:
            List: list with brand objects
        """
        response = self.__brands_list_service.send_request(query, verbose)
        brands = self.__brands_list_service.parse_response(response)
        return brands

    def find_product_by_id(
        self, id: str, verbose=False
    ):  # pylint: disable=redefined-builtin
        """searches a product by provided id

        Args:
            id (str): product id
            verbose (bool, optional): show htp request. Defaults to False.

        Returns:
            Object: product object
        """
        response = self.__products_retrieve_service.send_request(id, verbose)
        data = self.__products_retrieve_service.parse_response(response)
        return data

    def find_products(  # pylint: disable=too-many-locals, disable=too-many-arguments
        self,
        sold=True,
        on_sale=True,
        staff_pick=False,
        department=Departments.MENSWEAR,
        query_search="",
        page=1,
        hits_per_page=40,
        price_from=0,
        price_to=1_000_000,
        categories: Iterable = (),
        sizes: Iterable = (),
        designers: Iterable[str] = (),
        conditions: Iterable[Conditions] = (),
        markets: Iterable[Markets] = (),
        locations: Iterable[Locations] = (),
        max_values_per_facet=100,
        facets: Iterable[Facets] = __products_list_service.get_all_facets(),
        verbose=False,
    ):
        """Searches list of products with specified filters. Returns a list
        of this products.

        Args:
            sold (bool, optional): include sold products. Defaults to True.
            on_sale (bool, optional): include products on sale. Defaults to True.
            staff_pick (bool, optional): get only products that have been marked by staff. Defaults to False.
            department (Departments, optional): department, menswear or womenwear. Defaults to Departments.MENSWEAR.
            query_search (str, optional): filter by keyword. Defaults to "".
            page (int, optional): page index. Defaults to 1.
            hits_per_page (int, optional): products number in one page. Defaults to 40.
            price_from (int, optional): filter by min price. Defaults to 0.
            price_to (int, optional): filter by max price. Defaults to 1_000_000.
            categories (Iterable[Category], optional): filter by categories. Defaults to ().
            sizes (Iterable[Size], optional): filter by sizes. Defaults to ().
            designers (Iterable[str], optional): filter by designer names. Defaults to ().
            conditions (Iterable[Condition], optional): filter by conditions. Defaults to ().
            markets (Iterable[Markets], optional): filter by markets. Defaults to ().
            locations (Iterable[Locations], optional): filter by locations. Defaults to ().
            max_values_per_facet (int, optional): Defaults to 100.
            facets (Iterable[Facets], optional): Defaults to all facets.
            verbose (bool, optional): show htp request. Defaults to False.

        Returns:
            List: found products
        """

        self.__products_list_service.validate_categories_and_sizes(categories, sizes)
        params = self.__products_list_service.create_params_string(
            categories,
            sizes,
            designers,
            conditions,
            markets,
            locations,
            facets,
            department,
            staff_pick,
            hits_per_page,
            max_values_per_facet,
            price_from,
            price_to,
            page,
            query_search,
        )

        _requests = self.__products_list_service.get_payload_requests(
            sold, on_sale, params
        )
        response = self.__products_list_service.send_request(
            {"requests": _requests}, verbose
        )
        products = self.__products_list_service.parse_response(response)
        return products
