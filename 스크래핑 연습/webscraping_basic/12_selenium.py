# %% selenium을 활용한 자동 로그인

from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")

# 1. 네이버로 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭(로그인 창으로 이동)
element = browser.find_element_by_class_name("link_login")
element.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id 입력(일부러 틀린 것)")
browser.find_element_by_id("pw").send_keys("naver_password 입력(일부러 틀린 것)")

# 4. 로그인 버튼 클릭(로그인 실행)
browser.find_element_by_class_name("btn_login").click()

# 5. html 정보 출력
print(browser.page_source)

# 6. 브라우저 종료
# browser.close()  # 현재 탭만 종료
browser.quit()  # 전체 브라우저 종료