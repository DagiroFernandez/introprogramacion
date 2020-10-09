num1 = int(input("Ingrse un numero: "))
num2 = int(input("Ingrese un numero"))
cos = num1 //num2
rest = num1 % num2
if num1 % num2==0:
    print("La division es exacta")
else:
    print("La division no es exacta")
print(f"cociente = {cos}")
print(f"resto {rest}")