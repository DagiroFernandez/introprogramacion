numi=int(input("ingresa el numero inicial: "))
numf=int(input("ingrese en numero final: "))
numdenrango=[]
suma=0
suma2=0
for i in range(numi,numf+1):
    print( i,end="")
print("")

for i in range(numi,numf+1):
    if i%2==0:
        suma=suma+i
    else:
        suma2=suma2 +i
print("la suma de los pares es",suma,end="")
print("")
print("la suma de los impares es",suma2)