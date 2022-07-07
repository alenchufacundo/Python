#funcion para validad errores por ejemplo input si es un string pero pide un integer
#CODIGO ASCII (VER)
def esDigito (letra):
    if(letra >= '0') and (letra <= '9'): #IMPORTANTE COMILLAS SIMPLES, NO PONER DOBLES, YAQUE SI NO COMPARA CON UN CHAR(CADENA DE TEXTO)
        return True
    else:
        return False

x = 'A'
numero = esDigito(x)
if (numero == True):
    numero = int(x)