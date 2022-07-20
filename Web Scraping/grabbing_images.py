import requests
import bs4

# make a request to a URL to get all the content
res=requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup=bs4.BeautifulSoup(res.text,'lxml')

# Created a correct path to the image found through INSPECT in chrome , its an <a> with .image class with img element
computer=soup.select('a.image img')[0]

# Creating a link URL by selecting the src from the above path
image_link=requests.get('https:'+computer['src'])

# Opening and creating a file for the image - must be the same extension '.jpg' and type 'wb' because it is in binary Write Binary
# You can provide a full file path to where you want to save the image or it will save to the current location
f=open('deep_blue_computer_test.jpg','wb')

# Writting the BINARY contnet of the image
f.write(image_link.content)

# closing the file
f.close()