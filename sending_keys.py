# if you want to bypass captchas simply just pay for api
# that automates the solving of captchas.

from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://phptravels.com/demo/')
driver.implicitly_wait(5)

first_name = driver.find_element_by_xpath('//*[@id="Main"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[1]')
last_name = driver.find_element_by_xpath('//*[@id="Main"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[2]')
business_name = driver.find_element_by_xpath('//*[@id="Main"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[3]')
email = driver.find_element_by_xpath('//*[@id="Main"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[4]')

first_name.send_keys('Koa')
last_name.send_keys('Chang')
business_name.send_keys(Keys.NUMPAD1,Keys.NUMPAD5,'x',Keys.MULTIPLY,' @gmail.com',Keys.DECIMAL)
email.send_keys('mpono000@gmail.com')

time.sleep(25)
driver.quit()

# css selector
# login = driver.find_element_by_css_selector('a[href = "https://phptravels.org/"]')
# login.click()










