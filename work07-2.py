#!__*__coding:utf-8__*__

import pandas as pd

filename = r"C:\Users\Administrator\Downloads\상가업소정보\상가업소_201706_03.csv"
df = pd.read_csv(filename, engine="python")
df_star = df[df.상호명 =="스타벅스"]
df_star.to_excel("스타벅스거르기.xlsx")

df[["상호명", "위도", "경도"]]
df_star.to_excel("스벅위도경도.xlsx")




