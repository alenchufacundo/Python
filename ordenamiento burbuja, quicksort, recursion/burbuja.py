#METODO ordenamiento burbuja en una lista/array hasta 100 elementos

# numeros = [7,6]

# if numeros[0] > numeros[1]:
#     posicion0 = numeros[0]
#     posicion1 = numeros[1]
#     numeros[0] = posicion1
#     numeros[1] = posicion0

numeros = [5,2,1,8,4,0]

def burbuja(lista):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(lista) - 1):
            #print(f"{numeros[i]} > {numeros[i + 1]} = {numeros[i] > numeros[i + 1]}") #interpolacion
            if (numeros[i] > numeros[i + 1]):
                posicion0 = numeros [i]
                posicion1 = numeros [i + 1]
                numeros [i] = posicion1
                numeros [i + 1] = posicion0
                intercambio = True

burbuja(numeros)
print(numeros)