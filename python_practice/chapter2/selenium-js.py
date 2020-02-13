#셀레니움이 다양한 기능을 제공하지만 원하는 기능이 없을수도 있음
#이럴때는 execute_script() 메서드를 사용함

from selenium import webdriver

browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

#적당한 웹페이지 열기
browser.get("https://google.com")

#자바스크립트 실행하기
r = browser.execute_script("return 100+50")
print(r)