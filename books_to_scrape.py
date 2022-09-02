# Scraping info from toscrape.com

import requests
import bs4
import lxml

# All books with rate 3 and its price
star_Three_books = []
html_base = "http://books.toscrape.com/catalogue/page-{}.html"

for page in range(1, 51):
    res = requests.get(html_base.format(page))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")
    for book in books:
        if (len(book.select(".star-rating.Three")) != 0):
            title = book.select("a")[1]["title"]
            price = book.select(".price_color")[0].getText()
            star_Three_books.append(f"{title}. Price: {price[1:]}")

for i in star_Three_books:
    print(i)
