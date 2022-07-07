import random
numeroSecreto = random.randint(0,100)
print("Debes acertar el numero secreto para ganar")

contador = 0
while (contador == 0):
    numeroIngresado = int(input("Ingrese un numero entre 0-100: "))
    if(numeroIngresado == numeroSecreto):
        print("Usted es un ganador")
        repetirJuego = (input("Desea volver a jugar? yes/no: "))
        if(repetirJuego == "yes"):
            continue
        else:
            contador +=1 #tambien se puede poner un break para cortar el codigo
            print("Fin del juego") 
    elif(numeroIngresado > numeroSecreto):
        print("Estuvo cerca, el numero secreto es menor")
        print(" ")
        continue
    elif(numeroIngresado < numeroSecreto):
        print("Estuvo cerca, el numero secreto es mayor")
        print(" ")
        continue
