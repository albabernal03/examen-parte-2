

def menu():
    print('.:MENU.:')
    print('1.Comprobar matriz')
    print('2.Escribir una cadena con un numero limitado de caracteres')
    print('3.Imprimir una lista de numeros que vaya de forma ascendente o descendente')
    print('4.Imprimir una lista de numeros pares de un intervalo')
    print('5.Imprimir una lista con los numeros impares de un intervalo')
    print('6.Imprimir una lista de los multiplos de un intervalo')
    print('7.Hacer una tabla con dimensiones deseadas')
    opcion= int(input('Introduzcalo que desea hacer'))
    if opcion == 1:
        import clases.matriz
    if opcion ==2:
        import clases.cadena
    if opcion ==3:
        import clases.cuenta_atras_adelante
    if opcion ==4:
        import clases.pares
    if opcion ==5:
        import clases.impares
    if opcion ==6:
        import clases.multiplos
    if opcion ==7:
        import clases.tabla

    