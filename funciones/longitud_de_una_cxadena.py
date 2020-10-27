def longcadena(x):
    contador =0
    for i in (x):
        contador= contador +1
    return(contador)
x =input("Ingrese una cadena: ")
print(x, "tiene", longcadena(x), "caracteres")