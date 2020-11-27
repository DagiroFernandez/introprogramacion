vectorA=[]
vectorB=[]
vectorsuma=[]
for i in range (0,5):
    numA=int(input("ingrese un numero para A:"))
    vectorA.append(numA)
for i in range(0,5):
    numB=int(input("ingrese un numero para B: "))
    vectorB.append(numB)
for i in range(0,5):
    suma=vectorA[i]+vectorB[i]
    vectorsuma.append(suma)
print(vectorA)
print(vectorB)
print(vectorsuma)
