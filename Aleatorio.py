# en python trabajamos con muchos numeros aleatorios y para ello utilizaremos o trabajaremos con el objeto random
import random
#  deinimos la variable float la cual es para numeros en decimal o no enteros.
numero1=float(10.5)
# a continuacion realizamos una serie de instrucciones, para ello declaramos con def y todo aquello que este en espacio a la derecha estara dentro de la funcion
def miFuncion():
# se convierte el numero dado en float y si solo esta en el randrange, importamos el modulo
    numero2=float(random.randrange(1,10))
    mensaje="la suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1 + numero2))
# ejecutamos la funcion antes mencionada
miFuncion()