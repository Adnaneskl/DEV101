def menu():
    print("1.Saisir un étudiant.")
    print("2.Saisir plusieurs étudiant.")
    print("3.Afficher la liste des étudiant.")
    print("0.Quitter.")

filieres = ["Dev","Ir","Ge","Cm"]
etudiants=[]

def ajouter_un_stagiaire(numero_stagiaire):
    nom = input("Saisir le nom du stagiaire :\n")
    prenom = input("Saisir le prenom du stagiaire :\n")
    x= -1
    while(x<0):
        print("Choisir la filière :")
        for i in filieres:
            print(filieres.index(i)+1,'.',i, sep="")
        x = input("Choisir la filière : \n")
        if (x.isdigit()):
            x = int(x)
        else :
            x = -1
    match x:
        case 1:
            filiere = "Développement digitale"
        case 2:
            filiere = "Infrastructure réseau"
        case 3:
            filiere = "Gestion entreprise"
        case 4:
            filiere = "Commerce"
        case _:
            while(not x.isdigit or int(x) not in [1,2,3,4]):
                x = input("Choisir la filière : \n")

    etudiant = [numero_stagiaire,nom,prenom,filiere]
    etudiants.append(etudiant)

def select_menu():
    menu()
    x = input("Entrez votre choix")
    while (not x.isdigit() and x<0 and x not in [0,1,2,3,4,5,6,7,8,9]):
        menu()
        x = input("ari nichan ayezan")
    x = int(x)
    return x

        



#Ajouter un ou plusieur stagiaire
x=-1
while(x != 0):
    x = select_menu()
    match x:
        case 1 :
            p = "oui"  
            while(p!="non"):
                ajouter_un_stagiaire(len(etudiants) +1)
                p = input("Voulez vous continuez ? : non pour quitter \n")
                for i in etudiants:
                    print(i)
        case 2:
            print("bofar9och")
        case 3:
            print("thakhnanacht")
        case 4:
            print("tha9louloucht")

