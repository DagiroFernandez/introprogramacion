num=int(input("Ingrese el numero capicua: "))
numstr = str(num)
if numstr == numstr[::-1]:
    print(num, "El numero es un numero capicua")
else:
    print(num, "El numero no es un numero capicua")