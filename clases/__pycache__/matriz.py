
#Este problema va de multilistas
# Un poco de teoría sobre el acceso a estas listas: Si deseamos acceder al primer valor de la primera lista, entonces la instrucción sería:
#·valor = lista[0][0]
#Donde lista[0] ser refiere a la primera lista, por lo que lista[0][0] se refiere al primer elemento de la la multilista.


class Comprobacion:
    def __init__(self,n, matriz):
        self.n=n
        self.matriz=matriz
    def comprobacion(self):
        n=int(input('¿Qué fila desea comprobar?'))
        matriz= [[1, 1, 1, 3],[2, 2, 2, 7], [3, 3, 3, 9],[4, 4, 4, 13]]
        if n >=0 <=3:
            if matriz[n][3] == matriz[n][0] + matriz[n][1] + matriz[n][2]:
                print('El resultado es correcto, el cuarto numero es la suma de los tres anteriores')
            else:
                print('No es corrector')
        else:
            print('La fila seleccionada no existe')
    comprobacion('self')



