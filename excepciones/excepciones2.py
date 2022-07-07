try:
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    numero3 = numero1/numero2
except ValueError: #aca tiene en cuenta los tipos de datos
    print("Se deben ingresar valores numericos")
except ZeroDivisionError: #aca tiene en cuenta si se divide por 0
    print("No se puede dividir por cero") 
else:
    print("el resultado de la divison es:",numero3)