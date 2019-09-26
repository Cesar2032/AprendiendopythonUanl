# basicamente i es la base y j el elemento
for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    print()
    for j in range(1,11):
        salida="{} X {} = {}"
        print(salida.format(i,j,i*j))
    else:
# este es el ultimo paso que es imprimir resultados despues de cumplir con las iteraciones
        print()