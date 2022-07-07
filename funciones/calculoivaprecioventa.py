def calcularPorcentaje (monto, porc):
    porcentaje = (monto * porc) / 100 #se recomienda esto siempre para que de el resultado corrrecto (no poner el 0.21)
    
    return porcentaje

def calcularPrecioVenta(pc):
    iva = calcularPorcentaje(pc,21)
    ganancia = calcularPorcentaje(pc,120)
    precioVenta = (pc + iva + ganancia)

    return precioVenta, iva, ganancia

precio = float(input("Ingrese un precio: "))
venta = calcularPrecioVenta(precio)
print(venta[1])