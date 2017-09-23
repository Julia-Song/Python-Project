#!__*__coding:utf-8__*__

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

a=10
def abc():
    a=20
    print(a)
    pass

a=10
def abc():
    a=20
    print("inside",a)
    pass
abc()
print("outside",a)

print("---")
#바깥걸 불러들이는건 좋은 코딩이 아니다. 함수는 함수안에서 돌아가야하니까 함수안에서 변수지정해라. 바깥꺼 불러 쓸거면 이렇게 쓰기

a=10
def abc(a):
    print("inside",a)
    pass
abc(a)
print("outside",a)

