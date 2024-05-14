import os

os.system("cls")

texto = ""
continuar = "seguir"

                #Es sensible a las mayusculas y minusculas
while continuar == "seguir" : #Se repite estructura repetitiva

    texto += str(input("Dame un numero : "))

    #Pregunta si quiere seguir y esto
    continuar = input("Deseas continuar? (seguir): ") 
    #Es lo que realmente define si se repite o no se repite

    if continuar == "seguir" :
      texto += ","  
    else :
        break

print(texto)
