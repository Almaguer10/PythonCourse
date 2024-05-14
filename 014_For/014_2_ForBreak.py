import os

os.system("cls")

buscarnum = 2

for indice in range(7):
    print(f"{indice+1}.")
    if indice == buscarnum:
        print("Encontrado")
        break #interrumpe la iteracion porque se cumplio la condicion if
