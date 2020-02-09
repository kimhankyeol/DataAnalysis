#BeatifulSoup 으로 스크레이핑
#스크레이핑이란웹사이트에서 데이터를 추출하고 원하는 정보를 추출하는것 
# 파이썬 스크레이핑 할떄 대표적으로 BeatifulSoup 라이브러리를 이용함 
# 간단하게 HTML XML 정보를 추출할 수 있음

#BeatifulSoup 설치 

# 파이썬 라이브러리를 설치할때는 pip 명령어를 사용함
# pip 란 파이썬 패키지 관리 시스템임
# 파이썬 패키지는 Python Package Index(PyPI) 
# 설치 명령어 pip3 install beatifulsoup4      // pip3 는 파이썬3 버전

# 설치 명령어 안될시 
#https://pypi.python.org/pypi/beautifulsoup4 여기서 관련 whl 파일을 다운로드 함
# 다운로드 위치에서  python -m pip install whl 파일명 

#라이브러리 읽기
from bs4 import BeautifulSoup

#분석하고 싶은 html
html = """
<html><body>
    <h1>스크레이핑이란?</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는것</p>
</body></html>
"""

#HTML 분석
soup = BeautifulSoup(html,'html.parser')

#원하는 부분 추출
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling #next_sibling 한번하면 p태그뒤에있는 공백 추출됨 2번해야 p 2번째 줄
 
print("h1="+h1.string)
print("p1="+p1.string)
print("p2="+p2.string)