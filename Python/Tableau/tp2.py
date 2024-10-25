t=[0]*10
t[0] = int(input("Entrez la 1er Nombre :"))
max = t[0]
for i in range(1,10):
    t[i] = int(input(f"Entrez la {i+1}eme Nombre :"))
    if t[i-1] < t[i]:
        max = t[i]
print(t)
print(max)