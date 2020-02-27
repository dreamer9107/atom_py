from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# User-agent : 사용자를 대신해서 인터넷에 접속하는 소프트웨어, 즉 브라우저
# Mozilla/5.0 : 파이썬으로도 사용자 에이젼트 헤더를 바꾸는 게 가능하다.
# 즉 윈도우에서 리눅스 인척 또는 403에러 솔루션
# opener = req.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# req.install_opener(opener)

# HTML 가져오기
base = "https://search.naver.com/search.naver?where=image&query="
quote = rep.quote_plus("사자")
url = base + quote

res = req.urlopen(url)
savePath ="C:\\imagedown\\" #c:/imagedown/과 동일 폴더 생성
try:
    if not(os.path.isdir(savePath)): # 디렉토리가 있는지 확인 : 없디면 생성
        os.makedirs(os.path.join(savePath))
except OSError as e: #디렉토리가 있다면
    if e.errno != errno.EEXIST: # EEXIST :file이 존재할 경우에
        print("Failed to create directory!!!!!")
        raise #컴파일 하여 폴더 생성확인

soup = BeautifulSoup(res, "html.parser")

li_list = soup.select("div.img_area _item > a.thumb._thumb > img")
for i, div in enumerate(li_list,1):
    #print(div) #'data-source'확인
    #print(div['src']) #이미지 확인 불가능한 src
    #print("div =", div['data-source']) #사용가능한  url 확인
    fullfilename = os.path.join(savePath, savePath+str(i)+'.jpg')
    # print(fullfilename)
    req.urlretrieve(div['data-source'],fullfilename)
    print(i)
    
print("다운로드 완료")
