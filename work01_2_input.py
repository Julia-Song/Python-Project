#!_*_coding:utf-8_*_
input_value=input("input value3:")
c=int(input_value)*30

input_value2=int(input_value)
if input_value2 >0 or input_value2 <30:
    c=int(input_value)*50
else:
    c=int(input_value2)*50
c3="입력해 주신 값은 :"+input_value+"결과값은"+str(c)

print(c3)