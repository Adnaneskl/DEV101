import os

def saisir():
    if(os.path.exists("concours1.txt")):
        file = open("concours1.txt","r")
        data_concours = file.readlines()
        file.close()
    else:
        data_concours = []

    ncin = input("Entrez la cin : ")    
    nom = input("Nom : ")
    prenom = input("Prenom : ")
    age = input("Age : ")

    decisions = ["admis","refuse","ajourne"]
    print("Entrer la decision:\n1.Admis\n2.Refuse\n3.Ajourne")
    dec = input("Decision : ")
    match dec:
            case "1":
                dec = decisions[0]
            case "2":
                dec = decisions[1]
            case "3":
                dec = decisions[2]
            case _:
                dec=""
    while(dec not in decisions):
        dec = input("veuillez choisir un choix valide : ")

    data_concours.append(ncin+";"+nom+";"+prenom+";"+age+";"+dec+"\n")
    file = open("concours1.txt","w")
    file.write("".join(data_concours))
    file.close()

def admis():
    if(os.path.exists("concours1.txt")):
        file = open("concours1.txt","r")
        data_concours = file.readlines()
        file.close()
    else:
        quit

    if(os.path.exists("admis1.txt")):
        file = open("admis1.txt","r")
        data_admis = file.readlines()
        file.close()
    else:
        data_admis = []

    for i in range(len(data_concours)):
        c = data_concours[i].split(";")
        if(c[4] == "admis\n"):
            data_admis.append("".join(data_concours[i]))
    
    file = open("admis1.txt","w")
    file.write("".join(data_admis))
    file.close()

def attente():
    if(os.path.exists("admis1.txt")):
        file = open("admis1.txt","r")
        data_admis = file.readlines()
        file.close()
    else:
        quit

    if(os.path.exists("attente1.txt")):
        file = open("attente1.txt","r")
        data_attente = file.readlines()
        file.close()
    else:
        data_attente = []
    
    for i in range(len(data_admis)):
        c = data_admis[i].split(";")
        if(int(c[3]) > 30):
            d = data_admis[i]
            d[4]="ajourne"
            data_attente.append("".join(data_admis[i]))
    
    file = open("attente1.txt","w")
    file.write("".join(data_attente))
    file.close()

saisir()
admis()
attente()

    
    
    