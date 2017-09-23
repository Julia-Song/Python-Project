#!__*__coding:utf-8__*__

import os
import sys
import glob
import csv
import matplotlib.pyplot as plt
import matplotlib as mat

from konlpy.tag import Hannanum, Kkma, Twitter, Komoran
from collections import Counter

font_location = r"c:\windows\fonts\malgun.ttf"
font_name = mat.font_manager.FontProperties(fname=font_location).get_name()     #이거 안하면 한글이 안나옴.
mat.rc('font',family=font_name)

f = open("뉴스1.txt", "r", encoding="utf-8")
content = f.read()
t = Twitter()
result = t.nouns(content)
print(result)
result2 = Counter(result)
x = result2.most_common(10) #명사 많은 상위 10개 뽑아냄

headers =[]
values = []
for i in x:
    headers.append(i[0])
    values.append(i[1])

x = range(len(values))  #길이만큼 불러냄
print(headers)
print(values)
print(result2)


#plt.plot(x,values,'-bo')
plt.bar(x, values, width=0.3)
plt.ylabel("갯수")
plt.xlabel("단어")
plt.xticks(x, headers)
#plt.show()

plt.savefig("news_text.png")