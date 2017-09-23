#!__*__coding:utf-8__*__

import folium
import csv

my_map = folium.Map(location=[37.56667, 126.97806])

file = open("C:\\Users\\Administrator\\Downloads\\상가업소정보\\상가업소_201706_01.csv","r")
csv_reader = csv.reader(file)

for i in csv_reader:
    longitude = i[-2]
    latitude = i[-1]
    print(longitude)
    print(latitude )
    name = i[1]
    if name.find("버거킹") >=0:
        x = folium.Marker([float(latitude), float(longitude)], popup=name)
        x.add_to(my_map)

my_map.save("map_output_버거킹.html")