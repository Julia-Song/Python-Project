#!__*__coding:utf-8__*__
import os
import sys


class Car(object):
    def __init__(self, car_name):
        self.car_name = car_name
        self.km = None
        self.__color = None
        pass

    def set_km_per_liter(self, km):
        self.km = km

    def get_expected_km(self, liter):
        return self.km * liter

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


my_car = Car("honda")
my_car.set_color("red")
my_car.set_km_per_liter(8)

mom_car = Car("kia")
mom_car.set_color("white")
mom_car.set_km_per_liter(10)

print(my_car.get_color())
print(my_car.get_expected_km(10))

Car.set_color(None, "red")
