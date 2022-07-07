#from random import randint
#para importar librerias-> de la libreria random, importar randint(funcion)->esta importa una funcion en especifica
#numero = randint(0,100) -> randint(incio,fin)->genera un numero aleatorio.
#print(numero

import random #importa toda la libreria entera.
numeros = []

numero = random.randint(0, 20)#->aca es necesario poner la libreria.funcion()-> random.randint()

for i in range (0,numero,+1):
    numeroAleatorio = random.randint(0,99)
    numeros.append(numeroAleatorio)
print(numeros)

cantidadNumeros = len(numeros)
print ("La lista tiene", cantidadNumeros,"numeros")

#defino una variable contador
i = 0
#recorro el array
for x in range(0, cantidadNumeros,+1):
    if(numeros[x] > 50):
        i += 1
print("La cantidad de numeros mayores a 50 son: ",i)
        