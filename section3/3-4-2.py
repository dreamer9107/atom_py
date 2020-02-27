import requests
import sys
import io
from bs4 import BeautifulSoup
import urllib.parse as rep
import parser
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


#로그인 유저정보
LOGIN_INFO = {
'user_id':'sorkwo',
'user_pw':'sorkwo@123!'
}

#Session 생성, with구문 안에서 유지
with requests.session() as s:
    login_req=s.post('https://user.ruliweb.com/member/login_proc',data=LOGIN_INFO)
    # HTML 소스 확인
    #print('login_req : ',login_req.text)
    # HTTP Header확인
    print('login_header : ',login_req.headers)

    #Resopnse 정상 확인
    if login_req.status_code == 200 and login_req.ok:
        print('로그인 성공')
        #권한이 필요한 게시판 게시글 가져오기
        post_one=s.get('https://mypi.ruliweb.com/mypi.htm?nid=732406&num=6102')
        #예외처리
        post_one.raise_for_status()
        print(post_one.text)
        #BeautifulSoup 선언
        soup = BeautifulSoup(post_one.text, "html.parser")

        res=soup.select('div.readcomment')
        for i in res:
            print(i.text)
