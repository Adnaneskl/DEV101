import os

decisions = ["admis","refusé","ajourné"]

def saisir(decision):
    concour = []
    if(os.path.exists("concour.txt")):
        file = open("concour.txt","r")
        concour = file.readlines()
        file.close()

    ncin=input("Entrez le numero de la CIN")
    nom =input("Entrez votre nom")
    prenom=input("Entrez votre prenom")
    age=input("Entrez votre age")
    
    while(len(ncin) > 10):
        ncin=input("Merci de saisir un numéro de CIN valide :")
    while(len(nom)>12):
        nom = input("Merci de saisir un nom valide : ")
    while(len(prenom)>12):
        prenom = input("Merci de saisir un nom valide : ")
    while(not age.isdigit()):
        age =  input("Merci d'entrer un age valide : ")
    else:
        age = int(age)
        while(age < 18 or age > 30):
            if(age > 30):
                print("Vous serez mis à la liste d'attente.")
            elif(age < 18):
                print("Vous n'avez pas l'age minimum")
                quit
    while(decision not in decisions):
        decision = input("Merci d'entrer une décision valide : ")
    
    if("".isal)
    if(not os.path.exists("concour.txt")):
        file = open("concour.txt","w")
        file.write("".join(concour+"\n"))
        file.close()
    else:
        concour.append(ncin,nom,prenom,age,decision)




def admis():
    if(os.path.exists("admis.txt")):
        file = open("admis.txt","r")
        _=file.readlines()
        return _
    else:
        file = open("admis.txt","w")
        return []

saisir(decisions[1])
