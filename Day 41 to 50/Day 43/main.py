from bs4 import BeautifulSoup
import requests

# live scraping website

website_html = requests.get(url="https://news.ycombinator.com/news")

soup = BeautifulSoup(website_html.text, "html.parser")
formatted_data = {}

headlines = soup.findAll(name="a", class_='titlelink')
scores = soup.findAll(name="span", class_="score")

for headline in headlines:
    formatted_data[headline.getText()] = {"score": scores[headlines.index(headline) - 1].getText().split(" ")[0],
                                          "url": headline.get("href")}
    # print(headline.getText())

print(formatted_data)
# tutorial

# import lxml    # for xml files
# and instead of html.parser we use "lxml"
# with open("website.html", mode='r') as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)
# print(soup.a)  # print anchor tab
# # find all
#
# print(soup.findAll(name="a"))
# # print the data from anchor tags use GetText
# # for the link we will use get("href)
# # we can use find method also
# for tags in soup.findAll("a"):
#     print(tags.get("href"))
#
#
# a = soup.select_one(selector="p a")  # we can use css selector like '#' or'.' and other stuff
# print(a)
