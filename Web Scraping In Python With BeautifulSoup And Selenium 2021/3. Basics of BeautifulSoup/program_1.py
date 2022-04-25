import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

# print(requests.get(url))

page = requests.get(url)

# print(page.text)

# here "page.text" is grabbing all the HTML code on the provided on the page as a text. i.e. as a very long string.
# then the "lxml" parser convert back that sting into HTML format and put that into python.
soup = BeautifulSoup(page.text, 'lxml')
# print(soup)

# # this will provide everything inside the header tag
# print(soup.header)

# # this will only gives the first occurence of it
# print(soup.div)

# this will give everythng inside the "p" tag which is inside the "header" tag
tag = soup.header.p
# print(tag)

# # now we have all the html of "tag" as a string
# print(tag.string)

# # or we can also do like this to grab all the data insisde the tag as a string
# print(soup.header.p.string)

tag = soup.header.a
# print(tag)

# # to get the attributes of any tag use "attrs"
# print(tag.attrs)
# # output:
# # {'data-toggle': 'collapse-side', 'data-target': '.side-collapse', 'data-target-2': '.side-collapse-container'}

# # to find the what a perticular attributes of a tag is equal to the
# print(tag['data-toggle'])
# # output:
# # collapse-side

# # we can also input things and change the "html" that we have
# tag['attribute_new'] = 'this is a new attribute'
# # print(tag.attrs)
# # output:
# # {'data-toggle': 'collapse-side', 'data-target': '.side-collapse', 'data-target-2': '.side-collapse-container', 
# #   'attribute_new': 'this is a new attribute'}

# print(tag)
# # output:
# # <a attribute_new="this is a new attribute" data-target=".side-collapse" data-target-2=".side-collapse-container" data-toggle="collapse-side">
# # <button aria-controls="navbar" aria-expanded="false" class="navbar-toggle pull-right collapsed" data-target="#navbar" data-target-2=".side-collapse-container" data-target-3=".side-collapse" data-toggle="collapse" type="button">
# # <span class="sr-only">Toggle navigation</span>
# # <span class="icon-bar top-bar"></span>
# # <span class="icon-bar middle-bar"></span>
# # <span class="icon-bar bottom-bar"></span>
# # </button>
# # </a>

