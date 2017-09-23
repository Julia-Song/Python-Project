#!__*__coding:utf-8__*__

import folium
my_map = folium.Map(location=[37.5666, 126.97], tiles="Stamen Toner")

x = folium.Marker([37.5666, 126.95000], popup="한글")
x.add_to(my_map)

my_map.save("map_output_01.html")