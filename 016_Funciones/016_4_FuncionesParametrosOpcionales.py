def apellidoynombre(apellido, nombre):
    limpiarpantalla()
    print(f"Este es el nombre {nombre} y este es el apellido {apellido}")

def limpiarpantalla():
    import os 
    os.system("cls")

#Se definen los parametros de esta forma aqui no importa 
#El nombre, solo que esten definidos eso es todo
apellidoynombre(nombre="Andres", apellido="Almaguer")