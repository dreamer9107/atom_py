import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="https://ssl.pstatic.net/tveta/libs/1257/1257046/6f9937499c1fb6de1051_20191209174450739.jpg"
mp4URL ="https://tvetamovie.pstatic.net/libs/1267/1267665/f14ca57526550471a27c_20191203173036264.mp4-pBASE-v0-f96042-20191203173227718.mp4"

savePath1 ="D:/BIG_DATA/web_project/naver_banner.jpg"
savePath2 ="D:/BIG_DATA/web_project/naver_banner.mp4"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(mp4URL).read()

saveFile1 = open(savePath1,'wb') # w : write , r : read , a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)



print("다운로드 완료!")
