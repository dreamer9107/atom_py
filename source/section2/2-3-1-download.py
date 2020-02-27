import urllib.request
from urllib.parse import urlparse
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.encar.com/"

mem = urllib.request.urlopen(url)

print(type(mem))
print("geturl :",mem.geturl())
print("status :",mem.status) # 200,404,403,500
# if status==403 :
#    print ("5분후에 다시 접속하세요")
# elif
print("headers :",mem.getheaders())
print("info :",mem.info(),"\n")
print("code :",mem.getcode(),"\n")
print("getcode :",mem.getcode())
print("read :",mem.read(10).decode('utf-8')) # print("read :",mem.read()) :전체 forward
print(urlparse('http://www.encar.co.kr?test=test').query)
