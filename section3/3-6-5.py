import sys
import io
from selenium import webdriver
import time

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

driver=webdriver.Chrome("D:/atom_py/section3/webdriver/chrome/chromedriver")
driver.set_window_size(1920,1080)
driver.implicitly_wait(3)
driver.get("https://www.wishket.com/accounts/login/")
time.sleep(5)
driver.implicitly_wait(3)
driver.find_element_by_name('identification').send_keys('dreamer91')
driver.implicitly_wait(3)
driver.find_element_by_name('password').send_keys('rlatmdgus123!@#')
driver.implicitly_wait(3)
#로그인
driver.find_element_by_xpath('//*[@id="submit"]').click()
