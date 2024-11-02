ligne=input("Entrez le nombre des matières : ")
colonne=input("Entrez le nombre des élèves : ")
digit_counter = 0
for i in ligne:
    for j in range(1,10):
        if(i == str(j)):
            digit_counter+=1
if(digit_counter == ligne.__len__() and ligne.__len__()!=0):
    print(f"'{ligne}' is digit")
elif(ligne.__len__()==0):
    print("Empty input is not allowed")
else:
    print(f"'{ligne}' is not a digit")