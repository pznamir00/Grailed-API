import json
from warnings import warn
from typing import List, Tuple
from requests import Response
from facets import Facets


class ListService:
    def get_all_facets(self):
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

    def validate_categories_and_sizes(self, categories: Tuple, sizes: Tuple):
        if not categories or not sizes:
            return

        cat_prefixes = [cat.value.split(".")[0] for cat in categories]
        non_matching_sizes = [
            size.value for size in sizes if size.value.split(".")[0] not in cat_prefixes
        ]

        if non_matching_sizes:
            warn(
                f"Sizes {','.join(non_matching_sizes)} don't match any provided category, so they won't be considered in the query"
            )

    def enums_to_params(self, label: str, objects: Tuple):
        return [
            f'"{label.format(obj if isinstance(obj, str) else obj.value)}"'
            for obj in objects
        ]

    def get_payload_requests(self, sold: bool, non_sold: bool, params: str):
        requests = []
        if non_sold:
            requests.append({"indexName": "Listing_production", "params": params})
        if sold:
            requests.append({"indexName": "Listing_sold_production", "params": params})
        return requests

    def get_items_from_response(self, response: Response):
        data = json.loads(response.content)
        return [j for i in data["results"] for j in i["hits"]]

    def get_request_headers(self):
        return {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/x-www-form-urlencoded",
            "x-algolia-api-key": "bc9ee1c014521ccf312525a4ef324a16",
            "x-algolia-application-id": "MNRWEFSS2Q",
        }

    def create_list_params(
        self,
        category_params: List[str],
        designer_params,
        condition_params,
        market_params,
        location_params,
        size_params,
        facet_names: List[str],
        department: str,
        staff_pick: bool,
        hits_per_page: int,
        max_values_per_facet: int,
        price_from: int,
        price_to: int,
        page: int,
        query_search: str,
    ):
        return f'analytics=true\
&clickAnalytics=true\
&enableABTest=false\
&enablePersonalization=false\
&facetFilters=[\
[{",".join(category_params)}],\
[{",".join(designer_params)}],\
[{",".join(condition_params)}],\
[{",".join(market_params)}],\
[{",".join(location_params)}],\
[{",".join(size_params)}],\
["department:{department}"],\
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
