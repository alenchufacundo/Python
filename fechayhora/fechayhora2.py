from datetime import datetime, date, time, timedelta 

f1 = date(2021,5,14)
f2 = datetime.strptime("14/05/2021","%d/%m/%Y") #funcion con 2 parametros("string","formato") -> crea una fecha a partir de un string
print(f2)
fyh = datetime.strptime("06/10/1996 10:15:24","%d/%m/%Y %H:%M:%S")#aca es con hora tambien.
print(fyh)

#creamos input
f = input("Ingrese una fecha: ")
fecha = datetime.strptime(f, "%d/%m/%Y") #aca es lo mismo nada mas que en vez de escribirle un string, se le pone la variable del input.(f)
print(fecha)

fecha2= fecha.strftime("%d/%m/%Y") #formatea el orden de la fecha en el deseado
print(fecha2)

fecha3= fecha.strftime("Hoy es el dia %d del mes %m del año %Y") #formatea el orden de la fecha en el deseado
print(fecha3)

#importar el timedelta nos permite hacer calculos entre fechas

resultado = f2 - fecha
resultado2 = f2 - timedelta(days=90)#especifica que sume 90 dias ->puede ser weeks, months, years
print(resultado2)

print(type(fecha)) #el type nos dice que tipo es esa variable entre ()