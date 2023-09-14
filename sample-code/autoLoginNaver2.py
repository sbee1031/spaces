from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import getpass
import time

# 이 파일로 실행 시 자동로그인 안 됨, pyperclip으로 복붙해야 함

# URL
URL = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'

# ID/PW
user_id = input('아이디 입력: \n')
user_pw = getpass.getpass('비밀번호 입력: \n')

# Chrome Options
options = webdriver.ChromeOptions()
options.add_argument("headless")
#options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get(url=URL)

login_id = driver.find_element(by=By.ID, value="id")
login_pw = driver.find_element(by=By.ID, value="pw")
login_remember_id = driver.find_element(by=By.CLASS_NAME, value="keep_check")
login_enter = driver.find_element(by=By.ID, value="log.login")

login_id.send_keys(user_id)
login_pw.send_keys(user_pw)
login_remember_id.click()
login_enter.click()
driver.implicitly_wait(5)

driver.get_screenshot_as_file('naver_main_headless.png')

driver.quit()