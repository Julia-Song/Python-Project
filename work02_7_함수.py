customers=["andrew","thomas","sera","lara","allen","edward"]

print("dear "+customers[0])
print("dear "+customers[1])
print("dear "+customers[2])
print("dear "+customers[3])
print("dear "+customers[4])

def ax(i):
    return "my dear "+i
print(ax(customers[0]))


print("---함수쓰면 좋은점---")
print(10+5)
print(20+5)
print(30+5)

def calculate(a,b):
    return a-b
print(calculate(10,5))
print(calculate(20,5))
print(calculate(30,5))

print("---함수2---")

def show_main():
    return"""
    this program is..
    asd
    asd1
    asd2
    """


def show_main2():
    print("""
    hahaha
    """)

a=show_main()   #return뒤에 있는 값이 a로 들어온다. 프린트가 없어서 출력되진 않는다.
b=show_main2()  #끝나고 b는 null(아무것도 없다)
print(show_main())

print("---함수 심화---")    # *한개 하면 인자수 모를때 다 받을때 쓴다. *두개는 딕션어리 형태로 받는다는 뜻
