from bs4 import BeautifulSoup

#분석하고 싶은 html
html = """
<html><body>
    <h1 id="title">스크레이핑이란?</h1>
    <p id="body">웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는것</p>
</body></html>
"""

#HTML분석

soup =BeautifulSoup(html,'html.parser')

#find() 메서드로 원하는 부분 추출하기

title = soup.find(id="title")
body = soup.find(id="body")
 

#텍스트 출력
print("title= "+title.string)
print("body"+body.string)