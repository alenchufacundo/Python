from datetime import date, datetime, time, timedelta

#pide los datos
fecha1 = input("Ingrese una fecha: ")
fecha2 = input("Ingrese una fecha: ")

#intenta convertir los input.
try:
    fecha1form = datetime.strptime(fecha1,"%d/%m/%Y")
    fecha2form = datetime.strptime(fecha2,"%d/%m/%Y")
except:
    print("ERROR: Fechas ingresadas incorrectas")
else:
    #primero hacer la resta de las fechas formateadas
    resultado = fecha1form - fecha2form #->esta da como resultado un timedelta
    #en resultado tengo un timedelta y solo se le puede aplicar al timedelta la propiedad days.
    resultadodias = abs(resultado.days)#funcion abs para obtenes el valor absoluto(siempre positivo)
    print(resultadodias,"dias")