import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.airbnb.co.in/s/Honolulu--HI--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Honolulu%2C%20HI%2C%20United%20States&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&checkin=2022-04-19&checkout=2022-04-23&source=structured_search_input_header&search_type=autocomplete_click&federated_search_session_id=f408ab9a-d92f-403e-94ea-94982014d631&pagination_search=true'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

# creating dataFrame according to the values i am scraping
df = pd.DataFrame({'Links':[''], 'Title':[''], 'Details':[''], 'Price':[''], 'Rating':['']})

# while True:
while url != False:
    postings = soup.find_all('div', class_ = '_1e9w8hic')
    for post in postings:
        try:
            link = post.find('a', class_= 'l8au1ct dir dir-ltr').get('href')
            link_full = 'https://www.airbnb.co.in' + link
            title = post.find('span', class_= 'ts5gl90 tl3qa0j t1nzedvd dir dir-ltr').text
            price = post.find('span', class_= '_tyxjp1').text
            rating = post.find('span', class_= 'rpz7y38 dir dir-ltr').text
            details = post.find_all('span', class_= 'mp2hv9t dir dir-ltr')
            detail_text = []
            for detail in details:
                value = detail.text
                detail_text.append(value)
            detail_text_string = ', '.join([str(item) for item in detail_text])
            df = df.append({'Links':link_full, 'Title':title, 'Details':detail_text_string, 'Price':price, 'Rating':rating}, ignore_index=True)
        except:
            pass
    
    # df.to_csv('E:/Crawling/Crawler/Web Scraping In Python With BeautifulSoup And Selenium 2021/Project_2/project_2.csv')
    # here, .get() will give the value of 'href' or any attribute presenred
    try:
        next_page = soup.find('a', {'aria-label': 'Next'}).get('href')
        next_page_full = 'https://www.airbnb.co.in' + next_page
        url = next_page_full
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
    except:
        url = False
print(df)
df.to_csv('E:/Crawling/Crawler/Web Scraping In Python With BeautifulSoup And Selenium 2021/Project_2/project_2.csv')
