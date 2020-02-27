import requests
import sys
import io
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


URL="https://www.wishket.com/accounts/login/"
ua=UserAgent()

with requests.session() as s:
    #Login 정보 Payload
    s.get(URL)
    LOGIN_INFO={
    'identification':'dreamer91',
    'password':'rlatmdgus123!@#',
    'csrfmiddlewaretoken':s.cookies['csrftoken']
    }

    response=s.post(URL,data=LOGIN_INFO,headers={'User-Agent':str(ua.chrome),'Referer':'https://www.wishket.com/accounts/login/'})
    #html 결과 확인
    # print('response',response.text)
    # if response.status_code == 200 and reponse.ok:
    soup = BeautifulSoup(response.text,'html.parser')
    login = soup.select('#wrap > div.page > div.sidebar > div > div.partners-history')
    for i in login:
        print(i.text)
