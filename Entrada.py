# se pide que se registre la entrada un numero
entrada=input()
# demostramos una salida en la clase o tipo de dato que es
print(type(entrada))
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if(esEntero):
# si es entero se ejecutara o realizara lo siguinete dando salida a un mensaje
    print("Dato entero. Muy bien!")
else:
# por lo contrario si esta condicion no se cumple imprimira lo establecido
    print("Dato no es entero. Intentar nuevamente.")