import os

os.system("cls")

#Inciamos contador que nos ayudará a detener el WHILE
numero = 1
texto = ""

#Estructura de control While
while numero <= 10: #Evalua si el ciclo debe terminar o seguir
    texto += str(f"{numero}, ")
    numero += 1 #Va aumentando su valor para que el ciclo termine

print(texto)
input("Presione una tecla para continuar: ")

os.system("cls")

print("Su ciclo ha terminado")