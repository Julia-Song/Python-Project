#!__*__coding:utf-8__*__
import json
def help_screen():
    print("File : Input File name")
    print("Help : Displays this help screen")
    print("Quit : Exits the program")

def menu():
    return input("==F)ile H)elp Q)uit==")

def csv_file_open():
    filename=input("input csv filename")
    import os
    x=os.path.splitext(filename)
    outputfilename=x[0]+"_out"+x[1]
    f=open(filename,"r")
    f2=open(outputfilename,"w")

    cnt=0
    while True:
        oneline=f.readline()
        if oneline=="":
            break
        cols=oneline.split(",")
        if cols[1].find("롯데리아")>=0:
            f2.write(oneline)
            f2.flush()
    f.close()
    f2.close()

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