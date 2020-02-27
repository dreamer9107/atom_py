import sys
import io
from selenium import webdriver
from fake_useragent import UserAgent
import time
from selenium.webdriver.firefox.options import Options

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

#1.옵션 적용
firefox_option=Options()
firefox_option.add_argument("--headless") #CLI

driver=webdriver.Firefox(firefox_options=firefox_option,executable_path="D:/atom_py/section3/webdriver/firefox/geckodriver")

#2. GUI
#driver=webdriver.Firefox('D:/atom_py/section3/webdriver/firefox/geckodriver")

driver.set_window_size(1920,1080)
driver.get("https://google.com")
# time.sleep(5)
driver.save_screenshot("D:/atom_py/section3/webdriver/firefox/website1.png")
driver.get("https://daum.net")
# time.sleep(5)
driver.save_screenshot("D:/atom_py/section3/webdriver/firefox/website2.png")
driver.quit()


print('스크린샷 완료')
