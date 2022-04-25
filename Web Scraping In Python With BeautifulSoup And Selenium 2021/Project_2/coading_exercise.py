import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame({'Car':[''], 'Colour':[''], 'Price':[''], 'Links':['']})

postings = soup.find_all('div', class_ = 'media soft push-none rule')

while True:
    for post in postings:
        car = post.find('h4', class_ = 'hN').text.strip()
        colour = post.find_all('div', class_ = 'grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
        price = post.find_all('div', class_ = 'l-column l-column--medium-4 push-none')
        price_1 = post.find('strong', class_ = 'delta').text.strip()
        link = post.find('a', class_ = 'media__img media__img--thumb').get('href')
        link_full = 'https://www.carpages.ca' + link
        df = df.append({'Car':car, 'Colour':colour, 'Price':price_1, 'Links':link_full}, ignore_index=True)
    
    try:
        next_page = soup.find('a', {'title':'Next Page'}).get('href')
        url = next_page
        page = requests.get(next_page)
        soup = BeautifulSoup(page.text, 'lxml')
        postings = soup.find_all('div', class_ = 'media soft push-none rule')
    except:
        break
    
print('While Loop exit')
df.to_csv('E:\Crawling\Crawler\Web Scraping In Python With BeautifulSoup And Selenium 2021\Project_2\coading_exercise.csv')