import os

os.system("cls")

continuar = "S"

while continuar.lower() == "s" :

    continuar = str(input("Dame una letra (s) para continuar :"))
    
    if continuar.lower() == "s":
        if continuar.isupper() :
            print("Es mayuscula y continua")
    else :

        if continuar.isupper():
            print("Es mayuscula pero no continua")

        if continuar.islower():
            print("Es miniscula pero no continua")
            
        break