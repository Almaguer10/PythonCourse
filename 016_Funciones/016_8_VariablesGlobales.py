"""El Definir variables globales no es una buena practica
en Python ya que a veces estas variables se usan
en multiples funciones y suelen cambiar el tipo de 
dato lo que puede surgir un error en una funcion
que necesite esa variable en cierto tipo de dato"""
import os
os.system("cls")
#Esta variable puede ser usada dentro de cualquier funcion
#Pero no puede ser modificada dentro de una funcion
nombre = "Varible Global"

def funcion1():
    #nombre = "Variable Global desde funcion 1 modificada"
    #No se puede modificar una variable global dentro de una funcion
    global dentroFuncion
    dentroFuncion = "Estoy dentro de funcion 1"
    print(f"2. {dentroFuncion} : {nombre}")
    dentroFuncion = "Estoy en funcion 1, Me convierto en global"
    print(f"3. {dentroFuncion}")

def funcion2():
    dentroFuncion = "Vengo de la funcion 1 pero me modifique"
    print(f"4. Dentro de funcion 2 : {dentroFuncion}")

print(f"1. Estoy fuera de las funciones : {nombre}")
funcion1()
funcion2()


#Como se puede observar no se puede modificar las variables
#Globales dentro de una funcion amenos que hayan sido 
#Creadas dentro de una funcion

#Por defecto las variables que se definen fuera de la funcion
#Ya son globales