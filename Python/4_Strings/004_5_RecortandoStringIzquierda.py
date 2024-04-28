nombre = "Andres Alm"
#         ||||||!|||
# Indices 0123456789

# print1  012345 . Igual que el print 3
# print2  0123456789
# print3  012345 - Igual que el print 1
# print4  01234567 Igual que el print 5
# print5  01234567 Igual que el print 6

print(nombre[0:5])  #Donde 0 es donde inicia y 5
# Son las posiciones que va a tomar
# A partir de donde incia


print(nombre[0:])   #Donde empieza a tomar todo desde la pocisión 0 y como no se
# Indicó toma todo lo que resta desde la posición que se indique hasta el final
# (nombre[0:len(nombre)]) podriamos decir que es asi. como se indica al inicio de la fila

print(nombre[:5])   #Funciona al igual que el primero porque como no se define nada
#Por defecto el editor de texto predefine 0 y empezaria desde el inicio basicamente.

print(nombre[0:-2]) #Funcionaria 0 desde donde inicia hasta lo que mide la longitud
#menos lo que le indiquemos en este caso el menos 2 ([0:len(nombre)-2])
print(nombre[0:len(nombre)-2])#Esta funciona como el caso pasado

print(nombre[:]) #print(nombre[0 : len(nombre)])
print(nombre[0:len(nombre)])


