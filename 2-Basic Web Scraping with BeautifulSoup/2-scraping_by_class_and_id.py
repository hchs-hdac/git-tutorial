# importing necessary libraries
from bs4 import BeautifulSoup
import requests as req 

# Using requests to get HTML from URL (get function)
page = req.get('https://www.nytimes.com/2020/04/20/health/treatment-delays-coronavirus.html') # a times article about COVID-19

soup = BeautifulSoup(page.text, 'lxml')

# Visit the URL and use the element inspector (right click, then inspect) to find various class and id names

article = soup.find(id='story') # finds the element with the id story
print(article.get_text())

companion_columns = soup.find_all(class_='css-53u6y8') # finds all elements with the class css-53u6y8
print([column.get_text() for column in companion_columns])
