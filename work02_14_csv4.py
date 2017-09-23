#!__*__coding:utf-8__*__

f=open("C:\\Users\\Administrator\\Downloads\\상가업소정보\\상가업소_201706_01.csv","r")
f2=open("C:\\Users\\Administrator\\Downloads\\상가업소정보\\상가업소_201706_01_out.csv","w")

cnt=0
while True:
    oneline=f.readline()
    if oneline=="": #None type
        break
    cols=oneline.split(",")
    if cols[1].find("롯데리아")>=0:
        f2.write(oneline)
        f2.flush()  #파일을 실시간으로 바로바로 디스크에 기록한다.
f.close()
f2.close()
