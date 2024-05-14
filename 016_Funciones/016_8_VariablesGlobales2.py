"""Compartiendo variable global modificando dentro de funciones"""
import os
os.system("cls")

nombre = "Varible Global"

def funcion1():
    nombre = "2. Variable Global modificada desde funcion 1"
    print(nombre)

def funcion2():
    nombre = "3. Variable Global modificada desde funcion 2"
    print(nombre)

print(f"1. Estoy fuera de las funciones : {nombre}")
funcion1()
funcion2()
print(f"4. Estoy fuera de las funciones despues de modificaciones : {nombre}")


#Como se puede observar no se puede modificar las variables
#Globales dentro de una funcion amenos que hayan sido 
#Creadas dentro de una funcion las que se definen afuera de 
#Funciones nunca cambian

#Por defecto las variables que se definen fuera de la funcion
#Ya son globales pero su valor se conserva a menos
#Que se modifique en su mismo scoope