#!__*__coding:utf-8__*__

from konlpy.tag import Hannanum, Kkma, Twitter, Komoran
from collections import Counter
result = "오늘은 참 좋은 날씨입니다. 어제도 삼겹살을 먹었지만, 저녁에 식당에 가서 삼겹살을 먹어야겠습니다. ㅋㅋㅋ ㅠㅠ"

k = Twitter()
print(dir(k))
print(k.pos(result))
r = k.nouns(result)
x = Counter(r)
print(x)
r.sort()
print(r)

"""

k = Kkma()
r = k.nouns(result)


"""

