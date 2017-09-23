def help_screen():
    print("File : Input File name")
    print("Help : Displays this help screen")
    print("Quit : Exits the program")

#menu
#Display a menu
#Accepts no parameters
#Returns the string entered by the user

def menu():
    #Display a menu
    return input("==F)ile H)elp Q)uit==")

def csv_file_open():
    print("input csv filename")
    pass
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

#Global variables used by several functions
result=0.0
arg1=0.0
arg2=0.0