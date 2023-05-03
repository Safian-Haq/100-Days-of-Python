import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from constant import *

class InternetSpeedTwitterBot:



    def get_internet_speed(self):
        """Returns the upload and download speeds."""
        driver = webdriver.Edge(PATH_TO_DRIVER)
        driver.get(SPEED_URL)

        down_speed_value = None
        up_speed_value = None

        down_speed_element = driver.find_element(By.ID, 'speed-value')
        is_down_test_complete = False
        while not is_down_test_complete:
            if down_speed_element.get_attribute('class').split(' ')[-1] == 'succeeded':
                is_down_test_complete = True
                down_speed_value = down_speed_element.text
                print('Final down-speed: ', down_speed_value)

        driver.find_element(By.ID, 'show-more-details-link').click()

        up_speed_element = driver.find_element(By.ID, 'upload-value')
        is_up_test_complete = False
        while not is_up_test_complete:
            if up_speed_element.get_attribute('class').split(' ')[-1] == 'succeeded':
                is_up_test_complete = True
                up_speed_value = up_speed_element.text
                print('Final up-speed: ', up_speed_value)

        driver.close()
        return int(down_speed_value), int(up_speed_value)

    def tweet_at_provider(self, down_speed_value, up_speed_value):
        driver = webdriver.Edge(PATH_TO_DRIVER)
        tweet = f'My internet speed: DOWN {down_speed_value} | UP {up_speed_value} '
        driver.get(TWITTER_URL)

        time.sleep(5)
        login_input = driver.find_element(By.XPATH,
                                 '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                                 '2]/div/div/div/div[5]/label/div/div[2]/div/input')
        login_input.send_keys(EMAIL)
        next_button = driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                               '2]/div[2]/div/div/div/div[6]')
        next_button.click()
        time.sleep(5)

        try:
            username_input = driver.find_element(By.XPATH,
                                     '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                                     '2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            print('Unusual activity detected')
            username_input.send_keys(USERNAME)
            driver.find_element(By.XPATH,
                                     '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                                     '2]/div[2]/div/div/div/div/div'
                                     ).click()
        except NoSuchElementException:
            print('Unusual activity not detected.')

        time.sleep(5)
        password_input = driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                  '2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div['
                                                  '2]/div[1]/input')
        password_input.send_keys(PASSWORD)
        login_button = driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                                '2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        login_button.click()

        time.sleep(5)

        # Click tweet box
        driver.find_element(By.XPATH,
                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div['
                                 '2]/div[1]/div/div/div/div[2]/div['
                                 '1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div'
                                 ).click()

        driver.find_element(By.CSS_SELECTOR,
                                 'div[data-contents="true"]'
                                 ).send_keys(tweet)

        # send_keys(f'My internet speed: DOWN {down_speed_value} | UP {up_speed_value} ')

        driver.find_element(By.XPATH,
                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div['
                                 '2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span'
                                 ).click()

        time.sleep(10)
