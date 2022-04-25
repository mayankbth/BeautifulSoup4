import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

# print(soup)

# # Find() :- The reasion why find is a powerful function, because it is the main function we use to search through out the html. 
# #           And also it is a filterying function as well.
# print(soup.find('header'))

# # this wil only be useful when we have one header tag in the html file. because this will only provide the first occurance of header tag
# print(soup.header)

# print(soup.header.attrs)

# # to find the attributes of div tag
# print(soup.find('div', {'class': 'container test-site'}))

# print(soup.find('h4', {'class': 'pull-right price'}))
# # this only works for the class attribute and the out put will be same as above
# print(soup.find('h4', class_= 'pull-right price'))

# # find_all() returns all the tags and strings that match the filters.
# print('find_all()')
# print(soup.find_all('h4', {'class': 'pull-right price'}))

# # for all the products names
# print("product names")
# print(soup.find_all('a', {'class': 'title'}))
# # # we can also write the above statement like the bellow. 
# # # NOTE: This is only valide for class attribute.
# # print("product names")
# # print(soup.find_all('a', class_= 'title'))

# # "find_all()" for reviews
# print("product reviews")
# print(soup.find_all('p', {'class': 'pull-right'}))

# # to get the information as per the position inside the list.
# # we just need to add the indexing.
# # getting the prise of 6th product
# print(soup.find_all('h4', {'class': 'pull-right price'})[5])

# # here we can also apply list indexing and its operations
# print(soup.find_all('h4', {'class': 'pull-right price'})[5:])

# # to find more than one tag at once...
# print(soup.find_all(['h4', 'p', 'a']))

# # to filter based on boolian objects...
# # here we are getting all the "HTML" code that has "id" as an attribute
# print(soup.find_all(id = True))

# # to find objects directly based on strings
# print(soup.find_all(string = 'Iphone'))

# # to find the onjects bsaed on some charecters of a string
# import re
# # Support for regular expressions (RE)
# print(soup.find_all(string = re.compile('Iph')))
# # for NOKIA
# print(soup.find_all(string = re.compile('Nok')))

# # we can also use this re.complie when we are looking at attributes too
# # to find all the class name that have "pull" in it
# print(soup.find_all(class_ = re.compile('pull')))

# # to find all the class having "pull" in it with "p" tag associated
# print(soup.find_all('p', class_ = re.compile('pull')))

# # to use "soup.find_all()" with limit
# # for first 3
# print(soup.find_all('p', class_ = re.compile('pull'), limit = 3))

# # to find information based on more than one type of strings
# print(soup.find_all(string = ['Iphone', 'Nokia 123']))

# Now, we are creating a product table with all the details associated with the products

# # all product name
product_name = soup.find_all('a', class_='title')
# print(product_name)

# # all price
price = soup.find_all('h4', class_='pull-right price')
# print(price)

# # all reviews
review = soup.find_all('p', class_='pull-right')
# print(review)

# # all descriptions
description = soup.find_all('p', class_='description')
# print(description)

# To only get the text part from the HTML information

# for product names
product_name_list = []
for i in product_name:
    name = i.text
    # print(name)
    product_name_list.append(name)
    
# for product price
price_list = []
for i in price:
    price2 = i.text
    # print(price2)
    price_list.append(price2)
    
# for product reviews
review_list = []
for i in review:
    review2 = i.text
    # print(review2)
    review_list.append(review2)
    
# for product descriptions
description_list = []
for i in description:
    description2 = i.text
    # print(description2)
    description_list.append(description2)
    

# to put the list into an table and for that we need a liberary "pandas"
# "Pandas" is the main liberary used for accessing the data-frames
import pandas as pd
# DataFrame: Two-dimensional, size-mutable, potentially heterogeneous tabular data.
#            DataFrames are always in the dictonary.
table = pd.DataFrame({'Product Name': product_name_list,
                      'Description': description_list,
                      'Price': price_list,
                      'Reviews': review_list})
# print(table)


# # extracting data from nested HTML tags
# # this will give html information of all the boxex
# boxes = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')
# # print(boxes)
# # print(len(boxes))

# getting the html information of the third box
boxes = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')[6]
# print(boxes)

# to get the exact text info

# # find exact line for the html info
# print(boxes.find('a', class_='title'))

# # find the exact text info
# print(boxes.find('a', class_='title').text)
# print(boxes.find('p', class_='description').text)

# NOTE:
# when we use the "find_all()" and wnat it then subside again, then
# we will have to provide the position of the element otherwise it wil 
# create the list of elements and after that doing subsiding again 
# it will throw error
box2 = soup.find_all('ul', class_='nav', id='side-menu')[0]
# print(len(box2))
# print(box2)
print(box2.find_all('li')[1].text)