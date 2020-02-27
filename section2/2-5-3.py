from bs4 import BeautifulSoup
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

html="""
<html>
<body>
<ul>
<li><a href="http://www.naver.com">naver</a></li>
<li><a href="http://www.daum.net">daum</a></li>
<li><a href="http://www.daum.com">daum</a></li>
<li><a href="http://www.google.com">goole</a></li>
<li><a href="http://www.tistory.com">tistory</a></li>

</ul>
</body>
</html>
"""
soup=BeautifulSoup(html,"html.parser")
links=soup.find_all("a")
for a in links:
    print('a =>',a)
    href=a.attrs['href']
    text=a.string
    print(text,'>',href)
a=soup.find_all("a",string="daum")
b=soup.find('a')
c=a=soup.find_all("a",string=["naver","google"])
d=soup.find_all("a",limit=2)
print('soup : ',type(soup))
print('links : ',links)
print("a : ",a)
print('b : ',b)
print('c : ',c)
print('d :',d)
