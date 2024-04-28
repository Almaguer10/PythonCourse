import os

edad = int(input("Dame tu edad : "))
os.system("cls")
limite_min = int(input("Dame el limite minimo : "))
os.system("cls")
limite_max = int(input("Dame el limite maximo : "))
os.system("cls")

if edad > limite_min and edad <limite_max:
    print(f"Eres mayor a {limite_min} y menor a {limite_max} y tu edad es: {edad}")
else:
    print(f"Tal vez eres menor de edad o mayor a {limite_max}")