import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Book Name", "Price (£)", "Rating"])

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating_class = book.p["class"][1]
        rating = rating_class
        writer.writerow([title, price, rating])
        print(f"{title} | {price} | {rating}")

print("\nData has been saved to products.csv")
