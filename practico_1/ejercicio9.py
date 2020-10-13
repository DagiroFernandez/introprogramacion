num1 =int(input("ingrse un numero: "))
num2 = int(input("ingrese otro numero: "))
ope = input("ingrese un operador: ")
resul_suma = (num1+num2)
resul_resta= (num1-num2)
resul_mul=(num1*num2)
resul_divi= (num1/num2)
resul_poten = (num1**num2)
if ope == "+":
    print(f"{num1}+{num2}={resul_suma}")
elif ope == "-":
    print(f"{num1}-{num2}={resul_resta}")
elif ope == "*":
    print(f"{num1}*{num2}={resul_mul}")
elif ope == "/":
    print(f"{num1}/{num2}={resul_divi}")
elif ope == "**":
    print(f"{num1}**{num2}={resul_poten}")