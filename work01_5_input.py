#!_*_coding:utf-8_*_
input_value=input("input_value:")

if input_value.isdigit():   #if not으로 한다면 ~가 아니면이 된다.
    input_value2=int(input_value)
    if input_value2>0 and input_value2 <10:
        result=input_value
        print("입력해주신 값은" + input_value + "이고, 결과값은" + str(result) + "입니다")
    else:
        pass
else:
    print("문자열입니다. 다시 입력해 주세요")

a=3
if not (input_value.isdigit() and a==3):    #a가 숫자형이고 3인게 아니면 = 숫자형이 안거나 3이 아니면
    pass

if a!=3:     #3이 아니면