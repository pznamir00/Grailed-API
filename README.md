# Grailed API

This repository provides most important features when it comes to Grailed API.
This is only for searching objects, since there is no official API, or API key.

## How to install

To install the API, just run `pip install -r requirements.txt` command.
Then you have to provide both `X_ALGOLIA_API_KEY` and `X_ALGOLIA_APPLICATION_ID` keys.
Define them in `settings.py` file. You can get those keys from your browser.

### How to get access keys:

In order to have `X_ALGOLIA_API_KEY` and `X_ALGOLIA_APPLICATION_ID`, do following steps:
- go to https://www.grailed.com/
- click right mouse button
- click "inspect"
- in sidebar, click "Network"
- find keywords "objects?x-algolia-agent" (if you can't find it, refresh the browser)
- in headers of the request, you should find both keys

## How to use

In order to use the features, just import `Client` as in following code

```python
from client import Client

client = Client()
```

Then you are ready to use searching functions


### Methods

- `find_products` - returns products list
    - Parameters:
        - `sold` (bool, optional): include sold products. Defaults to True.
        - `on_sale` (bool, optional): include products on sale. Defaults to True.
        - `staff_pick` (bool, optional): get only products that have been marked by staff. Defaults to False.
        - `department` (Departments, optional): department, menswear or womenwear. Defaults to Departments.MENSWEAR.
        - `query_search` (str, optional): filter by keyword. Defaults to "".
        - `page` (int, optional): page index. Defaults to 1.
        - `hits_per_page` (int, optional): products number in one page. Defaults to 40.
        - `price_from` (int, optional): filter by min price. Defaults to 0.
        - `price_to` (int, optional): filter by max price. Defaults to 1_000_000.
        - `categories` (Iterable[Category], optional): filter by categories. Defaults to ().
        - `sizes` (Iterable[Size], optional): filter by sizes. Defaults to ().
        - `designers` (Iterable[str], optional): filter by designer names. Defaults to ().
        - `conditions` (Iterable[Condition], optional): filter by conditions. Defaults to ().
        - `markets` (Iterable[Markets], optional): filter by markets. Defaults to ().
        - `locations` (Iterable[Locations], optional): filter by locations. Defaults to ().
        - `max_values_per_facet` (int, optional): Defaults to 100.
        - `facets` (Iterable[Facets], optional): Defaults to all facets.
        - `verbose` (bool, optional): show htp request. Defaults to False.
    - Description:
        For parameters `department`, `categories`, `sizes`, `conditions`, `markets`, `locations`, `facets` use builtin enums that are available in `enums.categories` module. There are following categories: `Tops`, `Bottoms`, `Outerwear`, `Footwear`, `Tailoring`, `Accessories` available under `enums.categories` module.

        `sizes` parameter should contain categories' sizes that are accessible in `.sizes` properties (e.g. `Tops.sizes` or `Outerwear.sizes`). Note if you are gonna include size and won't include it's category, it won't be affected as well as including category with sizes of different categories. You can see the example below
    - Example:
        ```python
        from enums import Conditions, Markets, Locations
        from enums.categories import Tops

        products = client.find_products(
            sold=False,
            query_search='vintage',
            categories=[Tops.BUTTON_UPS, Tops.JERSEYS],
            sizes=[Tops.sizes.L, Tops.sizes.M, Tops.sizes.S],
            price_from=100,
            price_to=200,
            conditions=[Conditions.IS_GENTLY_USED, Conditions.IS_NEW],
            markets=[Markets.BASIC, Markets.GRAILED],
            locations=[Locations.ASIA, Locations.EUROPE]
        )
        ```


- `find_product_by_id` - find one product with provided id. If product doesn't exist, an error will be thrown
    - Parameters:
        - `id` (str): product id
        - `verbose` (bool, optional): show htp request. Defaults to False.
    - Example:
        ```python
        product = client.find_product_by_id(id='123456789')
        ```

- `find_brands` - find brands that match to query search
    - Parameters:
        - `query` (str): keyword to search a brand
        - `verbose` (bool, optional): show htp request. Defaults to False.
    - Example:
        ```python
        brands = client.find_brands(query='levis')
        ```

## How to test

To test the API, just run `pytest .` command.