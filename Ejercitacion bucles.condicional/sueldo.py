nombreEmpleado = input("Ingrese su nombre: ")
sueldo = int(input("coloque su sueldo en numero: "))
ambiguedad = int(input("coloque sus años de ambiguedad: "))

if sueldo < 50000 and ambiguedad >= 10:
    sueldoFinal = sueldo * 0.85
    print(nombreEmpleado," ",ambiguedad,"años ",sueldoFinal)
elif sueldo < 50000 and ambiguedad <10:
    sueldoFinal = sueldo * 0.90
    print(nombreEmpleado," ",ambiguedad,"años ",sueldoFinal)
elif sueldo == 50000:
    sueldoFinal = sueldo * 0.95
    print(nombreEmpleado," ",ambiguedad,"años ",sueldoFinal)
elif sueldo == 0:
    print("programa finalizado")
