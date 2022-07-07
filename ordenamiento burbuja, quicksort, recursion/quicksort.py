lista = [4,3,2,5,10,19,8,7,10,12]

def quickSort(lista):
    if len(lista) < 2: #esta condicion dice que si la longitud del array es menor a 2, es decir = 1, que retorne el array
        return lista

    pivote = lista[-1] #creacion del pivote y se le asigna el ultimo numero
    numerosIguales = [] #crea las listas vacias
    numerosMenores = []
    numerosMayores = []

    for numero in lista: #iteracion
        if numero == pivote: #condiciones.
            numerosIguales.append(numero) #append funcion de agregar.
        elif numero > pivote:
            numerosMayores.append(numero)
        else:
            numerosMenores.append(numero)
    
    return quickSort(numerosMenores) + numerosIguales + quickSort(numerosMayores)
#va llamadno la funcion muchas veces y a su vez va retornadno la funcion pero cuando empiezan a haber pocos elemtnos en la lista, empieza un proceso inverso,
# ya que se esta cumpliendo la condicion de que sea menor a 2 elementos

resultado = quickSort(lista)
print(resultado)