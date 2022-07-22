import requests
import bs4

# TASK 5
# Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. 
# Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website.
# Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. 
# For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, 
# but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!


page_num=1
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