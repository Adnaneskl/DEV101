import os

def forecolor(color):
    match color:
        case "RESET" :
            return "\033[0m"
        case "RED" :
            return "\033[91m"
        case "GREEN" :
            return "\033[92m"
        case "YELLOW" :
            return "\033[93m"
        case "BLUE":    
            return "\033[94m"
        case "MAGENTA":
            return "\033[95m"
        case "CYAN":
            return "\033[96m"
        case "WHITE":
            return "\033[97m"

def menu():
   # print(len(stagiaires))
    print(f"{forecolor("GREEN")}1.{forecolor("WHITE")}Saisir un étudiant ou plusieurs étudiants.")
    print(f"{forecolor("GREEN")}2.{forecolor("WHITE")}Afficher la liste des étudiants")
    print(f"{forecolor("GREEN")}3.{forecolor("WHITE")}Recherche un étudiant par numéro")
    print(f"{forecolor("GREEN")}4.{forecolor("WHITE")}Recherche un étudiant par nom")
    print(f"{forecolor("GREEN")}5.{forecolor("WHITE")}Recherche un étudiant par prénom")
    print(f"{forecolor("GREEN")}6.{forecolor("WHITE")}Afficher la liste des admis")
    print(f"{forecolor("GREEN")}7.{forecolor("WHITE")}Afficher la liste par filière")
    print(f"{forecolor("GREEN")}8.{forecolor("WHITE")}Modifier un étudiant")
    print(f"{forecolor("RED")}0.Quitter.")
    print(f"{forecolor("RESET")}")
stagiaires = [""]
filiaires = ["DEV","IR","CM","GE"]

def terminal_width():
    return os.get_terminal_size().columns
def title(title,symbol : str):
    title_len = len(title)
    stars = int((terminal_width()/2)-(title_len/2))
    print(f"{forecolor("CYAN")}","*"*stars,title,"*"*stars,f"{forecolor("RESET")}",sep="")

def ajouter_stagiaire():
    title("Ajout d'un stagiaire :","*")

    continuer = "oui"
    while(continuer != "non"):
        print(f"{forecolor("YELLOW")}")
        nom = input("\tEntrez le nom du stagiaire : ")
        print(f"{forecolor("RESET")}")
        while(nom.__len__() <1):
            print(f"{forecolor("RED")}")
            nom = input("\tMerci d'entrez un nom du stagiaire valide : ")
            print(f"{forecolor("RESET")}")

        print(f"{forecolor("YELLOW")}") 
        prenom =input("\tEntrez le prénom du stagiaire : ")
        print(f"{forecolor("RESET")}")
        while(prenom.__len__() <1):
            print(f"{forecolor("RED")}")
            prenom = input("\tMerci d'entrez un prénom du stagiaire valide : ")
            print(f"{forecolor("RESET")}")

        for i in filiaires :
            print()
            match i :
                case "DEV":
                    print(f"\t{filiaires.index(i)+1}","Développement Digitale.",sep=".",end="")
                case "IR":
                    print(f"\t{filiaires.index(i)+1}","Infrastructure Réseaux",sep=".",end="")
                case "CM":
                    print(f"\t{filiaires.index(i)+1}","Comptabilité et Finance.",sep=".",end="")
                case "GE":
                    print(f"\t{filiaires.index(i)+1}","Gestion d'Entreprises.",sep=".",end="")
        print(f"{forecolor("WHITE")}\n")
        choix_filiaire = input("\tChoissiez une filière : ")

        while(not choix_filiaire.isdigit() or choix_filiaire.__len__() <1 or choix_filiaire not in ["1","2","3","4"]):
            print(f"{forecolor("RED")}")
            choix_filiaire = input("Merci de choissir une filiaire valide ! : ")
        #match filiaire
        choix_filiaire = int(choix_filiaire)
        match choix_filiaire:
            case 1:
                filiaire = filiaires[0]
            case 2:
                filiaire = filiaires[1]
            case 3:
                filiaire = filiaires[2]
            case 4:
                filiaire = filiaires[3]
        #Saisie des notes
        for i in range(5):
            match i:
                case 0:
                    print(f"{forecolor("GREEN")}")
                    note1=input("Entrez la note du français : ")
                    while((not note1.isdigit() or note1.__len__()<1 or note1.__len__()>2)):
                        if(note1.isdigit()):
                            if(int(note1) > 20 or int(note1) < 0 ):
                                print(f"{forecolor("RED")}")
                                note1=input("La note doit être comprise entre 0 et 20 !!! : ")        
                        else:
                            print(f"{forecolor("YELLOW")}")
                            note1=input("Entrez une note valide de Français : ")
                    if(note1.isdigit()):
                        note1=float(note1)
                case 1:
                    print(f"{forecolor("GREEN")}")
                    note2=input("Entrez la note de l'Arabe : ")
                    while((not note2.isdigit() or note2.__len__()<1 or note2.__len__()>2)):
                        if(note2.isdigit()):
                            while(int(note2) > 20 or int(note2) < 0):
                                print(f"{forecolor("RED")}")
                                note2=input("La note doit être comprise entre 0 et 20 !!! : ")
                        else:
                            print(f"{forecolor("YELLOW")}")
                            note2=input("Entrez une note valide de l'Arabe : ")
                    if(note2.isdigit()):
                        note2=float(note2)
                case 2:
                    print(f"{forecolor("GREEN")}")
                    note3=input("Entrez la note de Physique : ")
                    while((not note3.isdigit() or note3.__len__()<1 or note3.__len__()>2)):
                        if(note3.isdigit()):
                            while(int(note3) > 20 or int(note3) < 0):
                                print(f"{forecolor("RED")}")
                                note3=input("La note doit être comprise entre 0 et 20 !!! : ")  
                        else:
                            print(f"{forecolor("YELLOW")}")
                            note3=input("Entrez une note valide de Physique : ")
                    if(note3.isdigit()):
                        note3=float(note3)
                case 3:
                    print(f"{forecolor("GREEN")}")
                    note4=input("Entrez la note des Mathématiques : ")
                    while((not note4.isdigit() or note4.__len__()<1 or note4.__len__()>2)):
                        if(note4.isdigit()):
                            while(int(note4) > 20 or int(note4) < 0):
                                print(f"{forecolor("RED")}")
                                note4=input("La note doit être comprise entre 0 et 20 !!! : ")  
                        else:
                            print(f"{forecolor("YELLOW")}")
                            note4=input("Entrez une note valide des Mathématiques : ")
                    if(note4.isdigit()):
                        note4=float(note4)

                case 4:
                    print(f"{forecolor("GREEN")}")
                    note5=input("Entrez la note de l'Histoire et Géographie : ")
                    while((not note5.isdigit() or note5.__len__()<1 or note5.__len__()>2)):
                        if(note5.isdigit()):
                            while(int(note5) > 20 or int(note5) < 0):
                                print(f"{forecolor("RED")}")
                                note5 = input("La note doit être comprise entre 0 et 20 !!! : ")
                        else:
                            print(f"{forecolor("YELLOW")}")
                            note5=input("Entrez une note valide de l'Histoire et Géographie : ")
                    if(note5.isdigit()):
                        note5=float(note5)
        #Calcul de moyenne
        moyenne = (note1+note2+note3+note4+note5)/5
        #Incrémentation du numéro de stagiaire
        compteur = 0
        for i in stagiaires:
            compteur+=1
        num = compteur
        #append dans la liste principale
        stagiaire = [num,nom,prenom,filiaire,moyenne,note1,note2,note3,note4,note5]
        stagiaires.append(stagiaire)
        print(f"{forecolor("WHITE")}")
        continuer = input(f"Voulez-vous countinuez ? '{forecolor("YELLOW")}non{forecolor("RESET")}' pour retourner au menu : ").lower()
        print()

def recherche_par_num():
    print(f"{forecolor("WHITE")}")
    num = input("Entrez le numéro de l'étudiant :\n")
    length = stagiaires.__len__()
    found = False
    for i in range (1,length):
        if(stagiaires[i][0] == int(num)):
            print("Stagiaire trouvé :")
            print(f"\tNom : {stagiaires[i][1]} ")
            print(f"\tPrénom : {stagiaires[i][2]}")
            print(f"\tFilière : {stagiaires[i][3]}")
            print(f"\tMoyenne : {stagiaires[i][4]}")
            found = True
    if(not found):
        print("Stagiaire non trouvé !")

def recherche_par_nom():
    nom = input("Entrez le nom de l'étudiant :\n")
    length = stagiaires.__len__()
    found = False
    for i in range (1,length):
        if(stagiaires[i][1] == nom):
            print("Stagiaire trouvé :")
            print(f"\tNom : {stagiaires[i][1]} ")
            print(f"\tPrénom : {stagiaires[i][2]}")
            print(f"\tFilière : {stagiaires[i][3]}")
            print(f"\tMoyenne : {stagiaires[i][4]}")
            found = True
    if(not found):
        print("Stagiaire non trouvé !")

def recherche_par_prenom():
    prenom = input("Entrez le prénom de l'étudiant :\n")
    length = stagiaires.__len__()
    found = False
    for i in range (1,length):
        if(stagiaires[i][2] == prenom):
            print("Stagiaire trouvé :")
            print(f"\tNom : {stagiaires[i][1]} ")
            print(f"\tPrénom : {stagiaires[i][2]}")
            print(f"\tFilière : {stagiaires[i][3]}")
            print(f"\tMoyenne : {stagiaires[i][4]}")
            found = True
    if(not found):
        print("Stagiaire non trouvé !")

def afficher_liste_admis():
    length = stagiaires.__len__()
    for i in range (1,length):
        match stagiaires[i][3]:
            case "DEV":
                if(stagiaires[i][4] >= 12):
                    print("La liste des admis en Dev :")
                    print(f"\tNom : {stagiaires[i][1]} ")
                    print(f"\tPrénom : {stagiaires[i][2]}")
                    print(f"\tMoyenne : {stagiaires[i][4]}")
            case "GE":
                if(stagiaires[i][4] >= 12):
                    print("La liste des admis en Ge :")
                    print(f"\tNom : {stagiaires[i][1]} ")
                    print(f"\tPrénom : {stagiaires[i][2]}")
                    print(f"\tMoyenne : {stagiaires[i][4]}")
            case "CM":
                if(stagiaires[i][4] >= 12):
                    print("La liste des admis en Cm :")
                    print(f"\tNom : {stagiaires[i][1]} ")
                    print(f"\tPrénom : {stagiaires[i][2]}")
                    print(f"\tMoyenne : {stagiaires[i][4]}")
            case "IR":
                if(stagiaires[i][4] >= 12):
                    print("La liste des admis en Ir :")
                    print(f"\tNom : {stagiaires[i][1]} ")
                    print(f"\tPrénom : {stagiaires[i][2]}")
                    print(f"\tMoyenne : {stagiaires[i][4]}")

def afficher_liste_filieres():
    length = stagiaires.__len__()
    for i in range (1,length):
        match stagiaires[i][3]:
            case "DEV":
                if(stagiaires[i][4] >= 12):
                    print("La liste des stagiaires en Dev :")
                    print(f"\tNum : {stagiaires[i][0]} ")
                    print(f"\tNom : {stagiaires[i][1]} ")
                    print(f"\tPrénom : {stagiaires[i][2]}")
            case "GE":
                if(stagiaires[i][4] >= 12):
                    print("La liste des stagiaires en Ge :")
                    print(f"\tNum : {stagiaires[i][0]} ")
                    print(f"\tNom : {stagiaires[i][1]} ")
                    print(f"\tPrénom : {stagiaires[i][2]}")
            case "CM":
                if(stagiaires[i][4] >= 12):
                    print("La liste des stagiaires en Cm :")
                    print(f"\tNum : {stagiaires[i][0]} ")
                    print(f"\tNom : {stagiaires[i][1]} ")
                    print(f"\tPrénom : {stagiaires[i][2]}")
            case "IR":
                if(stagiaires[i][4] >= 12):
                    print("La liste des stagiaires en Ir :")
                    print(f"\tNum : {stagiaires[i][0]} ")
                    print(f"\tNom : {stagiaires[i][1]} ")
                    print(f"\tPrénom : {stagiaires[i][2]}")

def modifier_stagiaire():
    num = input("Entrez le numéro du stagiaire :\n")
    while (not num.isdigit() or num.__len__()<1):
        num = input("Entrez le numéro du stagiaire :\n")
    num = int(num)
    length = stagiaires.__len__()
    for i in range (1,length):
        if(stagiaires[i][0]==num):
            print(f"Modification des infos de {stagiaires[i][1]} {stagiaires[i][2]}:")
            def menu_modif():
                print(forecolor("WHITE"))
                print("1.Modifier la note du Français.")
                print("2.Modifier la note de l'Arabe.")
                print("3.Modifier la note de Physique.")
                print("4.Modifier la note des Mathématiques.")
                print("5.Modifier la note du Histoire et Géographie.")
                print("6.Modifier la filière.")
                print("0.Quitter")
                print("RESET")
            stagiaire = stagiaires[i]
            choix = 7
            while(choix !=0 or choix not in [0,1,2,3,4,5,6]) :

                menu_modif()
                choix = int(input("Entrez un choix :\n"))
                match choix:
                    case 1:
                        stagiaire[5] = float(input("Entrez la note de français :\n"))
                        stagiaire[4] = (stagiaire[5]+stagiaire[6]+stagiaire[7]+stagiaire[8]+stagiaire[9])/5
                    case 2:
                        stagiaire[6] = float(input("Entrez la note de l'Arabe :\n"))
                        stagiaire[4] = (stagiaire[5]+stagiaire[6]+stagiaire[7]+stagiaire[8]+stagiaire[9])/5
                    case 3:
                        stagiaire[7] = float(input("Entrez la note du Physique :\n"))
                        stagiaire[4] = (stagiaire[5]+stagiaire[6]+stagiaire[7]+stagiaire[8]+stagiaire[9])/5
                    case 4:
                        stagiaire[8] = float(input("Entrez la note des Mathématiques :\n"))
                        stagiaire[4] = (stagiaire[5]+stagiaire[6]+stagiaire[7]+stagiaire[8]+stagiaire[9])/5
                    case 5:
                        stagiaire[9] = float(input("Entrez la note du Histoire et Géographie. :\n"))
                        stagiaire[4] = (stagiaire[5]+stagiaire[6]+stagiaire[7]+stagiaire[8]+stagiaire[9])/5
                    case 6:
                        stagiaire[3] = input("Entrez une filière ('DEV','GE','CM','IR')")
                        stagiaire[5] = float(input("Entrez la note de français :\n"))
                        stagiaire[6] = float(input("Entrez la note de l'Arabe :\n"))
                        stagiaire[7] = float(input("Entrez la note du Physique :\n"))
                        stagiaire[8] = float(input("Entrez la note des Mathématiques :\n"))
                        stagiaire[9] = float(input("Entrez la note du Histoire et Géographie. :\n"))
                        stagiaire[4] = (stagiaire[5]+stagiaire[6]+stagiaire[7]+stagiaire[8]+stagiaire[9])/5
                stagiaires[i] = stagiaire
                print(stagiaires[i])

def afficher_liste_stagiaires():
    for i in stagiaires:
        print(i) 

def select_menu():
    x=-1
    while(x != "0"):
        menu()
        x = input("Entrez un choix : ")
        while(not x.isdigit() or x not in ["0","1","2","3","4","5","6","7","8"] ):
            x = input("Merci de choisir un choix valide ! : ")  
        match x :
            case "1":
                ajouter_stagiaire()
            case "2":
                afficher_liste_stagiaires()
            case "3":
                recherche_par_num()
            case "4":
                recherche_par_nom()
            case "5":
                recherche_par_prenom()
            case "6":
                afficher_liste_admis()
            case "7":
                afficher_liste_filieres()
            case "8":
                modifier_stagiaire()
            case "0":
                print("Au revoir !")

select_menu()


