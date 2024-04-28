nombre = "   andres almaguer   "

print(nombre.capitalize()) #Como no encontro ningun caracter en la primera posicion no hace absolutamente nada
print(nombre.title()) #Aun que haya espacios sigue poniendo en mayusculas las primeras letras de cada palabra.
print(nombre.strip()) #Elimina los espacios de las orillas es como el trim de algunos otros lenguajes de programacion

#Para solucionar lo de capitalize realizamos el siguiente codigo

print(nombre.strip().capitalize())