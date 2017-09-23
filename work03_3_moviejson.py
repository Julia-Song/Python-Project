#!__*__coding:utf-8__*__
import os
import sys
import requests
import json


mykey = "a96f195ffdea76a4fde7c6bf2b07ca20"
URL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
key = "?key=" + mykey + "&targetDt=20170901"

# import types
def get_month(i):
    global URL, mykey
    #if type(i) ==types.Int:찾아보신다함
    i=str(i)
    if len(i) ==1:
        i = "0"+i
    key =  URL + "?key=" + mykey + "&targetDt=2016" + i + "01"
    return key


def x():
    f = open("movie_result.csv","w")

    for j in range(1,13):
        URL_1 = get_month(j)
        response=requests.get(URL_1)
        result=response.text
        result2 = json.loads(result,encoding="utf-8")   #한달치라서 딕셔너리를 바꿨다.
        x = result2["boxOfficeResult"]["dailyBoxOfficeList"]
        for i in x:                     #그달의 10개 영화를 for로 돌린다.
            print(i["movieNm"])
            f.write(i["movieNm"])
            f.write(",")
        f.write("\r\n")
        print(result)

    f.close()
"""
import sys      #프로그램 여기서 끝낸다는 함수
sys.exit()

URL = URL + key
response = requests.get(URL)
result = response.text      #쿠키 등등 다있는데 그 중에 텍스트만 보고싶어 라는 뜻
print(result)

import json
result=json.loads(result,encoding="utf-8")
x=result["boxOfficeResult"]["dailyBoxOfficeList"]
#result["boxOfficeResult"]["dailyBoxOfficeList"][0]["movieNm"]

f=open("movie_result.csv","w")
for i in x:
    print(i["movieNm"])
    f.write(i["movieNm"])
    f.write(",")
f.close()
"""