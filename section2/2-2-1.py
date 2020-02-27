import sys
import io
import urllib.request as dw

sys.stdout= io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr= io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgUrl="https://pds.joins.com/news/component/htmlphoto_mmdata/201901/30/a0257ba6-3c0b-4fc2-b295-4c4ccfb0b862.jpg"
htmlUrl="https://www.google.com/"
savePath1="D:/atom_py/section2/img/test_cat1.jpg"
savePath2="D:/atom_py/section2/html/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)

print("다운로드 완료")

# 저장-> open
