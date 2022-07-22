import requests
import bs4

page_num=0
valid_page=True

while valid_page:
    base_url=("https://www.xolobooks.com/bookstore?page={}")
    scrape_url=base_url.format(page_num)
    res=requests.get(scrape_url)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    button=soup.select('.txtqbB')
    if button == []:
        print('NO MORE PAGES')
        break
    page_num+=1
print(page_num)