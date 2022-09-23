class Multiplos:
    def __init__ (self,n1,n2,m,x):
        self.n1=n1
        self.n2=n2
        self.m=m
        self.x=x

    def multiplos(self):
        n1= int(input('introduce un numero:'))
        n2= int(input('introduce otro numero:'))
        m = int((input('¿De qué numero quieres los multiplos?')))
        if m <= 0:
            print('¡Los múltiplos deben ser de un numero entero mayor que 0!')
        else:
            if n1 % m !=0:
                x= n1 // m* m + m
            else:
                x= n1
            print(list(range(x,n2 + 1, m)))
    multiplos ('self')

        
