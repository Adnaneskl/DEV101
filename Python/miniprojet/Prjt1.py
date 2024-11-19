import os
from pathlib import Path

from miniprojet.cmd import cmd
def saisir():
    while(True):    
        ncin=input('Entrez le numero ncin: ')
        while (not ncin.isalnum() or (len(ncin)>7) or (len(ncin)<6) or not ncin[0].isalpha()):
            ncin=input('Veuillez entrer un numero ncin valide (ex:AB12345) : ')

        nom=input('Entrez le nom du candidat: ')
        prenom=input('Entrez le prénom: ')
        age=input("Entrez l'age du candidat: ")

        while(not age.isdigit()):
            age=input('entrer un age valide: ')
        else: 
            age=int(age)
            while (age<18 or age>100):
                age=input('entrer un age valide(min:18,max:99): ')

        decision=['admis','refuse','ajourne']
        print('Choisir la decision: \n1.admis\n2.refuse\n3.ajourne')
        _=input('Entrez la decision: ')

        while (decision[int(_)-1] not in decision):
            _=input('Veuillez entrer une decision valide: ')
        match _:
            case '1': 
                decision=decision[0]
            case '2':
                decision=decision[1]
            case '3':
                decision=decision[2]
        condidat=[ncin,nom,prenom,str(age),decision]
        
        #séparation des données par un point virgule
        for i in range(len(condidat)):
            condidat[i]+=";"
            if(i == len(condidat)-1):
                condidat[i]+="\n"

        if(os.path.exists("concours.txt")):
            file = open("concours.txt","r")
            data = file.readlines()
            data.append("".join(condidat))
            file.close()
            file = open("concours.txt","w")
            file.write("".join(data))
            file.close()
        else:
            file = open("concours.txt","w")
            file.write("".join(data))
            file.close()
        _=input("continuer ?")
        if(len(_)>0):
            break
123

#saisir()


def admis():
    if(os.path.exists("concours.txt")):
        file = open("concours.txt")
        data = file.read()
        file.close()
    else:
        print("Aucune liste de candidats !")
        quit
    

   # for i in range(0,len(data),4):


#saisir()
print(Path.cwd(e))
if(Path.exists(cmd)):
    print('exist')
else:
    print("doesnt exist")

#os.chdir("C:\\")

