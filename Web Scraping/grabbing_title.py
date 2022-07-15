import requests
import bs4

res=requests.get("http://example.com/")
print(type(res))
print(res.text)

soup=bs4.BeautifulSoup(res.text,"lxml")
print(soup)

# Grabs a list of elements
print(soup.select('title'))

# Gets just the text of the element ONLY
print(soup.select('title')[0].getText())

site_pars=soup.select('p')

print(site_pars[0].getText())