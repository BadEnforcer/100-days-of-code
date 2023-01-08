from bs4 import BeautifulSoup
import requests
product_url = 'https://www.amazon.in/Verilux%C2%AE-Multiport-Adapter-Portable-Compatible/dp/B09163Q5CD/ref=sr_1_11_sspa'

var_class = "a-price-whole"

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


response = requests.get(product_url, headers=HEADERS)
soup = BeautifulSoup(response.content, features="lxml")

try:
    price = float(
        soup.find(id='priceblock_ourprice').get_text().replace('.', '').replace('€', '').replace(',', '.').strip())
except:
    price = ''
print(price)

