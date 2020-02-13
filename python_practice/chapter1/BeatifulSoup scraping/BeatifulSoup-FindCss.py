from bs4 import BeautifulSoup

html="""
<html><body>
    <div id="meigen">
        <h1>h1 입니다</h1>
        <ul class="items">
            <li>li 1 입니다</li>
            <li>li 2 입니다</li>
            <li>li 3 입니다</li>
        </ul>
    </div>
</body></html>
"""

#html 분석

soup = BeautifulSoup(html,'html.parser')

#필요한 부분을 css 쿼리로 추출
#타이틀 추출
h1 = soup.select_one("div#meigen > h1").string
print("h1 = ",h1)

#목록부분 추출
li_list = soup.select("div#meigen > ul.items > li")

for li in li_list :
    print("li=",li.string)