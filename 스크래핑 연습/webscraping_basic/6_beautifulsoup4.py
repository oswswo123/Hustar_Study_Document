# %% beautifulsoup & lxml

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
response = requests.get(url)
response.raise_for_status()

# lxml : parser
soup = BeautifulSoup(response.text, "lxml")

# requests를 통해 네이버 웹툰 페이지의 html 문서를 가져옴
# 가져온 html 문서를 lxml parser를 이용해 BeautifulSoup 객체로 만듦

print(soup.title, end="\n\n")
print(soup.title.get_text(), end="\n\n")    # title tag의 element를 text만 return
print(soup.a, end="\n\n")
print(soup.a.attrs, end="\n\n") # a tag의 element중 attribute들을 return
print(soup.a["href"], end="\n\n")   # a tag의 element의 attribute중 href를 return

# find() : parameter로 준 정보에 일치하는 가장 처음 element를 return
# a tag의 element중 class의 attribute가 Nbtn_upload인 것만 return
print(soup.find("a", attrs={"class":"Nbtn_upload"}), end="\n\n")

print(soup.find("li", attrs={"class":"rank01"}), end="\n\n")

rank01 = soup.find("li", attrs={"class":"rank01"})
print(rank01.a, end="\n\n")

# next_sibling : 다음 tag의 정보를 return (형제 관계에서만 가능)
# previous_sibling : 이전 tag의 정보를 return (형제 관계에서만 가능)
# 가끔 tag 사이에 개행정보(ex. 줄바꿈)가 있어서 next_sibling 한번으로 안 될 때가 있음
# 여러번 하면 됨
print(rank01.next_sibling.next_sibling, end="\n\n")
rank03 = rank01.next_sibling.next_sibling.next_sibling.next_sibling
print(rank03, end="\n\n")

# parent : 부모 tag의 정보를 return
print(rank01.parent.get_text(), end="\n\n")

# find_next_sibling() : 다음 tag중 조건에 해당하는 tag를 return
# find_previous_sibling : 이전 tag중 조건에 해당하는 tag를 return
rank02 = rank01.find_next_sibling("li")
print(rank02, end="\n\n")

# find_next_siblings() : 다음 tag중 조건에 해당하는 tag를 모두 return
ranks = rank01.find_next_siblings("li")
print(ranks)

webtoon = soup.find("a", text="퀘스트지상주의-25화 비키니 사야겠네")
print(webtoon)