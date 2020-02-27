import sys
import io
from selenium import webdriver
from fake_useragent import UserAgent

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')




driver=webdriver.PhantomJS("D:/atom_py/section3/webdriver/phantomjs/phantomjs")

driver.implicitly_wait(5)
driver.get('http://google.com')
driver.save_screenshot("D:/atom_py/section3/webdriver/phantomjs/website1.png")

driver.implicitly_wait(5)
driver.get('http://daum.net')
driver.save_screenshot("D:/atom_py/section3/webdriver/phantomjs/website1.png")
driver.quit()

print('스크린샷 완료')
