import os

if(os.path.exists("students_list.txt")):
        with open("students_list.txt","r") as file:
            stdts_lst = [["".join(item) + ';' if i < len(line.split(";")) -1 else "".join(item) for i,item in enumerate(line.split(";"))] for line in file.readlines()]

        file.close()
else:
    stdts_lst= []

def add_stdt(stdts_lst :list[str]):
    
    name = input(f"Enter the Name for student {len(stdts_lst)+1} : ")+";"
    branch = input(f"Enter the Branch for student {len(stdts_lst)+1} : ")+";"
    mark = input(f"Enter the Mark for student {len(stdts_lst)+1} : ")

    return [str(len(stdts_lst)+1)+";",name,branch,mark]


def add_stdts():
    while(True):
        stdts_lst.append(add_stdt(stdts_lst=stdts_lst))
        if(input("Press enter to continue insersion or type no to exit.\n")=="no"):
            if(os.name=="nt"):
                os.system("cls")
            else:
                os.system("clear")
            break


def sort_by_branch():
    for _ in stdts_lst:
        stdts_lst.sort(key=lambda row: row[2])

def savetoFile():
    file = open("students_list.txt","w")
    for i in range(len(stdts_lst)):
        if(not str(stdts_lst[i][-1]).__contains__("\n")):
            stdts_lst[i][-1]= str(stdts_lst[i][-1])+"\n"
    
    file.write("".join( "".join(i) for i in stdts_lst))
    file.close()
        

add_stdts()
sort_by_branch()
savetoFile()

