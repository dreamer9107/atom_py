import sys
import io
import urllib.request
import urllib.parse
import urllib.request as dw


sys.stdout= io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr= io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


API="https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

values={
'ctxCd' : '1012'
}

print('before',values)

params=urllib.parse.urlencode(values)
print('after',params)

#요청 ulr 생성
url=API+"?"+params
print("요청 url : ",url)

data=urllib.request.urlopen(url).read()
text=data.decode('utf-8')
print(text)

mp4Url="https://tvetamovie.pstatic.net/libs/1273/1273252/1502a51e881e223deb91_20200122124722632.mp4-pBASE-v0-f97980-20200122124759073_1.mp4"
imgUrl="https://ssl.pstatic.net/tveta/libs/1260/1260649/19aabf7c9a09e0d9ed84_20200211140438611.jpg"


savePath1="D:/atom_py/section2/mp4/test_1.mp4"

savePath2="D:/atom_py/section2/img/test_1.html"

# dw.urlretrieve(imgUrl, savePath1)
# dw.urlretrieve(htmlUrl, savePath2)
#
# f=dw.urlopen(imgUrl).read()
f1=dw.urlopen(mp4Url).read()
f2=dw.urlopen(imgUrl).read()

# savefile1=open(savePath1, 'wb')
# savefile1.write(f)
# savefile1.close()
with open(savePath1,'wb') as savePath1:
    savePath1.write(f1)
with open(savePath2,'wb') as savePath2:
    savePath2.write(f2)

print("다운로드 완료!")
