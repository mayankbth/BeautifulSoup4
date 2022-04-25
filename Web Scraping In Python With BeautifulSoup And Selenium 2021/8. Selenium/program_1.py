from selenium import webdriver

driver = webdriver.Chrome('E:\Crawling\chrome_web_driver\chromedriver_win32\chromedriver.exe')

driver.get('https://www.goat.com/sneakers')

driver.find_element_by_class_name('GridCellProductInfo__ProductInfo-sc-17lfnu8-0 gseUSZ')