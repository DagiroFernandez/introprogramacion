partido_votado = input("ingrese el partido politico deseado entre MAS o UNIR: ")
if partido_votado == "MAS" or partido_votado == "mas":
    print(f"Usted a votado por {partido_votado}, te jodiste :v ")
elif partido_votado == "UNIR"or partido_votado == "unir":
    print(f"Usted ha votado por {partido_votado}")
else:
    print("EL voto es invalido")