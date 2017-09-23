import os
import sys
import urllib.request
import json
import csv
import html.parser
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

client_id = "RjvotaEwT3oTy_y8umFg"
client_secret = "54rlJdeY2L"

def get_query(keyword, x):
    encText = urllib.parse.quote(keyword)
    #url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100"  # json 결과
    url = "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=100&start=" + x


    """
    naver_headers={}
    naver_header["X-Naver-Client-Id"] = CLIENT_ID
    naver_headers["X-Naver-Client-Secret"] = 
    """



    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)

"""get_query("50")

for i in range(10): #[0,1,2,3,4,5,6,7,8,9]
    y=100 + i + 1   #[1,101,201,3,01,401,501,601,701,801,901]
    z=str(y)
    get_query(z)
"""

def run_naver_search_from_news(keyword):
    fout=open("naver_result_%s_news.csv" %keyword,"w",encoding="utf-8",newline="")       #파일을 쓰기모드로 열었다.
    csv_writer=csv.writer(fout)

    #for i in range(1, 1000,100):        #1부터 1000까지 100간격으로
    for i in range(1,500,100):
        #a = get_query(str(i))       #a의 타입은 json
        a = get_query(keyword, str(i))
        b = json.loads(a,encoding="utf-8")  #b의 타입은 딕셔너리. json을 파이썬 딕셔너리로 바꿔줬음

        for x in b["items"]:
            rx= []
            rx.append(x["title"])
            rx.append(x["link"])
            rx.append(x["originallink"])
            rx.append(x["description"])
            rx.append(x["pubDate"])
            #csv_writer.writerow(rx)   #문자열이 아니라 리스트를 넣어줘야 한다. 그래야 엑셀이 열별로 들어감

            if x["link"].find("news.naver.com") >=0:        #0번째가 1이니까 있다는 뜻이다.
                content = get_naver_news_crawling(x["link"])
                comment = ""
            else:
                content = ""
                comment = ""

    fout.close()

def get_naver_news_crawling(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')
    rs = bs.find(id = "articleBodyContents")

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
    return result

driver = None

def get_naver_news_crawling(url):
    global driver
    if driver ==None:
        browser = "D:\\chromedriver_win32\\chromedriver.exe"
        driver = webdriver.Chrome(browser)
    driver.get(url)
    time.sleep(2)

    html = driver.page_source
    bs=BeautifulSoup(html,"html.parser")
    contents=bs.find_all("span",{"class":"u_cbox_contents"})
    result=[]

    for i in contents:
        print(str(i))
        result.append(str(i.get_text()))

        return "@@@".join(result)
        pass
