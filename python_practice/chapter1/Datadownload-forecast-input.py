#!/usr/bin/env python3

#매개변수를 명령줄에서 지정하기
#현재 프로그램은 매개변수를 코드에 입력해야 하므로 다른 지역의 정보를 알아내고 싶을때는 프로그램을 열고 수정해야함

#라이브러리
import sys
import urllib.request as req
import urllib.parse as parse

#명령줄 매개변수 추룰
if len(sys.argv) <= 1 :
    print("USAGE : download-forecast-input-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

#매개변수를 URL 인코딩
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stnId':regionNumber
}

params = parse.urlencode(values)
url = API + "?" +params

print("url=",url)

#다운로드함
data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)


# 실행 
# python 파일명.py 지역번호     예 ) python Datadownload-forecast-inputa 108 109 184