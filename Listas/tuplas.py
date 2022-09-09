lista=[]  #creamos lista vacia
lista2=["juan", "marcos","lucas"]#creamos lista con 3 nombres
lista2[1]="Marcelo"
print(lista2)

tupla=("Luis","eva","agustin","carlos")#creamos una tupla de 4 nombres inmodificables
print(tupla)
print(tupla[3])

categorias=("consumidor final", "Responsable inscripto","Exento","Monotributo")
print(categorias)
c=int(input("Seleccione categoria(1-4): "))
print(" la categoria es",categorias[c-1])