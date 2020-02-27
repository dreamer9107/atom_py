import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

#1.옵션 적용
chrome_option=Options()
chrome_option.add_argument("--headless") #CLI


driver=webdriver.Chrome(chrome_options=chrome_option,executable_path=r'D:/atom_py/section3/webdriver/chrome/chromedriver')
driver.set_window_size(1920,1080)
driver.get("https://google.com")
time.sleep(5)
driver.save_screenshot("D:/atom_py/section3/webdriver/chrome/website3.png")
driver.get("https://daum.net")
time.sleep(5)
driver.save_screenshot("D:/atom_py/section3/webdriver/chrome/website4.png")
driver.quit()


print('스크린샷 완료')
