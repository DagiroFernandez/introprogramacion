estatura = float(input("ingrese su estatura: "))
peso = float(input("ingrese su peso: "))
edad = int(input("ingrese su edad: "))
indice_m = peso // (estatura **2)
if edad < 45 and indice_m <22.0:
    print("su riesgo es bajo")
elif edad < 45 and indice_m >= 22.0:
    print("su riesgo es medio")
elif edad >= 45 and indice_m < 22.0:
    print("su riesgo es medio")
elif edad >= 45 and indice_m >= 22.0:
    print("Su riesgo es alto, baje de peso urgente :v")