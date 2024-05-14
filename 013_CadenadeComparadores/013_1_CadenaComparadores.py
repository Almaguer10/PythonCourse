"""La cadena de comparadores nos ayuda a comprar
un valor que este dentro de un rango especifico

Por ejemplo queremos comparar una edad que este
entre 15 y 65 Años

Podemos usar una estructura if con un operador
logico and de la sig manera

if edad > 15 and edad < 65
de esta manera podriamos expresarla pero hay una
cadena de comparadores que podemos utilizar
para simplificarlo

"""
import os 
edad = 16

if 15 < edad < 65:
    os.system("cls")
    print("Si esta en el rango")

"""De esta manera podemos ir simplificando codigo"""
#De la misma forma que con operadores ternarios
#En operadores ternarios solo se puede hacer una cosa a la vez en el if
#No se le pueden agregar multiples opciones