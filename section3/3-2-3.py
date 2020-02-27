import requests, json
import sys
import io


sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

s=requests.session()
r=s.get("http://httpbin.org/stream/20")
print(r.text)
print(r.encoding) # 인코딩이 안되있으면 None값 변화

if r.encoding==None:
    r.encoding='utf-8' #utf-8로 인코딩

print(r.encoding) # utf-8

for line in r.iter_lines(decode_unicode=True):
    print(line)
    b=json.loads(line)
    for e in b.keys():
        print("key: ",e,"values: ",b[e])
