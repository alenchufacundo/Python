#FUNCION EXTRAER CODIGO
def extrarCodigo():
    print("Bienvenido!")
    codigoProducto = input("Ingrese codigo del producto: ")
    letras = codigoProducto[0:2]
    numeros = codigoProducto[2:]
    print(letras)
    print(numeros)

#EJECUCION DEL PROGRAMA    
extrarCodigo ()