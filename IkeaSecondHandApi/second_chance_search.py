import requests


def searchSecondChance(searchTerm, country_constant, store_ids=[], debug=False):
    found_items = []
    page = 0
    response_has_content = True
    formatted_store_ids = ','.join(map(str, store_ids))
    
    while(response_has_content):
        request_Url = f"https://web-api.ikea.com/circular/circular-asis/api/public/offers/{country_constant}?size=16&stores={formatted_store_ids}&search={searchTerm}&page={page}"
        #print(request_Url)
        response = requests.get(request_Url)
        response_code = response.status_code

        
        if response.status_code == 200:
            json_response = response.json()
            total_pages = json_response["totalPages"]
            if len(json_response["content"]) > 0:
                for item in json_response["content"]:
                    found_items.append({"id": item["id"],
                                        "store_id": item["unitId"],
                                        "title": item["title"],
                                        "description": item["description"],
                                        "price": item["price"],
                                        "article_price": item["articlesPrice"],
                                        "currency": item["currency"],
                                        "reason_discount": item["reasonDiscount"],
                                        "hero_image": item["heroImage"]
                                        })
            else:
                response_has_content = False

            if debug:
                print(f"Page: {page}/{total_pages}")
                print(f"Offers: {len(found_items)}")
        else:
            response_has_content = False
        page += 1

    return found_items