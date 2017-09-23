#!__*__coding:utf-8__*__

import folium

my_map = folium.Map(location=[37.56667, 126.97806])
print(dir(my_map))

x=folium.Marker([37.56667, 126.97806], popup = "한글")
x.add_to(my_map)

my_map.save("map_output.html")