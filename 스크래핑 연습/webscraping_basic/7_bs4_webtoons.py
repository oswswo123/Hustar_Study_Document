# %% beautifulsoup4 (webtoon 예)

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
response = requests.get(url)
response.raise_for_status()

# lxml : parser
soup = BeautifulSoup(response.text, "lxml")

# find_all() : parameter로 준 조건에 일치하는 모든 element를 return
# 네이버 웹툰 목록 가져오기(class의 attribute가 title인 모든 element return)
cartoons = soup.find_all("h6", attrs={"class":"title"})

for cartoon in cartoons:
    print(cartoon.a.get_text())

# %% 가우스전자 웹툰 목록 가져오기

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
response = requests.get(url)
response.raise_for_status()

# lxml : parser
soup = BeautifulSoup(response.text, "lxml")

GEs = soup.find_all("td", attrs={"class":"title"})

for GE in GEs:
    # tag의 하위 tag는 .(온점)을 이용해 접근 가능
    # tag의 attribute는 dictionary처럼 추출 가능
    link = "https://comic.naver.com" + GE.a["href"]
    print(GE.a.get_text(), link)

# %% 가우스전자 웹툰 평점 가져와서 평균 계산하기

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
response = requests.get(url)
response.raise_for_status()

# lxml : parser
soup = BeautifulSoup(response.text, "lxml")

GE_rates = soup.find_all("div", attrs={"class":"rating_type"})

sum_of_rate = 0
for GE_rate in GE_rates:
    print(GE_rate.strong.get_text())
    # 이거 말고 이거도 가능함
    print(GE_rate.find("strong").get_text())
    print()
    sum_of_rate += float(GE_rate.find("strong").get_text())

print("평균 평점 : {:.3f}".format(sum_of_rate / len(GE_rates)))
