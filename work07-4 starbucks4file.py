#!__*__coding:utf-8__*__

import pandas as pd

#"""
#for i in range(1,5):
#    filename = r"C:\Users\Administrator\Downloads\상가업소정보\상가업소_201706_%s.csv"
#    filename = filename %str(i).zfill(2)
#    a1 = pd.read_csv(filename, engine="python")
#    a_list.append(a1)
#"""

filename = r"C:\Users\Administrator\Downloads\상가업소정보\상가업소_201706_01.csv"
a1 = pd.read_csv(filename, engine="python")
filename = r"C:\Users\Administrator\Downloads\상가업소정보\상가업소_201706_02.csv"
a2 = pd.read_csv(filename, engine="python")
filename = r"C:\Users\Administrator\Downloads\상가업소정보\상가업소_201706_03.csv"
a3 = pd.read_csv(filename, engine="python")
filename = r"C:\Users\Administrator\Downloads\상가업소정보\상가업소_201706_04.csv"
a4 = pd.read_csv(filename, engine="python")

df=pd.merge([a1, a2, a3, a4])

df_star = pd.read_excel("스타벅스거르기2.xlsx")
df2 = df_star[["상호명", "시도명", "시군구명"]]
gf = df2.groupby(["시도명", "시군구명"]).count()
gf = gf.reset_index()
gf.to_excel("스타벅스_상점갯수.xlsx")

for i in gf.columns:
    print(i)

print(gf.head())

print(gf.info())

kf = pd.read_csv(r"D:\SHN\PythonProject\data_draw_korea.csv", engine="python",encoding="utf-8")
result = pd.merge(gf, kf, left_on=["시도명", "시군구명"], right_on=["광역시도", "행정구역"], how="right")

import korea_showMap
korea_showMap.drawKorea('상호명', result, '광역시도', '행정구역', 'Reds')