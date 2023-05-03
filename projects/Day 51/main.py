from selenium import webdriver
from selenium.webdriver.common.by import By
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 40
PROMISED_UP = 10


PATH_TO_DRIVER = 'C:\Selenium\msedgedriver.exe'


if __name__ == '__main__':
    bot = InternetSpeedTwitterBot()

    # speeds = bot.get_internet_speed()
    # if speeds[0] < PROMISED_DOWN:
    #     bot.tweet_at_provider(speeds[0], speeds[1])

    # Test code
    speeds = [10, 10]
    if speeds[0] < PROMISED_DOWN:
        bot.tweet_at_provider(speeds[0], speeds[1])
