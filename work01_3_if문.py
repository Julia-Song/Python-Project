#!_*_coding:utf-8_*_
money=input("please input your current money:")
money=int(money)
if money>1000 and money<2000:
    print("bus")
elif money>=2000:
    print("taxi")
else:
    print("walk")