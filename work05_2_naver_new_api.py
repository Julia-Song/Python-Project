import os
import sys
import urllib.request
import json
import csv
import html.parser
client_id = "RjvotaEwT3oTy_y8umFg"
client_secret = "54rlJdeY2L"

def get_query(keyword, x):
    encText = urllib.parse.quote(keyword)
    #url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100"  # json 결과
    url = "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=100&start=" + x
    #url = "https://openapi.naver.com/v1/search/news.json?query=" + encText
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

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
    for i in range(1,1000,100):
        #a = get_query(str(i))       #a의 타입은 json
        a=get_query(keyword,str(i))
        b = json.loads(a,encoding="utf-8")  #b의 타입은 딕셔너리. json을 파이썬 딕셔너리로 바꿔줬음
        for x in b["items"]:
            print (x)
            print(x["title"])
            print(x["link"])
            row_for_write = []
            row_for_write.append(x["title"])
            row_for_write.append(x["link"])
            row_for_write.append(x["originallink"])
            row_for_write.append(x["description"])
            row_for_write.append(x["pubDate"])
            csv_writer.writerow(row_for_write)   #문자열이 아니라 리스트를 넣어줘야 한다. 그래야 엑셀이 열별로 들어감


    fout.close()