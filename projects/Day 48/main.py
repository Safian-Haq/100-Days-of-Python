from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = 'C:\Selenium\chromedriver.exe'
driver = webdriver.Chrome(CHROME_DRIVER_PATH)


## Amazon Product Price Example
#
# URL = 'https://www.amazon.co.uk/Sony-WF-C500-Wireless-Headphones-Built-Black/dp/B09FKGJ1CB/ref' \
#               '=d_bmx_dp_cdjieemo_sccl_1_3/262-3215502-2054313?pd_rd_w=FKNxO&content-id=amzn1.sym.89757917-7d86-4c30' \
#               '-a82b-c76fe5b7d5a8&pf_rd_p=89757917-7d86-4c30-a82b-c76fe5b7d5a8&pf_rd_r=TARPZPHAE320QRPATHHF&pd_rd_wg' \
#               '=IfoOi&pd_rd_r=803fa2a6-3285-459c-8eb4-842b3262332c&pd_rd_i=B09FKGJ1CB&th=1'
#
#
# driver.get(URL)
#
# # Removes cookie pop up
# driver.find_element(By.ID,'sp-cc-rejectall-link').click()
# driver.maximize_window()
# element = driver.find_element(By.CSS_SELECTOR,'.priceToPay')
#
# print(element.text)

## Python.org search example
#
# URL = 'https://python.org'
#
# driver.get(URL)
# search_bar = driver.find_element(By.NAME, 'q')
# search_bar.send_keys('PEP 8')
# submit_button = driver.find_element(By.NAME, 'submit')
# submit_button.click()

## Python.org docs example
#
# URL = 'https://python.org'
#
# driver.get(URL)
#
# doc_link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
# print(doc_link.text)

## Python.org xPath example
#
# URL = 'https://python.org'
#
# driver.get(URL)
#
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

## Python.org Upcoming Events

# URL = 'https://python.org'
#
# driver.get(URL)
#
# events_list = driver.find_element(
#     By.CSS_SELECTOR, '.event-widget div ul'
# ).find_elements(
#     By.CSS_SELECTOR, 'li'
# )
# resutls = {}
# for i in range(len(events_list)):
#     event = events_list[i]
#     dt = event.find_element(By.CSS_SELECTOR, 'time').get_attribute('datetime').split('T')[0]
#     event_name = event.find_element(By.CSS_SELECTOR, 'a').text
#     resutls[i] = {'time': dt, 'name': event_name}
#
# print(resutls)
# driver.close()
