from datetime import date, datetime, time, timedelta

fechanacstr = input("Ingrese su fecha de nac en formato string.imiento: ") #pide fecha
fechanac = datetime.strptime(fechanacstr,"%d/%m/%Y") #conveirte la fecha de string a datos
dia = fechanac.day #extrae dia de la fecha de nacimiento
mes = fechanac.month #extrae mes de la fecha de nacimiento

if (mes < 6) or (mes == 6 and dia < 23):
    anio = 2023
else:
    anio = 2022

fechaprox = datetime(anio,mes,dia)
#fechaproxstr = input("Ingrese la fecha de su proximo cumpleaños: ")
#fechaprox = datetime.strptime(fechaproxstr,"%d/%m/%Y")
fechahoy = datetime.now() #toma fecha actual
print(fechahoy)

pasaron = fechahoy - fechanac #resto fecha de hoy menos la fecha de nacimiento # LA DIFERENCIA DE FECHAS SIEMPRE DEVUELVE DIAS.
print(pasaron) #esto irmpime la diferencia en DIAS
pasarondias = pasaron.days #metodo para mostrar dias nada mas. ESTE ES EL UNICO METODO QUE HAY PARA EXTRAER LOS DIAS.
print(pasarondias)
aniosvividos = int(pasarondias/365) #UTILIZA LOS DIAS Y LOS DIVIDE EN 365 PARA QUE DE EN AÑOS Y LO PONE QUE SEA EN ENTERO ASI ES EXACTO Y NO ES CON DECIMAL.
print("tenes",aniosvividos,"años")

#----------------------------------------------------------------
faltanTiempo = fechaprox - fechahoy
faltanDias = faltanTiempo.days
print(faltanTiempo)
print("te falta cumplir",faltanDias,"dias")
