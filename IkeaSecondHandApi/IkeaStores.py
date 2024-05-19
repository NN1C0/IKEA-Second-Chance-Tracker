import requests


def getStoreIds(countryCode="nl"):
    request_url = f"https://www.ikea.com/{countryCode}/{countryCode}/meta-data/navigation/stores.json"
    response = requests.get(request_url)
    ids = []

    for store in response.json():
        ids.append({"id": store["id"], "name": store["name"]})
    
    return ids
