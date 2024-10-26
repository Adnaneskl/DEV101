n = 0
T=[9,4,65,1,32,78,15,22]
for n in T:
    n+=1
for i in range(n-1):
    index = i
    for j in range(i+1,n):
        if(T[j]) < T[index]:
            index=j
    Temp = T[index]
    T[index] = T[i]
    T[i]=Temp
print(T)