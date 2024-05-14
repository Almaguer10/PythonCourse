import os

os.system("cls")

encontrado = False

for numeros in range(6):
    if numeros == 7 :
        encontrado = True
        break
else:
    print("No fue encontrado")

if encontrado: 
    print("Si fue encontrado")