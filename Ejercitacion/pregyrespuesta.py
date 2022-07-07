from pickle import TRUE


preguntas = ["Cual es la capital de Argentina?",
            "Cuantos huesos tiene el cuerpo humano?",
            "En que continente se encuentra Egipto?",
            "Cual es el presidente de Uruguay?",
            "Cuantos mundiales gano Brasil?"]

opcion1 = ["New York","206","Africa","Vladimir Putin","2"]
opcion2 = ["Buenos Aires","147","Asia","Alberto Fernandez","5"]
opcion3 = ["Santiago de Chile","328","America","Lacalle Pou","0"]
respuesta = [2,1,1,3,2]

def respuestaCorrecta(resp,numeroPreg):
    correcta = respuesta[numeroPreg]
    if (correcta == resp):
        return True
    else:
        return False

def mostrarPregunta(numeroPreg):
    print(preguntas[numeroPreg])
    print("1-",opcion1[numeroPreg])
    print("2-",opcion2[numeroPreg])
    print("3-",opcion3[numeroPreg])
    opcionSeleccionada = int(input("Ingrese una opcion correcta (1, 2 o 3): "))

    return opcionSeleccionada

contador = 0
respuestasCorrectas = 0
respuestasIncorrectas = 0
while contador < len(preguntas):
    x = mostrarPregunta(contador)
    v = respuestaCorrecta(x,contador)
    if (v == True):
        print("Usted contesto bien")
        respuestasCorrectas += 1 
    else:
        print("Usted contesto mal")
        respuestasIncorrectas += 1
    contador += 1
    print("-------------------------------")
    print("-------------------------------")

print("FIN DEL JUEGO")
print("Usted ha obtenido un total de",respuestasCorrectas,"respuestas correctas y",respuestasIncorrectas,"respuestas incorrectas.")