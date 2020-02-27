from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://finance.naver.com/sise/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

top = soup.select("#siselist_tab_0 > tr")

for e in top:
    print(e)

for e in top:
    print(e.find("a"))
# # none은  "a"태그가 없음을 표시

# 유형 1
# none 값은 무시하고 프린트를 안하므로 번호가 맞지않음
i = 1
for  e in (top):
    if e.find("a") is not None: #  title 이 tltle로 코딩되어 있음
        print(i,e.select_one(".tltle").string)
        i=i+1



# 유형 2
print('Top 10 종목명 출력')
for i, e in enumerate(top):
    if e.find("a") is not None: #  title 이 tltle로 코딩되어 있음
        i-=1
        if i>=9 :
            i=i-3
        print(i,e.select_one(".tltle").string)

print('-----------------------')
print('Top 10 현재가 출력')
i = 1
for e in top:
    if e.find("a") is not None:
        print(i,e.select_one(".tltle").string,"=", \
        e.select_one("td:nth-of-type(5)").string) # 현재가 출력
        i += 1
# td:nth-of-type(5) :td의 자식중 5번째
