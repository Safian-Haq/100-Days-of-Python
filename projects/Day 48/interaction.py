from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = 'C:\Selenium\chromedriver.exe'
driver = webdriver.Chrome(CHROME_DRIVER_PATH)

## Wikipedia article count

# URL = 'https://en.wikipedia.org/wiki/Main_Page'
#
# driver.get(URL)
#
# article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# print(article_count.text)
#
# driver.close()

