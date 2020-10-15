n = int(input("ingrese un numero: "))
while n!= 1:
    if n % 2==0:
        print(n//2)
        n = n//2
    else:
        print(n*3+1)
        n=n*3+1
