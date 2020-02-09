#ip확인 api로 접근해서 클라이언트 접속 결과 출력
import urllib.request

#데이터 읽기
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
#read()읽은 데이터는 바이너리임
data = res.read()

#바이너리를 문자열로 변환하기
text = data.decode("utf-8")
print(text)