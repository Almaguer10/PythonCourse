#Se define el nombre del parametro con un * al inicio
#Para indicar que es un xarg

#        *xarg
def suma(*numeros) :
    resultado = 0
    #Se manipulan datos con un for ya que 
    #No se sabe cuantos serán y serán diferentes
    #En cada vez que se llame la función
    for numero in numeros:
        resultado += numero
    
    print(f"El resultado de la suma fue : {resultado}" )

#Se manda a llamar la funcion con los argumentos que queramos
#La funcion siempre va a funcionar no importará el numero de
#Argumentos que le mandemos el for lo sabrá manipular
suma(10,15,30)
suma(10,54,56)
suma(10,54)
suma(5)