import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.nfl.com/standings/league/2019/REG'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table', class_ ="d3-o-table d3-o-table--row-striping d3-o-table--detailed d3-o-standings--detailed d3-o-table--sortable {sortlist: [[4,1]], sortinitialorder: 'desc'}")
# print(table)
# print(type(table))

headers = []

# print(type(table.find_all('th')))
for i in table.find_all('th'):
    title = i.text
    headers.append(title)
    
# print(headers)

df = pd.DataFrame(columns = headers)

for j in table.find_all('tr')[1:]:
    first_td = j.find_all('td')[0].find('div', class_ = 'd3-o-club-fullname')
    # print(first_td.text)
    row_data = j.find_all('td')[1:]
    row = [td.text for td in row_data]
    row.insert(0, first_td.text)
    length = len(df)
    df.loc[length] = row
    
# print(df)

df.to_csv('E:/Crawling/Crawler/Web Scraping In Python With BeautifulSoup And Selenium 2021/Project_1/coading_exercise.csv')