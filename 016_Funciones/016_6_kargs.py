#Definimos los Kargs con **
#Estos nos ayudarán a crear variables dentro de una variable
#Como un arreglo para ser mas especifico

"""
A diferencia de los xargs que manejabas con for aqui si puedes
ponerles etiquetas y es facil para datos mas estructurados
"""
def presentarme(**personas) :
    print(f"Hola mi nombre es : {personas["nombre"]}, mi apellido es : {personas["apellido"]}, {personas["desc"]}")

import os 
os.system("cls")

#Definimos los kargs en los argumentos con su nombre
#Su asignacion y estos los mandamos a llamar en la funcion
#Su nombre nos ayudará como indice para poder
#Acceder a su valor
presentarme(nombre="Mizty", apellido="Lopez", desc="Soy la niña más guapisima del universo ♥")
presentarme(nombre="Andrés", apellido="Almaguer", desc="Soy el novio de Mizty Lopez ♥\n")
