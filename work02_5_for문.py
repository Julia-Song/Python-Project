customers=["andrew","thomas","sera","lara""allen","edward"]
customers=("andrew","thomas","sera","lara""allen","edward")
for one_customer in customers:
    print(one_customer, end="")
    print(one_customer, end=",")

#D:\SHN\PythonProject\work02_5_for문.py>D:\SHN\PythonProject\test.csv 하면 디렉토리 변경 및 파일형태 변경 저장되는데 잘 모르겠음.

sum=0
for i in range(10):
    print(i)
    sum+=i
print("%d"%sum)

for i in range(5,10,3):
    print(i)
    sum+=i
print("다음 꺼 %d"%sum)