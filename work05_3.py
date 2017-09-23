#!__*__coding:utf-8__*__

import os
import requests
from bs4 import BeautifulSoup

url = "http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=005&aid=0001027677"
response=requests.get(url)
bs=BeautifulSoup(response.text,'html.parser')
#print(bs.get_text())    #html 날리고 text만 남기게 해주는게 get_text

rs=bs.find(id="main_content")        #find는 제일 먼저 찾은거 하나만 찾는다. findall은 다 찾아준다. 보통 list로 해서 for문으로 돌린다.

"""
클래스로 하고싶으면 이렇게 하면 된다.
rs=bs.find_all("a",class":r.compile("nclic")})
rs=bs.find_all("a",class":"nclic"})
"""


if rs == None:
    print("empty main_content")
for i in rs(["script","style"]):
    i.decompose()       #스크립트 객체랑 스타일 객체를 날려버려라
#print(rs.get_text())

content = rs.get_text()
result = ""
for i in content.splitlines():
    if i.strip() == "":
        pass
    else:
        result +=i
        result += "\n"
print(result)

#print(response.text)