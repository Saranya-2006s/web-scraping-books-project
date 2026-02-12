import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

titles = []
prices = []
ratings = []

for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]

        titles.append(title)
        prices.append(price)
        ratings.append(rating)

data = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings
})

data.to_csv("books_data.csv", index=False)

print("Data scraped and saved successfully!")
