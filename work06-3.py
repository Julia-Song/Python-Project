#!__*__coding:utf-8__*__

import folium
import pandas as pd

state_geo = r'seoul_municipalities_geo_simple.json'
state_unemployment = r'US_Unemployment_Oct2012.csv'

state_data = pd.read_csv(state_unemployment)

#Let Folium determine the scale
map = folium.Map(location=[48, -102], zoom_start=3)
map.choropleth(geo_data=state_geo, data=state_data,
             columns=['State', 'Unemployment'],
             key_on='feature.properties.SIG_CD',
             fill_color='PuBu', fill_opacity=0.7, line_opacity=0.2,
             legend_name='Unemployment Rage (%)')
#fill_color 'YlGn' 등으로 하면됨
map.save("map_output_03_kor.html")