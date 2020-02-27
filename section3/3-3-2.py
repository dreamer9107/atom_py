import requests, json
import sys
import io


sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


payload1={'key1':'name1','key2':'name2'}
payload2=(('key','name1'),('key2','name2'))
payload3={'sime':'nice'}

# r=requests.put('http://httpbin.org/put',data=payload1)
# print(r.text)


r=requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)
