import requests
from bs4 import BeautifulSoup

# Scrape product details
url = "https://www.saucedemo.com/inventory.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())

max_price = 0
max_price_product = {}

for product in soup.find_all('div', class_='inventory_item'):
    name = product.find('div', class_='inventory_item_name').text.strip()
    description = product.find('div', class_='inventory_item_description').text.strip()
    price = float(product.find('div', class_='inventory_item_price').text.strip().replace('$', ''))

    if price > max_price:
        max_price = price
        max_price_product = {'name': name, 'description': description}

# Add product with max price to cart
print(f"Adding product to cart: {max_price_product['name']}")
print("Product Description:", max_price_product['description'])
