# %% user agent 정리
'''
    requests package를 통해 그냥 get함수를 호출하면
    웹페이지에서 기계라 판단 올바르지 않은 정보를 줄 수도 있다.
    
    이 떄 user agent는 HTTP 요청을 보내는 디바이스와 브라우저 등
    사용자 소프트웨어의 식별 정보를 담고 있는 request header의 한 종류.
    임의로 수정될 수 없는 값이고, 보통 HTTP 요청 에러가 발생했을 때
    요청을 보낸 사용자 환경을 알아보기 위해 사용한다.
    
    이 값을 get함수의 header로 전달하면
    웹 페이지는 사람이라 판단하여 올바른 정보를 준다.
'''

# %%
import requests

url = "https://nadocoding.tistory.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
response = requests.get(url, headers=headers)
response.raise_for_status()

with open("nadocoding.html", "w", encoding="utf8") as file_pointer:
    file_pointer.write(response.text)