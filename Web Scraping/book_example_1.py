# GOAL: get the title of every book with a 2 star rating
import requests
import bs4

base_url='http://books.toscrape.com/catalogue/page-{}.html'

# LOGIC TESTS
# we are using a format {} in the URL to pass in a page number

# making a request to the specific URL passing 1 to indicate PAGE 1
#res=requests.get(base_url.format(1))
#soup=bs4.BeautifulSoup(res.text,'lxml')

# Getting an element by class="product_pod" each product has this class
#products=soup.select('.product_pod')

# example=products[0]

# Checking if the prodcuct does't have the class="star-rating Two" - if the LIST [] is empty that means it is NOT a 2 star product and we can move on
# print([]==example.select('.star-rating.Two'))

# We are grabbig <a> element of the product at index 1, becuse there are two <a> elements
# and we are selecting a title attribute from that <a> element NOT the text of the element
# print(example.select('a')[1]['title'])

# SOLUTION
two_star_titles=[]

for page_num in range(1,51):
    scrape_url=base_url.format(page_num)
    res=requests.get(scrape_url)

    soup=bs4.BeautifulSoup(res.text,'lxml')
    books=soup.select('.product_pod')

    for book in books:
        # if the list is 0 that means the class dose not exisit and the rating is NOT 2 stars
        if len(book.select('.star-rating.Two'))!=0:
            book_title=book.select('a')[1]['title']
            two_star_titles.append(book_title)

for book_t in two_star_titles:
    print(book_t)