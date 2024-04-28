gas = False
encendido = False

if gas and encendido :
    print("Avanzar")
elif not gas and not encendido:
    print("Ponle gas y enciendelo")      
else:
    if not gas:
        print("Ponle gas")
    else:
        print("Enciendelo") 