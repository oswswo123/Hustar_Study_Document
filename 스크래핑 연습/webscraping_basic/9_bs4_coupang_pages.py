# %% 여러 페이지에서 추출

import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}

for repeat in range(1, 6):
    print("page {}".format(repeat), end="\n\n")
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=178155&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(repeat)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "lxml")
    
    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    
    for item in items:
        # 광고 제품은 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            continue
        
        item_name = item.find("div", attrs={"class":"name"}).get_text()
        
        # 애플제품 제외
        if ("Apple" in item_name) or ("맥북" in item_name):
            continue
        
        item_price = item.find("strong", attrs={"class":"price-value"})
        if item_price:
            item_price = item_price.get_text()
        else:
            continue
        
        
        # 리뷰 600개 이상, 평점 4.5 이상 되는 것만 조회
        item_rate = item.find("em", attrs={"class":"rating"})    
        if item_rate:
            item_rate = item_rate.get_text()
        else:
            continue
            
        item_reviewnum = item.find("span", attrs={"class":"rating-total-count"})
        if item_reviewnum:
            item_reviewnum = item_reviewnum.get_text()
            item_reviewnum = item_reviewnum[1:-1]
        else:
            continue
        
        
        if float(item_rate) >= 4.5 and int(item_reviewnum) >= 600:
            item_link = item.find("a", attrs={"class":"search-product-link"})["href"]
            item_link = "https://www.coupang.com" + item_link
            print(item_name, item_price, item_rate, item_reviewnum, item_link, sep="\n", end="\n")
            print("==================================================")
            