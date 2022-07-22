# Web Scraping Exercises
# Complete the Tasks Below

import requests
import bs4

# TASK 1
# Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.

res=requests.get('http://quotes.toscrape.com/')
soup=bs4.BeautifulSoup(res.text,'lxml')
# print(soup)

# TASK 2
# Get the names of all the authors on the first page.
authors=soup.select('.author')
for author in set(authors):
    print(author.text)

# TASK 3
# Create a list of all the quotes on the first page.
quote_list=[]
quotes=soup.select('.text')
for quote in quotes:
    quote_list.append(quote.text)
print(quote_list)

# TASK 4
# Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...). 
# HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top right tags, perhaps check the span.

tags=soup.select('.tag-item a')
for tag in tags:
    print(tag.text)

# TASK 5
# Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. 
# Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website.
# Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. 
# For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, 
# but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!

