#!_*_coding:utf-8_*_
my_name=input("please in put your name:")
people=["andrew","thomas","sera","anna"]

my_name_lower=my_name.lower()
if my_name_lower in people:
    print("you are employee")
else:
    print("you are costomer")