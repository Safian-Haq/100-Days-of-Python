import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from constants import *


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Edge(PATH_TO_DRIVER)

    def login(self):
        self.driver.get(LOGIN_URL)
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Phone number, username, or email"]').send_keys(
            USERNAME)
        self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Password"]').send_keys(PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(5)

    def follow_all_followers(self, target_account_url):
        self.driver.execute_script(f'window.open("{target_account_url}","_blank");')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)
        pop_up_window = self.driver.find_element(By.CLASS_NAME, '_aano')

        while True:
            # Generate list of buttons
            follow_button_list = pop_up_window.find_elements(By.CSS_SELECTOR, 'button[type="button"]')

            for button in follow_button_list:

                # Validations for if the button is already pressed
                if button.is_displayed() and button.text == 'Follow' and button.get_attribute('color') != 'green':

                    # Click works but, it's kind of creepy :/
                    # Change color to green instead
                    # button.click()
                    
                    self.driver.execute_script('arguments[0].style.backgroundColor = "green"', button)

                    time.sleep(1)

            # Scroll the view
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window
            )
            time.sleep(2)

