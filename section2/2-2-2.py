import sys
import io
import urllib.request as dw

sys.stdout= io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr= io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgUrl="https://pds.joins.com/news/component/htmlphoto_mmdata/201901/30/a0257ba6-3c0b-4fc2-b295-4c4ccfb0b862.jpg"
htmlUrl="https://www.google.com/"


savePath1="D:/atom_py/section2/img/test_cat2.jpg"
savePath2="D:/atom_py/section2/html/index2.html"

# dw.urlretrieve(imgUrl, savePath1)
# dw.urlretrieve(htmlUrl, savePath2)
#
# f=dw.urlopen(imgUrl).read()
f2=dw.urlopen(htmlUrl).read()
# savefile1=open(savePath1, 'wb')
# savefile1.write(f)
# savefile1.close()
with open(savePath2,'wb') as savePath2:
    savePath2.write(f2)


print("다운로드 완료!")
