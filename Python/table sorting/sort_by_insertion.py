T=[16,79,15,43,26,33]
n=6
for i in range(1,n):
    p=T[i]
    j = i
    while(j>0 and T[j-1]>p):
        T[j] = T[j-1] 
        j=j-1
    T[j] = p
print(T)