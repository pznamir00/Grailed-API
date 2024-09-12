from typing import Tuple
from categories import Departments, Conditions, Locations, Markets
from facets import Facets
from .list_service import ListService
from .retrieve_service import RetrieveService


class Client:
    list_service = ListService()
    retrieve_service = RetrieveService()

    def retrieve(self, key: str):
        response = self.retrieve_service.send_request(key)
        data = self.retrieve_service.parse_response(response)
        return data

    def list(
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
        facets: Tuple[Facets, ...] = list_service.get_all_facets(),
        verbose=False,
    ):
        self.list_service.validate_categories_and_sizes(categories, sizes)

        facet_names = self.list_service.enums_to_params("{}", facets)
        cat_params = self.list_service.enums_to_params("category_path:{}", categories)
        des_params = self.list_service.enums_to_params("designers.name:{}", designers)
        cond_params = self.list_service.enums_to_params("condition:{}", conditions)
        mar_params = self.list_service.enums_to_params("strata:{}", markets)
        loc_params = self.list_service.enums_to_params("location:{}", locations)
        siz_params = self.list_service.enums_to_params("category_size:{}", sizes)

        params = self.list_service.create_list_params(
            cat_params,
            des_params,
            cond_params,
            mar_params,
            loc_params,
            siz_params,
            facet_names,
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

        _requests = self.list_service.get_payload_requests(sold, non_sold, params)
        response = self.list_service.send_request({"requests": _requests})
        items = self.list_service.parse_response(response)
        return items
