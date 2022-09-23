class Tabla:
    def __init__(self,filas,columnas):
        self.filas=filas
        self.columnas=columnas
    def constructor(self):
        filas= int(input('Introduce el numero de filas que desea que tenga su tabla:'))
        columnas= int(input('Introcuce el numero de columnas que desea que tenga su tabla:'))
        if filas<1 or filas>9 or columnas< 1 or columnas>9:
            print('Las dimensiones introducidas no son correctas, deben estar establecidas en un rago entre (1,9)')
        else:
            for i in range (filas):
                print('')
                for j in range(columnas):
                    print('*',end='')
    constructor('self')
