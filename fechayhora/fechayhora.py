#1er paso -> importar libreria

from datetime import datetime, time, date 

#crea una variable llamada hoy -> a la cual le asigna una objeto.metodo()
#datetime.now() -> da la fecha y hora exacta.
hoy = datetime.now()
print(hoy)

ahora = date.today()#esta funcion lo que hace es tomar la fecha de la computadora actual
print(ahora) 

fecha1 = date (2022,6,3)#funcion que permite colocar una fecha en especifico.
print(fecha1)

fecha2 = date (2023,2,7)
print(fecha2)

hora1 = time(14,34)
hora2 = time(23,5,33)

#miniprograma
d = int(input("Ingrese dia: "))
m = int(input("Ingrese mes: "))
a = int(input("Ingrese año: "))
fecha3 = date(a,m,d)
print(fecha3)

h = int(input("Ingrese hora: "))
mi = int(input("Ingrese minutos: "))
hora3 = time(h,mi)
print(hora3)

a1 = fecha3.year #extrae el año nada mas
a1  = fecha3.month #mes
a1  = fecha3.day #dia
#para la hora es lo mismo -> variable.hour/minutes/seconds
print(a1)