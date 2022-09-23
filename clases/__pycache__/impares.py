class Impares:
    def __init__(self,n1,n2,lista):
        self.n1=n1
        self.n2=n2
        self.lista=lista
    def impares(self):
        n1= int(input('introduce un numero'))
        n2= int(input('introduce un numero'))
        lista=[]
        for i in range(n1,n2):
            if i%2 !=0:
                lista.append(i)
        print(lista)
    impares('self')
      





