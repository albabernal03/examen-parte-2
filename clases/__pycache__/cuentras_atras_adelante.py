class Numeros:
    def __init__(self,n1,n2, lista):
        self.n1=n1
        self.n2=n2
        self.lista=lista
    def para_atras(self):
        lista=[]
        n1= int(input('introduce un numero'))
        n2= int(input('introduce un numero'))
        for i in range(n1,n2):
            lista.append(i)
        print(lista)
    para_atras('lista')


        


        

