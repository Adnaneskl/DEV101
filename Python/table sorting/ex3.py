T=[10,0,1,12,0]
tap=False
while top!=True:
    top=True
    for i in range(0,len(t)-1):
        if(T[i]>T[i+1]):
            Tap=False
            x=T[i]
            T[i]=T[i+1]
        