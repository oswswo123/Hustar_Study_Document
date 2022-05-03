#%% 연도별 영화 순위
import requests
from bs4 import BeautifulSoup

for year in range(2015, 2022):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "lxml")
    
    movie_images = soup.find_all("img", attrs={"class":"thumb_img"})
    
    for index, movie_image in enumerate(movie_images):
        # // 링크 https:// 붙여주기
        image_url = movie_image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
            
        #print(image_url)
        image_resource = requests.get(image_url)
        image_resource.raise_for_status()
        
        with open("movie_{}_{}.jpg".format(year, index+1), "wb") as file_pointer:
            file_pointer.write(image_resource.content)
        
        if(index == 4):
            break
