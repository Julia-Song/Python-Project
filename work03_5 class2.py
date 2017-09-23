#!__*__coding:utf-8__*__

import os
import sys

class Car(object):
    num_of_wheels = 4

    def __init__(self,car_name):
        self.car_name=car_name  #self.car name 이랑 그냥 car name 이랑 다르다.
        self.km=None
        self.color=None
        pass

    @classmethod
    def change_num_of_wheels(cls,num):
        cls.num_of_wheels = 3

    def set_km_per_liter(self,km):
        self.km=km

    def get_expected_km(self,liter):
        return self.km*liter

    def set_color(self,color):
        self.color=color

    def get_color(self):
        return self.color

my_car=Car("honda")
my_car.set_color("red")
my_car.set_km_per_liter(8)

print(my_car.color)

mom_car=Car("kia")
mom_car.set_color("white")
mom_car.set_km_per_liter(10)

print(my_car.get_color())
print(my_car.get_expected_km(10))