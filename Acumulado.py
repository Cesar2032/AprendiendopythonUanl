# a qui declaramos las variables
acumulado=int(0)
numero=str("")
# esta condicion ira pidiendo o solicitando numero enteros y si solo su numero es vacio el programa dara
# el total acumulado y imprimira salida del del programa.
while True:
    numero=input("dame un numero entero: ")
    if numero=="":
        print("vacio. salida del programa. ")
        break
    else:
# en esta parte de codigo se ira sumando el acumulado mas numero entero ingresado, al momento
# de salir del programa tendra una salida diciendo monto acumulado y la cantidad
        acumulado+=int(numero)
        salida="monto acumulado: {}"
        print(salida.format(acumulado))