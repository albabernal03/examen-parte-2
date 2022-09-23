
cadena=input('introduce una cadena:')
def longitud(cadena):
    if len(cadena)>3 and len(cadena)<10:
        print(cadena)
    else:
        print('no ha cumplido los requisitos')
        
longitud(cadena)