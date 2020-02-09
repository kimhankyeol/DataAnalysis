# 매개변수를 추가해 요청 전송하는 방법 ( 기상청 )
import urllib.request
import urllib.parse
#데이터 읽기
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stnId':'108'
}

params = urllib.parse.urlencode(values)
url = API+"?"+params
print(url)
#다운로드 
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)





