import warnings
from typing import Any, Dict, Iterable, List
import requests
from aenum._enum import EnumType
from grailed_api.enums import Markets, Conditions, Locations, Departments
from grailed_api.exceptions import WrongCategoryTypeError, WrongSizeTypeError
from grailed_api.facets import Facets
from grailed_api.settings import SEARCH_URL
from .api_service import ApiService


class ProductsListService(ApiService):
    """
    List service that provides products list http lookup utils
    """

    def send_request(
        self, data: Any, verbose: bool
    ):  # pylint: disable=arguments-differ
        return self._session.post(SEARCH_URL, data=data, verbose=verbose)

    def parse_response(self, response: requests.Response):
        content = super().parse_response(response)
        return [j for i in content["results"] for j in i["hits"]]

    def get_all_facets(self):
        """Returns all available facets to http request

        Returns:
            Iterable[Facets]: facets list
        """
        return (
            Facets.BADGES,
            Facets.CATEGORY_PATH,
            Facets.CATEGORY_SIZE,
            Facets.CONDITION,
            Facets.DEPARTMENT,
            Facets.DESIGNERS_NAME,
            Facets.LOCATION,
            Facets.PRICE_I,
            Facets.STRATA,
        )

    def validate_categories_and_sizes(self, categories: Iterable, sizes: Iterable):
        self.__validate_categories_and_sizes_are_enum_props(categories, sizes)
        self.__validate_categories_and_sizes_match(categories, sizes)

    def __validate_categories_and_sizes_are_enum_props(self, categories: Iterable, sizes: Iterable):
        """Checks if categories and sizes are fields of enums rather than just enums.
        This validation is needed for prevent a user provide categories e.g just 'Tops'

        Args:
            categories (Iterable[Category]): categories list
            sizes (Iterable[Size]): sizes list
        """
        for category in categories:
            if type(category) is EnumType:
                raise WrongCategoryTypeError(type(category))

        for size in sizes:
            if type(size) is EnumType:
                raise WrongSizeTypeError(type(size))
            

    def __validate_categories_and_sizes_match(self, categories: Iterable, sizes: Iterable):
        """Checks if user provided sizes that match to categories and shows a warning.
        If some size's category is not found in provided categories,
        this size won't be affected.

        Args:
            categories (Iterable[Category]): categories list
            sizes (Iterable[Size]): sizes list
        """
        if not sizes:
            return

        cat_prefixes = [cat.value.split(".")[0] for cat in categories]
        non_matching_sizes = [
            size.value for size in sizes if size.value.split(".")[0] not in cat_prefixes
        ]

        if non_matching_sizes:
            warnings.warn(
                f"Sizes {','.join(non_matching_sizes)} don't match any \
provided category, so they won't be considered in the query"
            )

    def __enums_to_params(self, label: str, objects: Iterable[Any]):
        """Converts objects list to facet parameters format

        Args:
            label (str): field format. Should include place to put object,
                since it will be replaced (e.g. "label:{}")
                objects (Iterable[Any]): objects that are gonna be put to label

        Returns:
            List[str]: list of final labels
        """
        return [
            f'"{label.format(obj if isinstance(obj, str) else obj.value)}"'
            for obj in objects
        ]

    def get_payload_requests(self, sold: bool, on_sale: bool, params: str):
        """Returns parameters requests object (custom Grailed object) that is gonna
            be included to http request. This is limited to products on sale and sold

        Args:
            sold (bool): include sold products
            on_sale (bool): include products on sale
            params (str): Grailed params string

        Returns:
            List[Dict[str, str]]: requests list
        """
        _requests: List[Dict] = []
        if on_sale:
            _requests.append({"indexName": "Listing_production", "params": params})
        if sold:
            _requests.append({"indexName": "Listing_sold_production", "params": params})
        return _requests

    def create_params_string(  # pylint: disable=too-many-locals, disable=too-many-arguments
        self,
        categories: Iterable,
        sizes: Iterable,
        designers: Iterable[str],
        conditions: Iterable[Conditions],
        markets: Iterable[Markets],
        locations: Iterable[Locations],
        facets: Iterable[Facets],
        department: Departments,
        staff_pick: bool,
        hits_per_page: int,
        max_values_per_facet: int,
        price_from: int,
        price_to: int,
        page: int,
        query_search: str,
    ):
        """Created Grailed params string base on provided filters

        Args:
            categories (Iterable[Category], optional): filter by categories.
            sizes (Iterable[Size], optional): filter by sizes.
            designers (Iterable[str], optional): filter by designer names.
            conditions (Iterable[Condition], optional): filter by conditions.
            markets (Iterable[Markets], optional): filter by markets.
            locations (Iterable[Locations], optional): filter by locations.
            facets (Iterable[Facets], optional):
            department (Department): department, menswear or womenwear.
            staff_pick (bool): get only products that have been marked by staff.
            hits_per_page (int): products number in one page.
            max_values_per_facet (int):
            price_from (int): filter by min price.
            price_to (int): filter by max price.
            page (int): page index.
            query_search (str): filter by keyword.

        Returns:
            str: Grailed params string
        """
        facet_names = self.__enums_to_params("{}", facets)
        cat_params = self.__enums_to_params("category_path:{}", categories)
        des_params = self.__enums_to_params("designers.name:{}", designers)
        cond_params = self.__enums_to_params("condition:{}", conditions)
        mar_params = self.__enums_to_params("strata:{}", markets)
        loc_params = self.__enums_to_params("location:{}", locations)
        siz_params = self.__enums_to_params("category_size:{}", sizes)

        return f'analytics=true\
&clickAnalytics=true\
&enableABTest=false\
&enablePersonalization=false\
&facetFilters=[\
[{",".join(cat_params)}],\
[{",".join(des_params)}],\
[{",".join(cond_params)}],\
[{",".join(mar_params)}],\
[{",".join(loc_params)}],\
[{",".join(siz_params)}],\
["department:{department.value}"],\
[{"badges:staff_pick" if staff_pick else ""}]\
]\
&facets=[{",".join(facet_names)}]\
&filters=\
&getRankingInfo=true\
&highlightPostTag=</ais-highlight-0000000000>\
&highlightPreTag=<ais-highlight-0000000000>\
&hitsPerPage={hits_per_page}\
&maxValuesPerFacet={max_values_per_facet}\
&numericFilters=["price_i>={price_from}","price_i<={price_to}"]\
&page={page}\
&personalizationImpact=0\
&query={query_search}\
&tagFilters='
