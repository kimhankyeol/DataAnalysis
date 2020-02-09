from bs4 import BeautifulSoup

html="""
<html><body>
    <ul>
        <li><a href="naver.com">naver</a></li>
        <li><a href="daum.net">daum</a></li>
    </ul>
</body></html>
"""

#HTML 분석
soup = BeautifulSoup(html,'html.parser')

#find_all() 메서드로 추출하기
links = soup.find_all("a")

#링크 목록 출력하기 
for a in links:
    href = a.attrs['href']
    text = a.string
    print(text,">",href)