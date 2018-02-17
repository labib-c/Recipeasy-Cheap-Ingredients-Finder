from bs4 import BeautifulSoup
import urllib.request


webpage_name = "https://www.loblaws.ca/search/1518898683998/page/~item/apple/~sort/recommended/~selected/true"
page = urllib.request.urlopen(webpage_name)
soup = BeautifulSoup(page, "html.parser")

# name_box = soup.find('span', attrs={'class': 'js-product-entry-name'})
# name = name_box.text.strip()
# print(name)
#
# name_box2 = soup.find_next('span', attrs={'class': 'js-product-entry-name'})
# name2 = name_box2.text.strip()
# print(name2)

for name in soup.find('span', attrs={'class': 'js-product-entry-name'}).parent.parent.parent.parent.parent.parent.parent.find_all(
        'span', attrs={'class': 'js-product-entry-name'}):
    print(name.text.strip())
for price in soup.find('span', attrs={'class': 'reg-price-text'}).parent.parent.parent.parent.parent.parent.parent.parent.find_all(
        'span', attrs={'class': 'reg-price-text'}):
    print(price.text.strip())
