numero_t = int(input("n: "))
suma= 0
for numero_t in range(1,numero_t+1):
    if numero_t % 2 ==0:
        signo= -1
    else:
        signo = 1
    valor_actual = signo / (1+2*(numero_t-1))
    suma= suma + valor_actual
pi = 4*suma
print(pi)