# %% 네이버 금융 시가총액

import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액 1~200.csv"
filepointer = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(filepointer)

# header 출력
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for page in range(1, 5):
    resource = requests.get(url + str(page))
    resource.raise_for_status()
    
    soup = BeautifulSoup(resource.text, "lxml")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        
        # 의미없는 데이터 skip
        if len(columns) <= 1:
            continue
        
        # strip() : 공백제거
        data = [column.get_text().strip() for column in columns]
        #print(data)
        writer.writerow(data)
    
filepointer.close()