class Cadena():
    def __init__(self,cadena):
        self.cadena=cadena
    def longitud(self):
        cadena= input('introduce una cadena de palabras >3 y <10:')
        if len(cadena)>3 and len(cadena)<10:
            print(cadena)
        else:
            print('no ha cumplido los requisitos')
    longitud('cadena')



