t=[0]*10
for i in range(10):
    n = int(input("entrez la premier note :"))
    t[i] = n
M = 0
for i in range(10):
    M = t[i] + M
print("la moyenne est :", M / 10)