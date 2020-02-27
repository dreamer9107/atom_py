import sys
import io
import urllib.request
import urllib.parse


sys.stdout= io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr= io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


API="https://api.ipify.org"

values={
'format' : 'json'
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
