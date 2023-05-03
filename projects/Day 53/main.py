from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time

MAX_RENT_PRICE = '25000'
NUMBER_OF_BEDS = '0'

FORM_LINK = 'https://forms.gle/6A2dtfMqjYa4KPkH7'

BASE_URL = 'https://www.zameen.com'
SEARCH_HOME_URL = 'https://www.zameen.com/Rentals/Karachi-2-1.html?'

PATH_TO_DRIVER = 'C:\Selenium\msedgedriver.exe'

def get_search_url(page_number: int):
    return f'https://www.zameen.com/Rentals/Karachi-2-{page_number}.html'

if __name__ == '__main__':

    headers = {
        'price_max': MAX_RENT_PRICE,
        'beds_in': NUMBER_OF_BEDS
    }

    data = []
    skipped_count = 0
    current_page = 1
    next_search_page = True
    while next_search_page:

        print(f'Page {current_page}\n')

        response = requests.get(get_search_url(current_page), params=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')

        # Extract information from each listing
        properties = soup.find_all(name='li', attrs={'aria-label': 'Listing'})
        for element in properties:
            try:
                address = element.findNext(name='div', attrs={'aria-label': 'Location'}).text
                price = element.findNext(name='span', attrs={'aria-label': 'Price'}).text
                property_link = element.find_next(name='a', attrs={'aria-label': 'Listing link'}).get('href')
                property_link = f'{BASE_URL}{property_link}'
                print(f'{price} | {address} | {property_link}')
                data.append((price, address, property_link))
            except AttributeError:
                skipped_count+= 1
                print(f'Skipped # of listings: {skipped_count}')

        # Check if the next page exits
        try:
            next_page_link = soup.find(name='a', attrs={'title': f'Page {current_page+ 1}'}).get('href')
            current_page += 1

        except AttributeError:
            print('Next page not found!\nScrapping complete')
            next_search_page = False

    driver = webdriver.Edge(PATH_TO_DRIVER)

    # For each listing fill the form
    for listing in data:
        driver.get(FORM_LINK)

        # Input address
        address_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="i1"]')
        address_input.click()
        # Need to wait to make the input interactable
        time.sleep(1)
        address_input.send_keys(listing[1])

        # Input price per month
        price_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="i5"]')
        price_input.click()

        time.sleep(1)
        price_input.send_keys(listing[0])

        # Input price per month
        link_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="i9"]')
        link_input.click()
        time.sleep(1)

        for ele in listing[2]:
            link_input.send_keys(ele)

        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

        time.sleep(3)
