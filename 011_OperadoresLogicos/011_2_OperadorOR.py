import os

op1 = False
op2 = False

if op1 or op2:
    if op1 and op2:
        print("Opcion 1 Activada y Opcion 2 Activada")
    else:
        if op1:
            print("Opcion 1 Activada y Opcion 2 Desactivada")
        else:
            print("Opcion 2 Activada y Opcion 1 Desactivada")
else:
    print("Opciones Desactivadas")