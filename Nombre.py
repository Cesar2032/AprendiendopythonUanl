# en las dos lineas siguientes se pide al usuario que registre el nombre y apellidos
nombre=input("nombre:")
apellidos=input("apellidos:")
# a qui se realiza una concatenacion es decir juntamos nombre y apellidos
nombreCompleto=nombre+" "+apellidos
# en esta parte al nombre completo se le aplicara un upper lo que es retornar en Mayusculas
nombreCompleto=nombreCompleto.upper()
# imprimimos o damos salida al nombre en mayusculas
print(nombreCompleto)