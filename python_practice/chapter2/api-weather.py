import requests
import json


#API키를 지정함
apikey = "APIKEY를 발급받아 사용해주세요"

#날씨를 확인할 도시 지정
cities = ["Seoul,KR","Tokyo,JP","New York,US"]

#API지정
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

#켈빈 온도를 섭씨온도로 변환하는 함수
k2c = lambda k:k-273.15

#각 도시의 정보 추출하기
for name in cities:
    #API URL 구성
    url = api.format(city=name,key=apikey)
    #API 요청을 보내 데이터 추출
    r = requests.get(url)
    #결과를 JSON 형식
    data = json.loads(r.text)

    #결과 출력 
    print("~~~도시=",data["name"])
    print("|날씨=",data["weather"][0]["description"])
    print("|최저기온=",k2c(data["main"]["temp_min"]))
    print("|최고기온=",k2c(data["main"]["temp_max"]))    
  #풍향 습도 기압 풍속  의 정보도 받을수있음
