dia = int(input("ingresa el dia de tu nacimiento: "))
mes = int(input("ingresa el mes de tu nacimiento: "))
año_nacimiento = int(input("ingresa el año de tu nacimineto: "))
año_actual = int(2020)
edad = año_actual - año_nacimiento
if(edad >= 18):
    print(f"Tienes {edad} años, eres mayor de edad ;)")
else:
    print(f"Tienes {edad} años, eres menor de edad :(")
