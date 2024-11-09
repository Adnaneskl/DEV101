def somme (x,y):
    s = x + y
    return s
def produit(x,y):
    p = x*y
    return p
def test():
    c=input(f"{'\033[91m'} saisir un choix:{"\033[0m"}")
    while (not c.isdigit()):
        c=input("merci de saisir un choix valide")
    return c
c = 0
while (c != 3):
    print("1.Somme")
    print("2.Produit")
    print("3.pour Quitter !!")
    c = int(test())
    if c == 3 :
        break
    n = float(input("enter la premier nombre :"))
    b = float(input("enter la deuxieme nombre :"))
    match c:
        case 1 : 
            print(somme (n,b))
        case 2 : 
            print(produit (n,b))
