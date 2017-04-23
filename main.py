import requests
from bs4 import BeautifulSoup

http_proxy  = ""
https_proxy = ""

proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy
            }

def used_prices(html):
    soup = BeautifulSoup(html, "html.parser")
    #table = soup.find('tbody', attrs={'class': 'stripe'})

    listing = soup.find_all(class_="ProductCell__container__BapE8")

    used_price_list = []

    for item in listing:
        atr = item.find(class_="ProductCell__title__rstiF")

        size =  atr.contents[0].get_text()
        price =  atr.contents[1].get_text()

        if size == "10.5":
            used_price_list.append(float(price[1:]))

        used_price_list.sort()
    return used_price_list



if __name__ == "__main__":
    url = 'https://www.goat.com/sneakers/yeezy-boost-350-pirate-2016-bb5350/used'
    response = requests.Session()
    out = response.get(url, proxies=proxyDict, verify=False)
    html = out.content

    pirate = used_prices(html)

    url = 'https://www.goat.com/sneakers/yeezy-boost-350-aq2660/used'
    response = requests.Session()
    out = response.get(url, proxies=proxyDict, verify=False)
    html = out.content

    moonrock = used_prices(html)


    print pirate
    print moonrock
