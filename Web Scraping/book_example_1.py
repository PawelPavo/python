# GOAL: get the title of every book with a 2 star rating
import requests
import bs4

# we are using a format {} in the URL to pass in a page number
base_url='http://books.toscrape.com/catalogue/page-{}.html'

res=requests.get(base_url.format(1))
soup=bs4.BeautifulSoup(res.text,'lxml')

books=soup.select('.product_pod')

print(len(books))