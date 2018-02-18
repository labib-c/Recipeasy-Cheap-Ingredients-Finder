from bs4 import BeautifulSoup
import urllib.request

def scrape(name_):
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
        prices.append(price.strip().replace("\n",'').replace("e",'').strip())
        quantity.append(quant.replace("\n",'').strip().replace(" ",''))
    for i in range(len(names)):
        if prices[i] != '' or quantity[i] != '':
            tup = (float(prices[i][1:]), names[i], quantity[i])
            prices_to_names.append(tup)

    return prices_to_names


def sort_tuple(tuple_list):
    return sorted(tuple_list, key=lambda x: x[0])

def get_wanted_quantities(desired_quantity, tuplist):
    counter = 0
    while counter < len(tuplist):
        if tuplist[counter][2] != desired_quantity:
            del tuplist[counter]
        else:
            counter += 1

if __name__ == "__main__":
    tup_list = scrape("orange")
    print(tup_list)

    sorted_tup_list = sort_tuple(tup_list)
    print(sorted_tup_list)

    get_wanted_quantities('kg', sorted_tup_list)
    print(sorted_tup_list)
