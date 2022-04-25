import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
# print(soup)

# print(soup.find_all('bg-quote', class_ = 'value')[0].text)
current_price = soup.find_all('bg-quote', class_ = 'value')[0].text
print(current_price)

# print(soup.find_all('td', class_ = 'table__cell u-semi')[0].text)
closing_price = soup.find_all('td', class_ = 'table__cell u-semi')[0].text
print(closing_price)

# # print(soup.find_all('span', class_ = 'primary')[4].text)
# week_range_start = soup.find_all('span', class_ = 'primary')[4].text

# week_range_start_2 = soup.find_all('span', class_ = 'primary')[4]
# print(week_range_start_2.find_all('span'))

# print(soup.find_all('div', class_ = 'range__header'))
range = soup.find_all('div', class_ = 'range__header')[2]
# print(range)
# print(type(range))
# print(range.text)

# print(range.find_all('span', class_ = 'primary')[0])

range_1 = range.find_all('span')[0].text
print(range_1)

range_2 = range.find_all('span')[2].text
print(range_2)

rating = soup.find_all('li', class_= 'analyst__option active')[0].text
print(rating)