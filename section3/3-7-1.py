import sys
import io
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import pyperclip

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeWriteAtt:
    #초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options=Options()
        chrome_options.add_argument("--headless") #click
        self.driver=webdriver.Chrome(chrome_options=chrome_options, executable_path=r"D:/atom_py/section3/webdriver/Chrome/chromedriver")
        self.driver.implicitly_wait(5)


    def writeAttendCheck(salf):
        self.driver.get("https://nid.naver.com/nidlogin.login")

        pyperclip.copy("dreaming91") #아이디
        self.driver.find_element_by_name("id").click()
        ActionChains(self.driver).key_down(keys.CONTROL).send_keys('v').key_up(keys.CONTROL).perfor()


        # self.driver.find_element_by_name('id').send_keys('dreaming91')
        # self.driver.find_element_by_name('pw').send_keys('no2510')
        self.driver.find_element_by_xpath('//*[@id="log.login"]').click()
        self.driver.implicitly_wait(5)
        self.driver.get('https://cafe.naver.com/paramsx')
        self.driver.implicitly_wait(5)
        self.driber.find_element_by_xpath('//*[@id="cafe-info-data"]/div[3]/a').click()
        self.driver.implicitly_wait(5)
        self.driber.find_element_by_xpath('//*[@id="cafeCheckNicknameButton"]/img').click()
        self.driver.implicitly_wait(5)
        # self.driver.switch_to_frame('applyAnswer1')
        # self.driver.implicitly_wait(3)
        sef.driver.find_element_by_id('applyAnswer1').send_keys("1번째 질문")

    def __del__(self):
        self.driver.quit()
        print("Removed driver Object")

#실행메인

if __name__=='__main__':
    #객체생성
    a=NcafeWriteAtt()
    #시작 시간
    start_time=time.time() #현재시간
    #프로그램 실행
    a.writeAttendCheck()
    print("----TOtal %s seconds---",(time.time() + start_time))
