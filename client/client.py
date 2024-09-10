from typing import Any
import json
import requests  # pylint: disable=import-error
from client.categories import Department
from settings import BASE_PRODUCTS_URL


class Client:
    def __send_request(self, url: str, data: Any):
        return requests.post(
            url,
            data=json.dumps(data),
            headers=self.__get_request_headers(),
        )

    def __get_request_headers(self):
        return {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/x-www-form-urlencoded",
            "x-algolia-api-key": "bc9ee1c014521ccf312525a4ef324a16",
            "x-algolia-application-id": "MNRWEFSS2Q",
        }

    def fetch_products(
        self,
        categories=tuple(),
        designers=tuple(),
        sold=True,
        non_sold=True,
        department=Department.MENSWEAR,
        query_search="",
        page=1,
        hits_per_page=40,
        price_from=0,
        price_to=1_000_000,
        max_values_per_facet=100,
        facets=(
            "category_path",
            "department",
            "category_size",
            "designers.name",
            "price_i",
            "condition",
            "location",
            "badges",
            "strata",
        ),
    ):
        category_params = [f'"category_path:{cat}"' for cat in categories]
        designer_params = [f'"designers.name:{des}"' for des in designers]

        params = f'analytics=true\
            &clickAnalytics=true\
            &enableABTest=false\
            &enablePersonalization=false\
            &facetFilters=[[{",".join(category_params)}],[{",".join(designer_params)}],["department:{department}"]]\
            &facets=[{",".join(facets)}]\
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

        reqs = []
        if non_sold:
            reqs.append({"indexName": "Listing_production", "params": params})
        if sold:
            reqs.append({"indexName": "Listing_sold_production", "params": params})

        result = self.__send_request(BASE_PRODUCTS_URL, {"requests": reqs})
        data = json.loads(result.content)
        items = [j for i in data["results"] for j in i["hits"]]
        return items
