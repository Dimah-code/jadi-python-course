import requests
from bs4 import BeautifulSoup

url = "https://scrapeme.live/shop/"
target_class = "li.product"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

page_title = soup.title.string.strip()
products = soup.select(target_class)

titles = []
url_images = []

for product in products:

    title_tag = product.find("h2", class_="woocommerce-loop-product__title")
    if title_tag:
        titles.append(title_tag.get_text(strip=True))
    else:
        titles.append("Unknown")

    img_tag = product.find("img")
    if img_tag and img_tag.has_attr("src"):
        url_images.append(img_tag["src"])
    else:
        url_images.append("No image found")

print("Page Title:", page_title)

print("\nTitles:\n")
for t in titles:
    print("-", t, "\n")

print("\nImage URLs:\n")
for img in url_images:
    print("-", img, "\n")
