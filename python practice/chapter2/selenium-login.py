from selenium import webdriver
USER="<USER>"
PASS="<PASS>"
#PhantomJS 드라이버 추출
browser =webdriver.PhantomJS()
browser.implicitly_wait(3)

#로그인  페이지 접근
url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("login  access")

#텍스트 박스에 아이디와 비밀번호 입력하기
e = browser.find_element_by_id("id")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)

#입력양식 전송해서 로그인하기
form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("login button click")

#쇼핑페이지의 데이터 가져오기
browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

#쇼핑목록 출력하기
products = browser.find_elements_by_css_selector(".p_info span")
print(products)

#쇼핑목록 출력하기
for product in products:
    print("-",product.text)
