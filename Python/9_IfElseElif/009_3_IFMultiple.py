def verificar(edad):
    if edad < 0:
        print("Es imposible")
    elif edad < 18:
        print("No puede ver la pelicula, es menor de edad")
    else:
        print("Puedes ver la pelicula")

verificar(-5)
verificar(15)
verificar(18)

#Verificamos multiples condiciones para tomar la mejor desicion.
