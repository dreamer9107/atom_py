import requests
import sys
import io
from bs4 import BeautifulSoup
import urllib.parse as rep
import parser
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


with requests.session() as s:
    post_one=s.get("http://www.cgv.co.kr/movies/")
    post_one.raise_for_status()
    # print(post_one.text)
    #BeautifulSoup 선언
    soup = BeautifulSoup(post_one.text, "html.parser")

    res=soup.select('#contents > div.cols-rank > div.col-rank-search > div > ol > li > a > strong')
    # print(res.text)
    for i,e in enumerate (res,1):
        print('실시간 인기영화: ',i,e.text)
