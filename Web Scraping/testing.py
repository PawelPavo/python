import requests
import bs4

res=requests.get("https://www.xolobooks.com/bookstore?page=2")
print(type(res))

soup=bs4.BeautifulSoup(res.text,"lxml")
for title in soup.select('.syHtuv'):
    print(title.text)