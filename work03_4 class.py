#!__*__coding:utf-8__*__
"""
def cal_km_per_liter():
    pass

def car_color(color):
    pass

car_a=""
car_b=""

car_a_color = "red"
car_color(car_a_color)
"""
class Car():
    rate=1.0

"""
    def __str__(self):
        i="I am class"+self.color
        return i
"""
    def __init__(self,color):       #생성자 함수 무조건 문법이 __ init__ 이다. 무조건 self라는 파라미터가 하나 붙는다. 그 뒤엔 초기값을 뭘받을지 적는다.
        pass
        self.color = color

    def set_km_per_liter(self, i):
        self.set_km_per_liter=i
        pass

    def get_distance(self,liter):
        return liter*self.set_km_per_liter


a_car=Car("red")
b_car=Car("yellow")
print(a_car.rate)
print(b_car.rate)

Car.i_am_class_method()
print(a_car.rate)
print(b_car.rate)
b_car.color="black"
print(a_car.color)
print(b_car.color)
a_car.set_km_per_liter(20)
a_car.get_distance(50)
b_car.set_km_per_liter(10)
b_car.get_distance(50)

print(str(a_car))   #class의 정보만 string 으로 바꿔서 출력한다.
print(dir(a_car))
print(dir(Car.__class__))