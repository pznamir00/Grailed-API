from typing import Tuple
from categories import Departments, Conditions, Locations, Markets
from facets import Facets
from services import ListService, RetrieveService, BrandsService


class Client:
    __list_service = ListService()
    __retrieve_service = RetrieveService()
    __brands_service = BrandsService()

    def find_brands(self, query: str):
        response = self.__brands_service.send_request(query)
        brands = self.__brands_service.parse_response(response)
        print(brands)

    def find_product_by_id(self, id: str):  # pylint: disable=redefined-builtin
        response = self.__retrieve_service.send_request(id)
        data = self.__retrieve_service.parse_response(response)
        return data

    def find_products(  # pylint: disable=too-many-locals, disable=too-many-arguments
        self,
        sold=True,
        non_sold=True,
        staff_pick=False,
        department=Departments.MENSWEAR,
        query_search="",
        page=1,
        hits_per_page=40,
        price_from=0,
        price_to=1_000_000,
        categories: Tuple = (),
        sizes: Tuple = (),
        designers: Tuple[str, ...] = (),
        conditions: Tuple[Conditions, ...] = (),
        markets: Tuple[Markets, ...] = (),
        locations: Tuple[Locations, ...] = (),
        max_values_per_facet=100,
        facets: Tuple[Facets, ...] = __list_service.get_all_facets(),
        verbose=False,
    ):
        self.__list_service.validate_categories_and_sizes(categories, sizes)
        params = self.__list_service.create_list_params(
            categories,
            sizes,
            designers,
            conditions,
            markets,
            locations,
            facets,
            department.value,
            staff_pick,
            hits_per_page,
            max_values_per_facet,
            price_from,
            price_to,
            page,
            query_search,
        )

        if verbose:
            print("Params", params)

        _requests = self.__list_service.get_payload_requests(sold, non_sold, params)
        response = self.__list_service.send_request({"requests": _requests})
        items = self.__list_service.parse_response(response)
        return items
