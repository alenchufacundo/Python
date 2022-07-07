def calculariva(p):
    i=p*21/100
    return i

def mostrardatos(p,i,g):
    print("El precio del producto es: ", p)
    print("El iva del producto es: ", i)
    print("La ganancia es de: ", g)

def calcularporc(pre,porc):
    porcentaje=pre*porc/100
    return porcentaje

pre=float(input("Ingrese precio"))
iva=calculariva(pre)
print(iva)
gan=calcularporc(pre,120)
mostrardatos(pre,iva,gan)