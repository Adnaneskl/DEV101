from pathlib import Path
import os

list_quartiers = []

#currentPath = Path.cwd()

def justify_center(string:str,symbol:str):
    terminal_width = os.get_terminal_size().columns
    string_len = len(string)
    new_string_size = int(terminal_width/2) - int(string_len/2) 
    if(new_string_size*2+string_len > terminal_width):
        print("\n",symbol*new_string_size,string,symbol*(new_string_size-1),sep="")
    else:
        print("\n",symbol*new_string_size,string,symbol*new_string_size,sep="")

def justify_left(string:str,symbol:str):
    terminal_width = os.get_terminal_size().columns
    string_len = len(string)
    left_string_length = int(((terminal_width)/2)-(terminal_width*0.2))
    right_string_length = int(string_len + (terminal_width-(left_string_length+string_len)))
    while(left_string_length + right_string_length + string_len > terminal_width):
        right_string_length-=1
    print(symbol*left_string_length,string,sep="",end="")

def menu():
    justify_center("Gestion des quartiers","~")
    print("Taper le numéro de l'opération à réaliser :")
    print("1 ----- Ajout un nouveau quartier. (4 pts)")
    print("2 ----- Afficher les quartiers. (3 pts)")
    print("3 ----- Supprimer un quartier. (3 pts)")
    print("4 ----- Chercher un quartier. (3 pts)")
    print("5 ----- Sauvegarder dans un fichier. (4 pts)")
    print("6 ----- Quitter (1 pt)")
    justify_center("","~")

def quartiers(nom : str,surface: float,nbr_habitants :int):
    quartiers= [nom,surface,nbr_habitants]
    return quartiers

def getListFromFile():
    if(os.path.exists("liste_quartiers.txt")):
        file = open("liste_quartiers.txt","r")
        list_quartiers = file.readlines()
    else :
        file = open("liste_quartiers.txt", "w")
        list_quartiers = []

def ajouter_quartier():
    justify_center(" Ajout de quartier ","~")
    def verifier_existant():
        justify_left("Nom du quartier : "," ")
        _=input("")
        for i in list_quartiers:
            while(_ == i[0]):
                justify_left("ce nom existe déjà, Veuillez choisir un autre nom : "," ")
                _=input()
        return _
    def verifier_digit():
        _=input(justify_left("Surface : "," "))
        while (not _.isdigit()):
            _=input(justify_left("La surface est un chiffre ! Réssayez : "," "))
        print(_)
        return float(_)
    def verifier_entier():
        _=input(justify_left("Nombre d'habitants : "," "))
        while(not _.isdigit()):
            _=input(justify_left("Le nombre d'habitants doit être un entier ! Réssayez : "," "))
            print(_)
        return int(_)

    list_quartiers.append(quartiers(verifier_existant(),verifier_digit(),verifier_entier()))

def afficher_liste_quartier():
    justify_center(" Liste des quartiers ","~")
    print()
    for i in list_quartiers:
        justify_left(f"Nom du quartier : {i[0]}"," ")
        justify_left(f"La surface quartier : {i[1]}"," ")
        justify_left(f"Nombre des habitants du quartiers : {i[2]}"," ")
        if(i == list_quartiers[-1]):
            justify_center("","~")
        else:
            print()
def supprimer_quartier():
    saisie = input("\nEntrez le nom du quartier à supprimer : ")
    for i in list_quartiers:
        if (i[0] == saisie):
            print(f"\nQuartier {i[0]} Bien supprimé !\n")
            list_quartiers.remove(i)
        else :
            print("Le nom de quartier n'existe pas !")


def save():
    file = open("liste_quartiers.txt","w")
    for i in list_quartiers:
        pass

while(True):
    getListFromFile()
    menu()
    saisie = input("Entrez votre choix : ")
    while(saisie not in ["1","2","3","4","5"] and saisie != "6"):
        saisie = input("Entrez un choix valide : ")
    match saisie:
        case "1":
            ajouter_quartier()
        case "2":
            afficher_liste_quartier()
        case "3":
            supprimer_quartier()
        case "4":
            pass
        case "5":
            pass
        case "6":
            break

