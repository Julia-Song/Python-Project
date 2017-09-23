#!__*__coding:utf-8__*__

f=open("C:\\Users\\Administrator\\Downloads\\상가업소정보\\상가업소_201706_01.csv","r")
a=f.readlines()    #readline은 한줄만 읽어
print(len(a))

cnt=0
for oneline in a:
    print(oneline)
    cnt=cnt+1
    if cnt>100:
        break


print("--")

#!__*__coding:utf-8__*__

f=open("C:\\Users\\Administrator\\Downloads\\상가업소정보\\상가업소_201706_01.csv","r")
while True:
    oneline=f.readline()
    if oneline=="":
        break
    print(oneline)

f.close()
