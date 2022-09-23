class Pares:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    
    def pares(self):
        n1= int(input('introduce un numero'))
        n2= int(input('introduce un numero'))
        if n1 % 2 !=0:
            print(list(range(n1 + 1, n2 + 1, 2)))
        else:
            print(list(range(n1, n2 + 1, 2)))
    pares('self')


        