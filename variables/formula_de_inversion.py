monto_a_invertir = int(input("ingrese monto a invertir: "))
interes_anual = int(input("ingrese interes anual: "))
numero_de_años = int(input("ingrese numero de años: "))
ganancia_neta = interes_anual + 1
ganancia_neta = ganancia_neta ** numero_de_años
ganancia_neta = ganancia_neta * monto_a_invertir
print(f"Tu ganancia neta es {ganancia_neta}bs")