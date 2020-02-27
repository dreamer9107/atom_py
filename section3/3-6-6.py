import sys
import io
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
option = Options()
option.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=option, executable_path=r"D:/atom_py/section3/webdriver/Chrome/chromedriver")

driver.get("http://www.encar.com/dc/dc_carsearchlist.do?carType=kor&searchType=model&TG.R=A#!")
driver.implicitly_wait(3)


carClsP = driver.find_elements_by_class_name("cls")
carDtlP = driver.find_elements_by_class_name("dtl")
carPrcP = driver.find_elements_by_class_name("prc")

for i in range(len(carClsP)) :
    print("{}번째 차 : {} {} \n,가격 : {}".format(i+1, carClsP[i].text, carDtlP[i].text,carPrcP[i].text))
driver.quit()
