#!__*__coding:utf-8__*__

import requests

test_url="http://blog.naver.com/hdybaba/221090847685"
response = requests.get(test_url)
response.text

f = open("work04_5.txt","w",encoding="utf-8")
f.write(response.text)
f.close()

test_url2="http://blog.naver.com/PostView.nhn?blogId=hdybaba&logNo=221090847685&redirect=Dlog&widgetTypeCall=true"
response = requests.get(test_url2)
response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text,"html.parser")
result_text=soup.get_text()
t=soup.find(id="postListBody")
result_text=t.get_text()

f = open("work04_5_1.txt","w",encoding="utf-8")
f.write(result_text)
f.close()