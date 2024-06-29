import requests


def searchSecondChance(searchTerm, country_constant, store_ids, debug=False):
    """
    Search for items on the IKEA "As-Is" section using the IKEA API.

    This function queries the IKEA API directly for the "As-Is" section offers based on the provided search term, country, and store IDs. 
    Note that it cannot be used to search across multiple countries simultaneously.

    Args:
        searchTerm (str): The term to search for in the IKEA "As-Is" section.
        country_constant (str): The country code constant representing the country to search in.
        store_ids (list): A list of store IDs to search within.
        debug (bool, optional): If True, prints debug information during the search process. Defaults to False.

    Returns:
        list: A list of dictionaries containing the found items.

    Example:
        >>> searchTerm = "chair"
        >>> country_constant = "US"
        >>> store_ids = [123, 456, 789]
        >>> found_items = searchSecondChance(searchTerm, country_constant, store_ids, debug=True)
        >>> print(found_items)

    Notes:
        - This function constructs a URL for the IKEA API with the given search term, country, and store IDs.
        - It handles pagination and continues to fetch pages until no more content is available or an error occurs.
        - If `debug` is set to True, the function prints the current page number and the number of offers found so far.
    """
    found_items = []
    page = 0
    response_has_content = True
    formatted_store_ids = __format_store_list_to_string(store_ids)
    
    while(response_has_content):
        request_Url = f"https://web-api.ikea.com/circular/circular-asis/offers/public/{country_constant}?size=16&stores={formatted_store_ids}&search={searchTerm}&page={page}"
        response = requests.get(request_Url)

        if response.status_code == 200:
            json_response = response.json()
            total_pages = json_response["totalPages"]
            if len(json_response["content"]) > 0:
                for item in json_response["content"]:
                    found_items.append(__response_item_to_dict(item))
            else:
                response_has_content = False

            if debug:
                print(f"Country: {country_constant} \t| Page: {page}/{total_pages} \t| Offers: {len(found_items)}")
        else:
            response_has_content = False
        page += 1

    return found_items

def __response_item_to_dict(item) -> dict:
    return{"id": item["id"],
            "store_id": item["unitId"],
            "title": item["title"],
            "description": item["description"],
            "price": item["price"],
            "article_price": item["articlesPrice"],
            "currency": item["currency"],
            "reason_discount": item["reasonDiscount"],
            "hero_image": item["heroImage"]
            }

def __format_store_list_to_string(stores: list[str]) ->str:
    return ','.join(map(str, stores))