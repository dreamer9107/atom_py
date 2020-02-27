from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser') # html 초기화

print('prettify',soup.prettify())
a = soup.find_all("a", string="daum")
b = soup.find_all(string=["naver", "daum"])
c = soup.find_all("a", limit=2) # limit=0 전체가져오기
d=soup.find("a") #첫번째 a태그만 검색
print('a',a)
print('b',b)
print('c',c)
print('d',d)
links = soup.find_all("a") # a태그의 내용을 한번에 찾아오기
print('links',links)
# 출력
for a in links:
    print('a',type(a),a)
    href = a.attrs['href'] # 딕셔너리로 리턴해야하므로 href키 사용
    text = a.string
    print(text, ">", href)
