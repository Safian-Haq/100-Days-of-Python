from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pynput.keyboard import Key, Controller


URL = 'https://orteil.dashnet.org/cookieclicker/'

PATH_TO_DRIVER = 'C:\Selenium\msedgedriver.exe'

driver = webdriver.Edge(PATH_TO_DRIVER)

driver.get(URL)

time.sleep(10)

lang_button = driver.find_element('id', 'langSelect-EN')
lang_button.click()

# Zoom out to ensure all elements are on screen
kb = Controller()
for i in range(6):
    kb.press(Key.ctrl)
    kb.tap('-')
    kb.release(Key.ctrl)
    time.sleep(1)
    print('Zoomed out | {}'.format(i + 1))

time.sleep(10)
cookie = driver.find_element('id','bigCookie')

product_ids = [ f'product{i}' for i in range(11)]
product_ids.reverse()
print(product_ids)
while True:
    for i in range(1000):
        cookie.click()
    try:
        driver.find_element(By.ID, 'upgrade0').click()
    except:
        print('No upgrades in store!')

    for id in product_ids:
        element = driver.find_element(By.ID, id)
        while 'enabled' in element.get_attribute('class').split(' '):
            element.click()