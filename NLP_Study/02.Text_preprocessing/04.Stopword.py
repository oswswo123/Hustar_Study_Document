# %% 불용어(Stopword)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt

stop_words_list = stopwords.words("english")
print("불용어 개수 : ", len(stop_words_list))
print("불용어 10개 출력 : ", stop_words_list[:10])

# %% NLTK로 불용어 제거하기

example = "Family is not an important thing. It's everything."
stop_words = set(stopwords.words("english"))

word_tokens = word_tokenize(example)

result = list()
for word in word_tokens:
    if word not in stop_words:
        result.append(word)

print("불용어 제거 전 : ", word_tokens)
print("불용어 제거 후 : ", result)

# %% 한국어 불용어 제거

okt = Okt()

example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
stop_words = "를 아무렇게나 구 우려 고 안 돼 같은 게 구울 때 는"

stop_words = set(stop_words.split(" "))
word_tokens = okt.morphs(example)

result = [word for word in word_tokens if word not in stop_words]

print("불용어 제거 전 : ", word_tokens)
print("불용어 제거 후 : ", result)