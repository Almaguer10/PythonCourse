n1 = int(input("Dame un numero : "))
n2 = int(input("Dame otro numero : "))

#Si no se convirte en entero solo concatenará el texto

mensaje = f"""Para los numeros {n1} y {n2}
la suma es : {n1+n2}
la resta es : {n1-n2}
la multiplicacion es : {n1*n2}
la division es : {n1/n2}
"""


print(mensaje)