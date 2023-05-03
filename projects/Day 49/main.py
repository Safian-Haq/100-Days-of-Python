import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

USERNAME = os.environ.get('LINKEDIN_USERNAME')
PASSWORD = os.environ.get('LINKEDIN_PASSWORD')

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3376287978&geoId=101022442&keywords=consulting&location=Pakistan&refresh=true'

PATH_TO_DRIVER = 'C:\Selenium\msedgedriver.exe'

if __name__ == '__main__':
    driver = webdriver.Edge(PATH_TO_DRIVER)

    driver.get(URL)

    # Login
    driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()
    time.sleep(10)

    driver.find_element(By.ID, 'username').send_keys(USERNAME)
    driver.find_element(By.ID, 'password').send_keys(PASSWORD)

    driver.find_element(By.CSS_SELECTOR, '.login__form_action_container button').click()

    time.sleep(10)

    # Save the first job
    driver.find_element(By.CSS_SELECTOR, '.jobs-save-button').click()
