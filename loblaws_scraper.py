from bs4 import BeautifulSoup
import urllib.request




# name_box = soup.find('span', attrs={'class': 'js-product-entry-name'})
# name = name_box.text.strip()
# print(name)
#
# name_box2 = soup.find_next('span', attrs={'class': 'js-product-entry-name'})
# name2 = name_box2.text.strip()
# print(name2)


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
    for price in soup.find('span', attrs={
        'class': 'reg-price-text'}).parent.parent.parent.parent.parent.parent.parent.parent.find_all(
            'span', attrs={'class': 'reg-price-text'}):
        prices.append(price.text.strip())
    prices_to_names = []

    for i in range(len(names)):
        tup = (float(prices[i][1:]), names[i])
        prices_to_names.append(tup)

    return prices_to_names


def sort_tuple(tuple_list):
    return sorted(tuple_list, key=lambda x: x[0])

if __name__ == "__main__":
    tup_list = scrape("apple sauce")
    print(tup_list)

    sorted_tup_list = sort_tuple(tup_list)
    print(sorted_tup_list)
