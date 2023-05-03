from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import *
from insta_follower import InstaFollower

if __name__ == '__main__':
    bot = InstaFollower()
    bot.login()
    bot.follow_all_followers(TARGET_INSTA_ACCOUNT_URL)

