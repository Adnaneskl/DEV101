def menu():
    choix = -1
    while(choix != 0):
        print("1.Saisir un étudiant.")
        print("2.Saisir plusieurs étudiant.")
        print("3.Afficher la liste des étudiant.")
        print("0.Quitter.")
        choix = int(input("Entrez votre choix :\n"))

filieres = ["Dev","Ir","Ge","Cm"]
etudiants=[]

def ajouter_un_stagiaire(numero_stagiaire):
    nom = input("Saisir le nom du stagiaire :\n")
    prenom = input("Saisir le prenom du stagiaire :\n")
    print("Choisir la filière :")
    for i in filieres:
        print(filieres.index(i)+1,'.',i, sep="")
    x=int(input("Choisir la filière : \n"))
    match x:
        case 1:
            filiere = "Développement digitale"
        case 2:
            filiere = "Infrastructure réseau"
        case 3:
            filiere = "Gestion entreprise"
        case 4:
            filiere = "Commerce"
    etudiant = [numero_stagiaire,nom,prenom,filiere]
    etudiants.append(etudiant)

p = -2
c = 0
while(p!=-1):
     ajouter_un_stagiaire(c)
     p = int(input("Voulez vous continuez ? : -1 pour quitter \n"))
     c += 1
     for i in etudiants:
         print(i)