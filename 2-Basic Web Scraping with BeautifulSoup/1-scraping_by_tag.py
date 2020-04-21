# importing necessary libraries
from bs4 import BeautifulSoup
import requests as req 

# Using requests to get HTML from URL (get function)
page = req.get(url='https://www.york.ac.uk/teaching/cws/wws/webpage1.html')

soup = BeautifulSoup(page.text, 'lxml') # lxml allows Python to easily process HTML files

body = soup.find('body') # extracts all the html in the body of the webpage
print(body) # returns a lot of messy html
print(body.get_text()) # returns only the text of the html, without the tags

paragraphs = soup.find_all('p') # extracts all the html with the <p> tag (if you just use find, it will only return the first <p>)
print([paragraph.get_text() for paragraph in paragraphs]) # looping through all the <p>s that were returned

# used list comprehension shortcut above -- but here's the long version (commented out)
'''
lst = []
for paragraph in paragraphs:
    lst.append(paragraph.get_text())
'''

