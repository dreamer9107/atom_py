import sys
import io
import urllib.request
from urllib.parse import urlparse


sys.stdout= io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr= io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


url="http://www.encar.com/"
mem=urllib.request.urlopen(url)

# print(type(mem))
# print("geturl : ",mem.geturl())
# print("status : ",mem.status)
#
# # 에러사항 뿌리기
# # if status==403:
# #     print("5분뒤에 다시 접속하세요")
# #
# # elif staus==500:
# #     print()
#
# print("header : ",mem.getheaders())
# print("info : ",mem.info())
# print("getcode : ",mem.getcode())
# print("read : ",mem.read())
print(urlparse(url).query())
