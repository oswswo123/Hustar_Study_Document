# %% beautifulsoup (coupang 예제)

# 노트북 이름 출력
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=178155&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

for item in items:
    print(item.find("div", attrs={"class":"name"}).get_text())

# %% 이름, 가격, 평점, 리뷰 수 추출

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=178155&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

for item in items:
    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("<광고 상품 제외>\n")
        continue
    
    item_name = item.find("div", attrs={"class":"name"}).get_text()
    
    # 애플제품 제외
    if ("Apple" in item_name) or ("맥북" in item_name):
        print("<애플 제품 제외>\n")
        continue
    
    item_price = item.find("strong", attrs={"class":"price-value"}).get_text()
    
    
    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    item_rate = item.find("em", attrs={"class":"rating"})    
    if item_rate:
        item_rate = item_rate.get_text()
    else:
        print("<평점 없는 상품 제외>\n")
        continue
        
    item_reviewnum = item.find("span", attrs={"class":"rating-total-count"})
    if item_reviewnum:
        item_reviewnum = item_reviewnum.get_text()
        item_reviewnum = item_reviewnum[1:-1]
    else:
        print("<리뷰 없는 상품 제외>\n")
        continue
    
    if float(item_rate) >= 4.5 and int(item_reviewnum) >= 100:
        print(item_name, item_price, item_rate, item_reviewnum, sep="\n", end="\n\n")