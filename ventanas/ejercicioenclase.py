from tkinter import Tk, messagebox, simpledialog
import math

window = Tk()
window.withdraw

def volverEjecutar():
    return messagebox.askyesno(title="Pregunta",message="Desea volver a calcular?")

def comprobarNumeroNegativo(numero):
    if numero < 0:
        messagebox.showerror(title="Error",message="Ingresaste un numero negativo")
        return False
    else:
        return True

def comprobarNumero (numero):
    if (numero == None):
        messagebox.showerror(title="Error",message="No ingreso ningun numero")
        return False
    else:
        return True  

def pedirDatos ():
    validacion = True
    while validacion == True:
        precio = simpledialog.askfloat(title="Datos",prompt="Ingrese el precio por m2: ")
        if (comprobarNumero(precio)) and (comprobarNumeroNegativo(precio)):            
            largo = simpledialog.askfloat(title="Largo",prompt="Ingrese la altura del objeto: ")
            if(comprobarNumero(largo)) and (comprobarNumeroNegativo(largo)):
                ancho = simpledialog.askfloat(title="Ancho", prompt="Ingrese el ancho del objeto")
                if(comprobarNumero(ancho)) and (comprobarNumeroNegativo(ancho)):
                    cubierto = simpledialog.askfloat(title="Datos",prompt="Cuanto metros cubre cada caja?: ")
                    if(comprobarNumero(cubierto)) and (comprobarNumeroNegativo(cubierto)):
                        return precio, largo, ancho, cubierto

def calcularCajas (superficie,cubierto):
    cajas = superficie / cubierto
    cajas = math.floor(cajas)
    return cajas

def calcularArea(altura, base):
    area = base * altura
    return area

def calcularPrecio(superficie,precio,cajas):
    total = precio * superficie * cajas
    return total

def mostrarDatos(dato):
    msg = "el precio es de: " + str(dato)
    messagebox.showinfo(title="Informacion",message=msg)

#programa
validacion = True
while validacion == True:
    datos = pedirDatos()
    area = calcularArea(datos[1],datos[2])
    cajas = calcularCajas(area,datos[3])
    respuesta = calcularPrecio(area, datos[0],cajas)
    mostrarDatos(respuesta)
    validacion = volverEjecutar()
