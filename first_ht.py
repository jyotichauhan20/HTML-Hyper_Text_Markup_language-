import requests
from bs4 import BeautifulSoup
data=requests.get("https://www.imdb.com/chart/top/").text
soup=BeautifulSoup(data,"html.parser")
print(soup)

soup.title
soup.title.name
soup.title.string

