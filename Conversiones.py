#declaramos una variable str, para una cadena de numeros
numero="1234"
#A continuacion una salida de tipo dato
print(type(numero))
#convertimos la cadena a int, numeros enteros
numero=int(numero)
#damos una salido al tipo que seria int o el tipo que sea en su caso
print(type(numero))
salida="El numero utilizado es {}"
#En esta parte del codigo damos salida al texto y al numero que este entre {}
print(salida.format(numero)) 