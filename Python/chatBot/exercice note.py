ligne = input("Entrez le nombre des matières : ")
colonne = input("Entrez le nombre des élèves : ")
digit_counter = 0
is_digit = False


while(digit_counter <1 and is_digit == False):
    if(ligne.__len__()==0):
        print("Empty input is not allowed")
    else :
        for i in ligne:
            for j in [1,2,3,4,5,6,7,8,9]:
                if(i == str(j)):
                    digit_counter+=1
                    is_digit = True
                else:
                    is_digit = False
        if(ligne.__len__() != digit_counter or is_digit == False):
            print(f"'{ligne}' is not a number, please try again.")
            print(digit_counter)
            digit_counter = -1
        else:
            ligne = int(ligne)
            colonne = int(colonne)
x=-1
if(digit_counter>0 and is_digit == True):
    t=[[0]*colonne for i in range(ligne)]
    while(x!=4):
        print("Menu :")
        print("\t1.Entrer les nom","2.Entrer les notes","3.Afficher les moyennes","4.Quitter",sep="\n\t")
        x=int(input("\n\tEntrez votre choix : "))
        match x :
            case 1:
                for p in range(colonne):
                    t[0][p] = input(f"\t\t\tEntrez le nom de l'élève numéro {p+1}: ")
            case 2:
                for p in range(colonne):
                    for m in range(1,ligne):
                        note = int(input(f"\t\t\tEntrez la note numéro {m} de l'élève numéro {t[0][p]} : "))
                        while(note<0 or note >20 and str(note).__len__() != 0):
                            print("\t\t\tMerci d'entrez une note valide !!")
                            note = int(input(f"\t\t\tEntrez la note numéro {m} de l'élève numéro {t[0][p]} : "))
                        t[m][p]= note
            case 3:
                search_name=input("\t\t\tEntrez le nom de l'élève que vous chercher : ")
                ligne +=1
                for i in range(ligne-1):
                    if(str(t[0][i]) == search_name):
                        for j in range(i):
                            print(f"\t\t\tLes notes de {t[0][i]} est : \n\t\t\t\t",t[i][j])
                print(t)
