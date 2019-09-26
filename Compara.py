# se pide el ingreso de dos numeros de variable numero1 y numero2, despues damos la salida juntando los numeros siendo separados solo por una y
numero1=input("numero 1: ")
numero2=input("numero 2: ")
salida="numeros proporcionados: {} y {}. {}."
# a continuacion se realiza una condicion que dice que si numero1 es igual a numero2, imprima los numeros son iguales
if(numero1==numero2):
    print(salida.format(numero1, numero2, "los numeros son iguales"))
else:
# esta indicacion dice que si numero1>numero2 imprima el mayor es el primero
    if numero1>numero2:
        print(salida.format(numero1, numero2, "el mayor es el primero"))
    else:
# esta indicacion dice que si numero1<numero2 imprima el mayor es el segundo

        print(salida.format(numero1, numero2, "el mayor es el segundo"))