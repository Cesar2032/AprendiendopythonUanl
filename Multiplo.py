# solicitamos un numero y este es guardado en int 
numero=int(input("dame un numero entero: "))
# del numero ingresado si el residual es 0 significa que el numero es multiplo.
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
# a qui se pone una condicion o indicion la cual dice que si es multiplo de 3 y multiplo de 5 o multiplo de 7 imprime correto
# si no incorrecto
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("correcto. ")
else:
    print("incorrecto. ")
