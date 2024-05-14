def infoContacto(nombre, telefono="No tiene") :
    print(f"Su nombre es {nombre} y su telefono : {telefono}")

import os
os.system("cls")

infoContacto("Andres Almaguer") #No tiene telefono pero
#En consola pone el valor por defecto que no tiene
#No marca el error porque en el parametro
#Se definio un valor por defecto de lo contrario
#Marcaria error


infoContacto("AlmaguerUSA", "+524321320999")
#En este caso como si tiene telefono pone el telefono
#En lugar del valor por defecto ♥
