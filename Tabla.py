# solicitamos en esta linea que el usuario proporcione un numero del 1 al 9
numero=input("Dame un numero del 1 al 9: ")
# le damos un valor como entero
numero=int(numero)
# aplicaremos el ciclo for en un rango del 1 al 11 y daremos salida en forma de multiplicacion al numero proporciona hasta el 10 y dando el resultado de cada operacion

for i in range(1,11):
    salida="{} * {} = {}"
# damos salida imprimiendo la multiplicacion completa, o el formato
    print(salida.format(numero,i,i*numero))