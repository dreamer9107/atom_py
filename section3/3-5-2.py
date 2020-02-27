from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import os
import json
from fake_useragent import UserAgent

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')



#Fake headers
ua=UserAgent()

#헤더 선언
headers={
    'User-Agent':ua.ie,
    'Referer':'https://finance.daum.net/'
}
#다음 주식 요청 url
url="https://finance.daum.net/api/search/ranks?limit=10"
# print(request.get_method()) #Post or Get 확인
#요청
res = req.urlopen(req.Request(url,headers=headers)).read().decode('utf-8')
print('res',res)

rank_json = json.loads(res)['data']

# print('중간확인 : ', rank_json.'\n')
for elm in rank_json:
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'],elm['tradePrice'],elm['name']),)
