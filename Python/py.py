import os

if(os.path.exists("Q.txt")):
    file = open("Q.txt","r")
    lq = file.readlines()
else:
    file = open("Q.txt","w")
    lq=[]
file.close()


def ajout():
    nom = input("Entrez le nom du quartier : ")
    sur = input("Entrez la surface : ")
    while(not sur .isdigit()):
        sur = input("La surface doit être un nombre : ")
    nbh = input("Entrez le nombre des habitants : ")
    while(not nbh.isdigit()):
        nbh = input("Le nombre des habitants doit être un nombre : ")
    lq . append(nom+" " * (25 - len(nom))+" " * (15-len(sur)) + sur + " " * (7-len(nbh)) + nbh + "\n")

def afficher():
    print("Nom"+" " * 22," " * 8+"Surface "," "*9+"Nombre habitants\n",sep="")
    for i in lq:
        print(i[0:40]," "*9,i[40:42]," "*16,i[42:-1],sep="",end="\n")

def supprimer():
    nom = input("Entrez le nom du quartier à supprimer : ")
    for i in range(len(lq)):
        if(nom == str(lq[i][0:24]).strip()):
            del lq[i]
            break
    else:
        print("introuvable")

def chercher():
    pass
def sauver():
    file=open("Q.txt","w")
    file.write("".join(lq))
    file.close()

ajout()
afficher()
sauver()