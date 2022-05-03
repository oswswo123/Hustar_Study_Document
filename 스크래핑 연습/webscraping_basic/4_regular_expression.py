# %% 요약
'''
    1. pattern = re.compile("원하는 정규식 형태")
    
    2. match_value = pattern.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
    3. match_value = pattern.search("비교할 문자열") : 주어진 문자열 내에 일치하는게 있는지 확인
    4. match_list = pattern.findall("비교할 문자열") : 일치하는 모든 것을 list로 return
    
    원하는 형태 : 정규식
    . : 하나의 문자를 의미  ex) ca.e : care, cafe, case ... (매칭o) | caffe (매칭x)
    ^ : 문자열의 시작을 의미  ex) ^de : desk, destination ... (매칭o) | fade (매칭x)
    $ : 문자열의 끝을 의미  ex) se$ : case, base ... (매칭o) | face (매칭x)
'''

# %% match(regular expression)

import re

# ca?e....? caae, cabe, cace, cade ... 너무 많다
# ca?e를 정규식으로 작성

# . : 하나의 문자를 의미  ex) ca.e : care, cafe, case ... (매칭o) | caffe (매칭x)
# ^ : 문자열의 시작을 의미  ex) ^de : desk, destination ... (매칭o) | fade (매칭x)
# $ : 문자열의 끝을 의미  ex) se$ : case, base ... (매칭o) | face (매칭x)
pattern = re.compile("ca.e")

# 문자열의 매칭을 return
#match_value = pattern.match("case")
match_value = pattern.match("caseless")  # 얘도 매치 됨.(주어진 문자열의 처음부터 일치하는지 확인함)

# group() : 매칭된 문자열들 return
# print(match_value.group())

# match_value = pattern.match("base")
# print(match_value.group())  # 매치되지 않으면 에러 발생(NoneType을 가지게 됨)

if match_value:
    # 문자열이 매칭 된 경우
    print(match_value.group())
else:
    # 문자열이 매칭 되지 않은 경우
    print("매칭되지 않음")

# %% search(regular expression)

# search는 match와 다르게 작동
# match : 주어진 문자열의 처음부터 일치하는지 확인
# search : 주어진 문자열 중에 일치하는게 있는지 확인
import re

pattern = re.compile("ca.e")
match_value = pattern.search("good care")
# match_value = pattern.search("careless")

if match_value:
    print(match_value.group())  # 일치하는 문자열 return
    print(match_value.string)   # 입력받은 문자열 return
    print(match_value.start())  # 일치하는 문자열 시작 index return
    print(match_value.end())    # 일치하는 문자열 끝 index return
    print(match_value.span())   # 일치하는 문자열의 시작/끝 index return
else:
    print("매칭되지 않음")

# %% findall(regular expression)

# findall : 일치하는 모든 것을 list 형태로 return
import re

pattern = re.compile("ca.e")

match_list = pattern.findall("good care cafe")
print(match_list)