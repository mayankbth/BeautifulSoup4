from bs4 import BeautifulSoup
import pandas as pd 
import requests

url = 'https://www.goat.com/sneakers'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
# print(soup)
# print('-------')

postings = soup.find_all('div', class_ = 'grid_cell_product')
# here we are getting "posting" as an empity list because "BeautifulSoup" is not able to scrape the JavaScript Code.
print('-------')
print(postings)
print('-------') 