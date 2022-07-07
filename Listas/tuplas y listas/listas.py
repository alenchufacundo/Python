variada=[6,"hola","Z",1,19.90,"chau"] #creamos una lista de tipo variada
print(variada)
notas=[9.0,3.50,7.0,4.0,8.30,9.0,10.0,4.0]#creamos una lista de notas flotantes
print(notas)
notas.append(0) #agrega la nota 0 al final de la lista
print(notas)
notas.insert(0,5) #agrega la nota 5 en la posicion 0
print(notas)
x=len(notas)
print("la lista  tiene",x, " notas")
notas.remove(4)# elimina la primer aparicion de un  elemento de la lista que exista
print(notas)
notas.pop()#la funcion pop sin parametro elimina el ultimo elemento de la lista
print(notas)
notas.pop(2)#elimina el elemento de la posicion 2 de la lista
print(notas)
notas.sort() #ordena  la lista de menor a mayor
print(notas)
x=len(notas)
print("la lista  tiene",x, " notas")
z=notas.index(10)#devuelve la posicion de un elemento dado
print("el 10 esta en posicion",z+1)
y=notas.count(6) #devuelve la cantidad de apariciones de un elemento
print(y)
print("la primer nota de la lista es ",notas[0]) #muestra el primer valor de la lista
r=notas[3]
print("la cuarta nota de la lista es ",r) #muestra el cuarto elem de la lista
notas[1]=7.6 #modifica el contenido de un elemento de la lista
print(notas)