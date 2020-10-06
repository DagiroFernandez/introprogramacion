año = int(input("Ingrese año: "))
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print("El añor es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("EL año es bisiesto")
else:
    print("El año no es bisiesto")
