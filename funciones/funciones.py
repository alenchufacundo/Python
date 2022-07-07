def calcularIva(p):
    i = p * 0.21
    return i

#variables p e i no se correlacionan entre ellas en cada funcion, el ambito es local. no se relacionan
def mostrarDatos(p,i,g):
    print("El precio del producto es",p)
    print("El iva del producto es de",i)
    print("El porcentaje de ganancia es de",g,"%")

def calcularPorcentaje(pre,porc):
    porcentaje = pre * porc/100
    return porcentaje

pre = float(input("Ingrese precio: ")) 
iva = calcularIva(pre)
ganancias = calcularPorcentaje(pre,120)
mostrarDatos(pre,iva,ganancias)
