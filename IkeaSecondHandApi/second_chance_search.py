import requests


def searchSecondChance(searchTerm, country_constant, storeIds=[]):
    found_items = []
    page = 0
    response_has_content = True
    
    while(response_has_content):
        request_Url = f"https://web-api.ikea.com/circular/circular-asis/api/public/offers/{country_constant}?size=16&stores={storeIds}&search={searchTerm}&page={page}"
        response = requests.get(request_Url)
        response_code = response.status_code

        
        if response.status_code == 200:
            json_response = response.json()
            if len(json_response["content"]) > 0:
                for item in json_response["content"]:
                    found_items.append({"title": item["title"],
                                        "description": item["description"],
                                        "price": item["price"]
                                        })
            else:
                response_has_content = False
        page += 1

    return found_items