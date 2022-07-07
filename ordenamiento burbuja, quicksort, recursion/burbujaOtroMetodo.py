def ordenamientoBurbuja(lista):
    for k in range (len(lista)-1, 0, -1):#inicio, fin, decremento
        for i in range(k):
            if (lista[i] > lista[i + 1]):
                x = lista [i]
                lista[i] = lista[i + 1]
                lista[i + 1] = x

lista = [1,9,2,3,6,8,4,1,49,30]

ordenamientoBurbuja(lista)
print(lista)
