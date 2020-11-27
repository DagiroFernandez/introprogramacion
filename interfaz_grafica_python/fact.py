FACT=[]
def fact (numero):
    for i in range(1, numero):
        numero = numero * i
    FACT.append(numero)



for n in range(1,21):
    fact(n)
print(f"FACT=",FACT)