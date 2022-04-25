import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.worldometers.info/world-population/'

page = requests.get(url)
# print(page)

soup = BeautifulSoup(page.text, 'lxml')
# print(soup)

table = soup.find('table', class_ = 'table table-striped table-bordered table-hover table-condensed table-list')
# print(table)
# print(table.find_all('th'))

headers = []
for i in table.find_all('th'):
    title = i.text
    headers.append(title)
# print(headers)

# this will hold the data but not create a row in data frame
# So, the statement will help you to create coulmns and the headers
df = pd.DataFrame(columns = headers)

# # this will add a row in the data frame so, if using this statement
# # we will not be able to create a columns headers in data frame
# df = pd.DataFrame({'columns': headers})

# print(df)

# print(table.find_all('tr')[1:])

for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    # row_data holds the HTML data of the current row.
    
    # the bellow statement goes to "row_data" 
    # and gets the every text for the curent row.
    row = [tr.text for tr in row_data]
    # print(row)
    
    length = len(df)
    # print(length)
    # print(df)
    # defining the row length for the current row data for data frame
    df.loc[length] = row
    # The loc property is used to access a group of rows 
    # and columns by label(s) or a boolean array.
    
# print(df)

# To export the data frame as an CSV file.
# CSV: A comma-separated values (CSV) file 
# is a delimited text file that uses a comma to separate values.
# it is almost the exact same as the excel file.
df.to_csv('E:/Crawling/Crawler/Web Scraping In Python With BeautifulSoup And Selenium 2021/Project_1/table_scraped.csv')
# "to_csv" eill Write object to a comma-separated values (csv) file.