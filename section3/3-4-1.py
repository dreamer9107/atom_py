import requests, json
import sys
import io
from bs4 import BeautifulSoup
import urllib.parse as rep

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

#Session 생성, with구문 안에서 유지
with requests.session() as s:
    # 게시글 가져오기
    post_one=s.get('https://bbs.ruliweb.com/market/board/1020/read/37546')
    #예외 발생
    post_one.raise_for_status()
    #예외발생 print
    print(post_one.raise_for_status())
    #Beautifulsoup 선언 및 확인
    soup = BeautifulSoup(post_one.text,"html.parser")
    g=soup.select("#board_read > div > div.board_main > div.board_main_view > div.view_content > div > p")
    print('g---------------------',g )
    for i in g:
        print(i.string)
