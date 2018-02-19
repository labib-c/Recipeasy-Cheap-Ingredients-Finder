from bs4 import BeautifulSoup
import urllib.request
import conversions

def scrape(name_):
    """Returns list of tuples of form (price, name, quantity) given an item to search loblaws"""
    name_list = name_.split()
    if len(name_list) == 1:
        webpage_name = ("https://www.loblaws.ca/search/1518898683998/page/~item/" + name_ +
                        "/~sort/recommended/~selected/true")
    else:
        name_cat= ''
        for i in name_list:
            name_cat += i
            name_cat += '+'
        webpage_name = ("https://www.loblaws.ca/search/1518898683998/page/~item/" + name_cat[:len(name_cat)-1] +
                        "/~sort/recommended/~selected/true")
    page = urllib.request.urlopen(webpage_name)
    soup = BeautifulSoup(page, "html.parser")
    names = []
    for name in soup.find('span', attrs={
        'class': 'js-product-entry-name'}).parent.parent.parent.parent.parent.parent.parent.find_all(
            'span', attrs={'class': 'js-product-entry-name'}):
        names.append(name.text.strip())

    prices = []
    prices_to_names = []

    quantity = []

    for q in soup.find('span', attrs={
        'class':'reg-qty'}).parent.parent.parent.parent.parent.parent.parent.parent.find_all(
            'span', attrs={'class': 'reg-qty'}):
        qty = q.text.strip()
        if '100ea' in (qty.replace("\n", "")).replace(" ", ""):
            price = ""
            quant = ""
        elif 'ea' in qty:
            price = qty[qty.find("\n")+1:qty.find("/")]
            quant = 'each'
        else:
            price = qty[qty.find("\n")+1:qty.find("/")]
            quant = qty[qty.find("/")+1:]
            if len(quant) > 16:
                quant = quant.replace("\n", '').strip()[0:3]
        quant_to_add = quant.replace("\n",'').strip().replace(" ",'')
        price_to_add = price.strip().replace("\n",'').replace("e",'').strip()[1:]
        if quant_to_add != '' or price_to_add != '':
            price_to_add = float(price_to_add)
            if quant_to_add.strip() == 'kg':
                price_to_add /= 10
                price_to_add = round(price_to_add, 2)
                quant_to_add = "100g"
        prices.append(price_to_add)
        quantity.append(quant_to_add)
    for i in range(len(names)):
        if prices[i] != '' or quantity[i] != '':
            tup = (prices[i], names[i], quantity[i])
            prices_to_names.append(tup)

    return prices_to_names


def sort_tuple(tuple_list):
    """Return sorted list of tuples given an unsorted list"""
    return sorted(tuple_list, key=lambda x: x[0])


def get_wanted_quantities(desired_quantity, tuplist):
    """Remove all items from given tuple list if they do not match the given quantity type"""
    conv = conversions.get_loblaws_quantity(desired_quantity)
    counter = 0
    while counter < len(tuplist):
        if tuplist[counter][2] != conv:
            del tuplist[counter]
        else:
            counter += 1


if __name__ == "__main__":
    tup_list = scrape("orange")
    print(tup_list)

    sorted_tup_list = sort_tuple(tup_list)
    print(sorted_tup_list)

    get_wanted_quantities('g', sorted_tup_list)
    print(sorted_tup_list)
