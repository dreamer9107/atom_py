import requests
import sys
import io
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


URL="https://www.wishket.com/accounts/login/"


with requests.session() as s:
    #Login 정보 Payload
    LOGIN_INFO={
    'identification':'dreamer91',
    'password':'rlatmdgus123!@#'
    }

    response=s.post(URL,data=LOGIN_INFO)
    #html 결과 확인
    print('response',response.text)
