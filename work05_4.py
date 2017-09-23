#!__*__coding:utf-8__*__

import time
from selenium import webdriver
from bs4 import BeautifulSoup

browser = 'D:\\Chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(browser)
driver.get("http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=005&aid=0001027677")
time.sleep(3)   #3초 기다려(파이썬은 초단위. 나머진 ms로 1000분의 1단위). 이미지나  로딩되는데 시간 걸리니까 3초 후에 다음 코딩 실행.
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
"""

for i in range(0,10):
    driver.find_element_by_css_selector(".u_cbox_btn_more").click()
    time.sleep(3)
    i+=1


html = driver.page_source
bs = BeautifulSoup(html,'html.parser')
contents = bs.find_all("span",{"class":"u_cbox_contents"})  #파이썬 클래스말고 html 클래스
for i in contents:
    print(str(i.get_text()))