import requests
import bs4
import lxml

# Main 10 tags
res = requests.get(" http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(res.text, "lxml")
tags = []

tag = soup.select(".col-md-4.tags-box")

for i in tag:
    for g in range(0, 10):
        tags.append(i.select(".tag")[g].getText())
# print(tags)

# all unique authors list
allAuthors = set()
base_html = "http://quotes.toscrape.com/page/{}/"

for i in range(1, 11):
    res = requests.get(base_html.format(i))
    soup2 = bs4.BeautifulSoup(res.text, "lxml")
    for j in soup2.select(".author"):
        allAuthors.add(j.getText())
# print(allAuthors)
