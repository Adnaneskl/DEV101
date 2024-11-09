def choix (choix):
    print("____________")
    print("1. Saisir un etudiant !")
    print("2. Saisir plusiurs etudiant !")
    print("3. Afficher la list des etudiants !")
    print("4. Rechercher un etudiant par numero !")
    print("5. Rechercher un etudiant par nom !")
    print("6. Quitter !")
    num = ["1","2","3","4"]
    choix = ""
    while (choix not in num):
        choix = input("Entrez Votre Choix :")
    choix = int(choix)
    return choix
# a functions that return the filiare
def filiare():
    filaires=["dev","ge","cm"]
    filiar = ""
    while (filiar not in filaires):
        filiar = input('Saisir le filiare { "dev" , "ge" ou "cm" } :')
    return filiar
#create a empty list 
students = []

# Function to add a new student
def add_student(i):
    student = []
    student.append(i)
    student.append(input("Entrez le nom d'etudaint :"))
    student.append(input("Entrez le Prenom d'etudaint :"))
    student.append(filiare())
    student.append(int(input("Entrez la 1er Note :")))
    student.append(int(input("Entrez la 2eme Note :")))
    student.append(int(input("Entrez la 3eme Note :")))
    student.append(int(input("Entrez la 4eme Note :")))
    student.append(int(input("Entrez la 5eme Note :")))
    student.append((student[4] + student[5] + student[6] + student[7] + student[8]) / 5)
    students.append(student)
#function pour afficher la list des etudiants
def afficher ():
    for i in range (len(students)):
        print(f"eleve N° {i+1} est : {students[i][1]} {students[i][2]}")

#function pour rechercher pour un eleve par numero
def recher_num ():
    num = int(input("Rechercher un etudiant par numero :"))
    for i in range (len(students)):
        if students[i][0] == num :
            print(f"Ce numero ({num}) est pour cet etudiant : {students[i][1]} {students[i][2]}")
            break
        else:
            print("le nombre Invalid !!")
def recher_nom ():
    nom = input("Rechercher un etudiant par nom :")
    for i in range (len(students)):
        if students[i][1] == nom :
            print(f" l'etediant est : {students[i][1]} {students[i][2]}")
        else:
            print("le nombre Invalid !!")

i = 1
x = choix(choix)
while (x != 6 ):
    match x:
        case 1:
            print("____________")
            add_student (i)
            print("____________")
            x = choix(choix)
            i += 1
        case 2:
            n = ""
            while( n != "stop"):
                add_student (i)
                n = input("Entrez 'stop' Pour Quitter le saisir :")
            i += 1
            x = choix(choix)
        case 3:
            afficher()
            x = choix(choix)
        case 4:
            recher_num ()
            x = choix(choix)
        case 5:
            recher_nom()
            x = choix(choix)