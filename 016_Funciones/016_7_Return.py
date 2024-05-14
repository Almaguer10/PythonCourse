def calcular_promedio(*notas):
    promedio = 0

    for nota in notas:
        promedio += nota

    promedio /= (len(notas))

    return promedio #Regresamos el promedio calculado por medio
    #De un xargs podemos calcular cualquier promedio
    #De cualquier longitud

#Definimos la funcion que va a mostrar el promedio
def mostrar_promedio(p_promedio_final):
    print(f"El promedio es : {p_promedio_final}")

#Creamos funcion para limpiar pantalla
def limpiar_pantalla():
    import os 
    os.system("cls")

#Limpiamos pantalla por medio de la funcion definida
limpiar_pantalla()

#Mostramos el promedio por una funcion pasandole
#El promedio desde otra funcion
mostrar_promedio(calcular_promedio(10,10,10))
mostrar_promedio(calcular_promedio(9,9,8,10))