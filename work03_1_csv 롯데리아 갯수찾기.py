#!__*__coding:utf-8__*__
#import json
def help_screen():
    print("File : Input File name")
    print("Help : Displays this help screen")
    print("Quit : Exits the program")

def menu():
    return input("==F)ile H)elp Q)uit==")

def draw_pytagcloud(data_array):
    #data_array=["롯데리아","롯데리아","롯데리아","롯데리아","롯데리아","CU"]
    from pytagcloud import create_tag_image, make_tags
    from collections import Counter
    words_count=Counter(data_array)
    counts=words_count.most_common(100)
    tags=make_tags(counts,maxsize=120)
    create_tag_image(tags,"cloud_large.png",size=(900,600),fontname='Malgun')


def csv_file_open():
    filename=input("input csv filename")
    import os
    x=os.path.splitext(filename)
    outputfilename=x[0]+"_out"+x[1]
    f=open(filename,"r")
    f2=open(outputfilename,"w")

    cnt=0
    lotte_cnt=0
    titles_dic={}   # 아무값없는 딕션어리
    titles_array=[]
    while True:
        oneline=f.readline()
        if oneline=="":
            break
        cols=oneline.split(",")
        title_key=cols[1]
        titles_array.append(title_key)
        if title_key not in titles_dic:
            titles_dic[title_key]=1
        else:
            titles_dic[title_key] = titles_dic[title_key] + 1
            #titles_dic[title_key]+=1
        if cols[1].find(" 롯데리아")>=0:
            if cols[1].find("롯데리아")>=0:
                f2.write(oneline)
                f2.flush()
                #print(oneline)
    f.close()
    f2.close()

    report=open("result.txt","w")
    for title in titles_dic:
        report.write(title+":")
        report.write(str(titles_dic[title]))
        report.write("\n")
    report.close()

    draw_pytagcloud(titles_array)

help_screen()
while True:
    val=menu().upper()
    if val not in ["F","H","Q"]:
        print("wrong input")
        continue
    if val=="H":
        help_screen()
    elif val=="Q":
        break
    else:
        csv_file_open()
        pass

# 파일 이름칠때 C:\Users\Administrator\Downloads\상가업소정보\상가업소_201706_04.csv 라고 친다.
# pip install -U pytagcloud
# pip install -U pygame
# pip install -U simplejson