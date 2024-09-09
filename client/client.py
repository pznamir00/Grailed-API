from typing import Any
import json
import requests
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

    def fetch_products(self):
        data = {
            "requests": [
                {
                    "indexName": "Listing_production",
                    "params": "analytics=true&clickAnalytics=true&enableABTest=false&enablePersonalization=false&facetFilters=%5B%5B%22category_path%3Atops.button_ups%22%2C%22category_path%3Atops.jerseys%22%2C%22category_path%3Atops.long_sleeve_shirts%22%2C%22category_path%3Atops.polos%22%2C%22category_path%3Atops.short_sleeve_shirts%22%2C%22category_path%3Atops.sleeveless%22%2C%22category_path%3Atops.sweaters_knitwear%22%2C%22category_path%3Atops.sweatshirts_hoodies%22%5D%2C%5B%22department%3Amenswear%22%5D%5D&facets=%5B%22category_path%22%2C%22department%22%2C%22category_size%22%2C%22designers.name%22%2C%22price_i%22%2C%22condition%22%2C%22location%22%2C%22badges%22%2C%22strata%22%5D&filters=&getRankingInfo=true&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&highlightPreTag=%3Cais-highlight-0000000000%3E&hitsPerPage=40&maxValuesPerFacet=100&numericFilters=%5B%22price_i%3E%3D0%22%2C%22price_i%3C%3D1000000%22%5D&page=3&personalizationImpact=0&query=&tagFilters=&userToken=1ebfc4e8-199c-45e7-aaff-d3749b169ea1",
                },
                {
                    "indexName": "Listing_sold_production",
                    "params": "analytics=true&clickAnalytics=true&enableABTest=false&enablePersonalization=false&facetFilters=%5B%5B%22category_path%3Atops.button_ups%22%2C%22category_path%3Atops.jerseys%22%2C%22category_path%3Atops.long_sleeve_shirts%22%2C%22category_path%3Atops.polos%22%2C%22category_path%3Atops.short_sleeve_shirts%22%2C%22category_path%3Atops.sleeveless%22%2C%22category_path%3Atops.sweaters_knitwear%22%2C%22category_path%3Atops.sweatshirts_hoodies%22%5D%2C%5B%22department%3Amenswear%22%5D%5D&facets=%5B%22category_path%22%2C%22department%22%2C%22category_size%22%2C%22designers.name%22%2C%22price_i%22%2C%22condition%22%2C%22location%22%2C%22badges%22%2C%22strata%22%5D&filters=&getRankingInfo=true&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&highlightPreTag=%3Cais-highlight-0000000000%3E&hitsPerPage=40&maxValuesPerFacet=100&numericFilters=%5B%22price_i%3E%3D0%22%2C%22price_i%3C%3D1000000%22%5D&page=3&personalizationImpact=0&query=&tagFilters=&userToken=1ebfc4e8-199c-45e7-aaff-d3749b169ea1",
                },
            ],
        }
        result = self.__send_request(BASE_PRODUCTS_URL, data)
        data = json.loads(result.content)
        items = [j for i in data["results"] for j in i["hits"]]
        return items
