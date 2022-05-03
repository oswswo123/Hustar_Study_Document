# %% selenium을 활용한 자동 항공권 예약

# selenium을 이용해 가져온 web data를 bs4를 활용해 정리하려면
# <webdriver 객체>.page_source 로 가져오면 됨.
# ex. soup = BeautifulSoup(browser.page_source, "lxml")

from selenium import webdriver

# 로딩시간 대기를 위한 프레임워크
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 크롬 창 열기
browser = webdriver.Chrome("./chromedriver.exe")
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
browser.quit()