from IkeaSecondHandApi import Ikea_stores, Second_chance_search
import pprint

def main():
    search_country = input("which country would you like to search in?\n")
    store_ids = Ikea_stores.getStoreIds(search_country)
    for i, market in enumerate(store_ids):
        print("%s %s" % (i, market["name"]))
    
    selected_market = int(input("Which market do you want to search in?\n"))
    search_term = input("What are you looking for?\n")

    search_results = Second_chance_search.searchSecondChance(search_term, store_ids[selected_market]["id"], search_country)
    print(f"I found {len(search_results)} results for: {search_term}")
    
    for result in search_results:
        print("Article: %s \t Price: %s \t Description: %s" % (result["title"], result["price"], result["description"]))


if __name__ == "__main__":
    main()