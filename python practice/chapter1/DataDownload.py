# 파이썬은 웹사이트 에 있는 데이터를 추출하기 위해 urllib 라이브러리를 사용 
# 이 라이브러리를 이용하면 HTTP or FTP 를 사용해 데이터를 다운로드 할 수 있음
#urllib 은 URL을 다루는 모듈을 모아 놓은 패키지 라 할수 있음
# 그중 urllib.request 모듈은 웹사이트에 있는 데이터에 접근하는 기능을 제공 하고 인증, 리다이렉트 쿠키 처럼 인터넷을 이용한 다양한 요청과 처리를 지원함

#라이브러리 읽어들이기
import urllib.request

# URL과 저장경로 지정하기
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"
###################################################
#다운로드 
#1.urlretrieve 를 이용하면 파일을 바로저장 
##
#urllib.request.urlretrieve(url,savename)
#print("저장완료")
##
###################################################
#2. 메모리위에 올리고 난후 파일로 저장하기 
#request.urlopen() 을 이용하면 곧바로 파일로 저장하는게 아니라 데이터를 파이썬 메모리 위에 올릴수 있음
# 메모리 위에 데이터를 올리고 파일로 저장
#urlopen으로 url 리소스를 열고 read() 메서드로 데이터를 읽어들임
#파일을 여는 open()함수로 파일을 열고 w 는 쓰기 , b 는 바이너리 
#write()로 저장
mem = urllib.request.urlopen(url).read()
with open(savename,mode="wb") as f:
    f.write(mem)
    print("메모리 올린후 저장완료")