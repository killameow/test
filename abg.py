massiv=[]
for i in range(5):
    massiv.append(int(input()))

def minfunc():
    min_=massiv[0]
    for i in range(5):
        if(massiv[i]<min_):
            min_=massiv[i]
    return min_


print(minfunc())
