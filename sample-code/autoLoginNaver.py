from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import getpass
import requests
import json

# URL
URL = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'

# ID/PW 입력받기
user_id = input('아이디 입력: \n') 
user_pw = getpass.getpass('비밀번호 입력: \n') 

# 창 숨기기
options = webdriver.ChromeOptions()
#options.add_argument("headless")
#options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=options)

driver.get(url=URL)
driver.implicitly_wait(time_to_wait=3)

login_id = driver.find_element(by=By.ID, value="id")
login_id.click()
pyperclip.copy(user_id)
login_id.send_keys(Keys.COMMAND, 'v')

login_pw = driver.find_element(by=By.ID, value="pw")
login_pw.click()
pyperclip.copy(user_pw)
login_pw.send_keys(Keys.COMMAND, 'v')

login_enter = driver.find_element(by=By.ID, value="log.login")
login_enter.click()

#el = driver.find_element(By.XPATH, "//*")
#print(el.get_attribute("outerHTML"))

driver.get("https://www.naver.com")
#el = driver.find_element(By.XPATH, "//*")
# print(el.get_attribute("outerHTML"))

#print(driver.get_cookies())

driver.quit()
