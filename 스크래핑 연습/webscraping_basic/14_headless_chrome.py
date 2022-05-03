# %% Headless Chrome

'''
    selenium과 beautifulsoup을 활용한 scraping은 강력함.
    그러나 selenium을 활용한 webdriver가 매번 브라우저를 띄워주는건 리소스 낭비.
    브라우저를 띄우지 않고 background에서 chrome을 동작시키는 것이 headless chrome.
    
    주의점) headless chrome는 user-agent값이 headless chrome가 됨.
        그래서 user-agent값을 보고 접속을 차단할 수도 있음.
        이 경우 options의 argument로 user-agent값을 추가하면 됨.
'''

from selenium import webdriver

# Chrome webdriver의 headless 설정을 True로 변경
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

# 로딩시간 대기를 위한 프레임워크
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 크롬 창 열기(추가적으로 options 지정)
browser = webdriver.Chrome("./chromedriver.exe", options=options)
browser.maximize_window()  # 창 최대

# 네이버 항공권으로 이동
url = "https://flight.naver.com/"
browser.get(url)  # url로 이동

# 도착지 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/button[1]").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[2]").click()

# 가는 날, 오는날 선택 (4/23, 4/30)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# 날짜 선택 로딩창 시간이 좀 걸림.
# 최대 10초 대기. 만약 아래에 해당하는 XPATH의 element 등장한다면 바로 다음 진행
# 조건에 따라 XPATH 이외에 class, id 등으로도 사용 가능
try:
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[7]/button")))
    # 성공시 다음 동작 수행
except:
    browser.quit()
    # 실패시 브라우저 종료
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[7]/button").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[7]/button").click()

# 항공권 검색 클릭
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/button").click()

# 최대 20초 대기. 만약 아래에 해당하는 XPATH의 element가 등장한다면 바로 다음 진행
try:
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]/div/button")))
except:
    browser.quit()
element = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]/div/div[1]")
print(element.text)

# headless chrome이 잘 작동했는지 확인하기 위한 스크린 샷 촬영
browser.get_screenshot_as_file("naver_flight.jpg")
browser.quit()