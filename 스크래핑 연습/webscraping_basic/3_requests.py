import requests

#response = requests.get("http://nadocoding.tistory.com")
#print("응답코드 :", response.status_code)

response = requests.get("http://google.com")
print("응답코드 :", response.status_code) # 정상 : 200

'''
if response.status_code == requests.codes.ok:   # requests.codes.ok : 200
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드 ", response.status_code, "]")
'''

# raise_for_status() : 문제가 생겼을 경우 오류를 출력하고 프로그램을 종료함
response.raise_for_status()
print("웹 스크래핑을 진행합니다.")

print(len(response.text))

with open("mygoogle.html", "w", encoding="utf8") as file_pointer:
    file_pointer.write(response.text)