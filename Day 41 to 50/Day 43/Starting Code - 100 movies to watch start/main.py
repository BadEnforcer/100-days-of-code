import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")

movie_names = soup.findAll(name="h3", class_="title")
with open("movies.txt", mode="a") as file:
    for name in movie_names[::-1]:
        file.write(f"{name.getText()}\n")
