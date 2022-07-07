print ("Ingrese numero")
num = int(input())
while num < 0 or num > 999:
    print(".error.")
    num = int(input())
cont = 0 #el cont tiene que ir afuera del while->se inicializa afuera
while num > 0 and num < 999:
    num = num // 10
    cont = cont + 1
print ("digitos",cont,"cifras")

