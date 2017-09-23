#!_*_coding:utf-8_*_
input_value=input("input value1:")
c=int(input_value)*30
c1="입력해 주신 값1은 :"+input_value+"결과값은"+str(c)

print(c1)

input_value=input("input value2:")
c=int(input_value)*30

input_value2=int(input_value)
if input_value2 >0 and input_value2 <30:
    c=int(input_value)*50

c2="입력해 주신 값2은 :"+input_value+"결과값은"+str(c)

print(c2)

import sys
sys.exit()