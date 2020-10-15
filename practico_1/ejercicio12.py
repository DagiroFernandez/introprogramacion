num_p = int(input("Ingrese el numero de palabras que ingresara: "))
p_larga = ""
p_corta=""
for i in range(1,num_p+1):
    palabra_in= input("ingrese una por una las palabras: ")
    if len(palabra_in) > len(p_larga):
        p_larga = palabra_in
    elif len(palabra_in ) < len (palabra_in):
        p_corta = palabra_in
print("La palabra mas larga es", (p_larga))
print("La palabras mas corta es", (p_corta))
