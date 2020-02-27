import urllib.request
import urllib.parse
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API = "https://api.ipify.org"

values = {
    'format': 'json' # 'format': 'jsonp'로도 확인
}
print('before',values) # 여기까지 코딩후 확인 ->형식이 맞지 않음을 확
params = urllib.parse.urlencode(values)
print('after',params)
#요청 URL 생성
url = API + "?" + params
print("요청 url=", url)
#읽기
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
