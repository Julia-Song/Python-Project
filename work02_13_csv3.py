#!__*__coding:utf-8__*__

f=open("C:\\Users\\Administrator\\Downloads\\상가업소정보\\상가업소_201706_01.csv","r")
f2=open("C:\\Users\\Administrator\\Downloads\\상가업소정보\\상가업소_201706_01_out.csv","w")

cnt=0
while True:
    #cnt=cnt+1
    #if cnt>100:
    #break
    oneline=f.readline()
    if oneline=="": #None type
        break
    if oneline.find("롯데리아")>=0:     #롯데리아가 있으면 위치가 찍히니까 0이상이다. 음수 나오면 없다는뜻
        f2.write(oneline)
    #print(oneline)

f.close()
f2.close()      #파일열면 반드시 닫아야한다.

#startswith()    #그걸로 시작하니?
#endswith()      # 그걸로 끝나니?
#find()          #문자가 가장 먼저 나오는 위치를 숫자로 알려준다. 자리는 0부터


