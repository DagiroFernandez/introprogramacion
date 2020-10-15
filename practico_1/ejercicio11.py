from time import localtime
t = localtime()
t.tm_mday
14
t.tm_mon
10
t.tm_year
2020
dia_nac = int(input("ingrese el dia de nacimiento: "))
mes_nac = int(input("ingrese el mes de nacimiendo"))
año_nac = int(input("ingrese el año de nacimiento: "))
año_res= t.tm_year-año_nac
if dia_nac > t.tm_mday and mes_nac > t.tm_mon:
    print(f"Usted tiene {año_res}")