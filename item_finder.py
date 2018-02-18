import loblaws_scraper
import validity_checker
import conversions

def find_items(items, quantities, numbers): #items, quantities, and numbers should be parallel lists
    price = 0
    tuples = []
    for i in range(len(items)):
        prices_to_items = loblaws_scraper.scrape(items[i])
        sorted_tup = loblaws_scraper.sort_tuple(prices_to_items)
        loblaws_scraper.get_wanted_quantities(quantities[i], sorted_tup)
        corresponding_tuple = validity_checker.check_similarity(items[i], sorted_tup)
        price += round(conversions.convert_quantities(corresponding_tuple[0], numbers[i], quantities[i]), 2)
        tuples.append(corresponding_tuple)
    return [tuples, price]

def return_final_price(items, quantities, numbers):
    tuples_price = find_items(items, quantities, numbers)
    return tuples_price[1]

if __name__ == "__main__":
    items_ = ["apple", "banana", "orange"]
    quantities_ = ["g", "g", "g"]
    numbers_ = [10, 10, 10]
    final_price = return_final_price(items_, quantities_, numbers_)
    print(final_price)
