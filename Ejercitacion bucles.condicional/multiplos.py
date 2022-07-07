def es_multiplo(numero, multiplo):
    if numero % multiplo == 0:
        return True
    else:
        return False

if es_multiplo(15, 3):
    print("Sí es múltiplo")
else:
    print("No es múltiplo")

def imprimir_submultiplos(numero):
    for i in range(1, numero+1):
        if es_multiplo(numero, i):
            print(f"{i},", end="")