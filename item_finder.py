import loblaws_scraper
import validity_checker

def find_items(items, quantities, numbers): #items, quantities, and numbers should be parallel lists
    price = 0
    tuples = []
    for i in range(len(items)):
        prices_to_items = loblaws_scraper.scrape(items[i])
        sorted_tup = loblaws_scraper.sort_tuple(prices_to_items)
        loblaws_scraper.get_wanted_quantities(quantities[i], sorted_tup)
        corresponding_tuple = validity_checker.check_similarity(items[i], sorted_tup)
        price += corresponding_tuple[0] * numbers[i]
        tuples.append(corresponding_tuple)
    return [tuples, price]

if __name__ == "__main__":
    items_ = ["apple", "banana", "orange"]
    for item in items_:
        tuple_list = loblaws_scraper.scrape(item)
        print(loblaws_scraper.sort_tuple(tuple_list))
        print("")
    quantities_ = ["100g", "100g", "100g"]
    numbers_ = [10, 10, 10]
    tuples_and_price = find_items(items_, quantities_, numbers_)
    print(tuples_and_price)
