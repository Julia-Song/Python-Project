#!__*__coding:utf-8__*__

import os
import sys
import glob
import csv
import matplotlib.pyplot as plt
import matplotlib as mat
font_location = r"c:\windows\fonts\malgun.ttf"
font_name = mat.font_manager.FontProperties(fname=font_location).get_name()     #이거 안하면 한글이 안나옴.
mat.rc('font',family=font_name)

folder = r"D:\SHN\PythonProject\대구북구인구현황\*.csv"   #r을 쓰면 \를 한번씩만 쓰면된다. \를 \로 읽기때문
files = glob.glob(folder)
#files = glob.glob(folder + r"\*.csv")  #이렇게 쓰거나 윗윗줄처럼 디렉토리에 *.csv를 덧붙이면 된다.

y = []
x_ticks = []
for one_file in files:
    m=one_file[:-6]
    h=m[-4:]
    x_ticks.append(h)
    f = open(one_file,"r", encoding="cp949")
    csv_reader = csv.reader(f)
    x = 0
    for cols in csv_reader:
        print(cols)
        try:
            x = x + int(cols[4])
        except:         #에러가 나면 패스 (에러 날게 맨 윗줄 한글인 인구수(숫자로 변환 불가능) 밖에 없으니까)
            pass
    print(one_file)
    print(x)
    y.append(x)     #빈list 안에 담기

print(y)

x = range(len(y))
print(x)

axes = plt.gca()    #축객체 가져오는거
axes.set_ylim([400000,500000])

plt.plot(x,y,'-bo')
plt.ylabel("인구수")
plt.xlabel("월별")
#plt.xticks([0,1,2], ["3월", "4월", "5월","6월", "7월", "8월","9월", "10월", "11월", "12월"])
plt.xticks(x,x_ticks)
#plt.show()

plt.savefig("daegu_output.png")