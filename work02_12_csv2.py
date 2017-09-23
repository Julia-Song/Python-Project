#!__*__coding:utf-8__*__

f=open("C:\\Users\\Administrator\\Downloads\\상가업소정보\\상가업소_201706_01.csv","r")
f2=open("C:\\Users\\Administrator\\Downloads\\상가업소정보\\상가업소_201706_01_out.csv","w")

cnt=0
while True:
    cnt=cnt+1
    if cnt>100:
        break
    oneline=f.readline()
    if oneline=="":
        break
    f2.write(oneline)
    print(oneline)

f.close()
f2.close()      #파일열면 반드시 닫아야한다.