palabra = input("ingrese palabra: ")
caracter1 = input("ingrese caracter: ")
caracter2 = input("ingrese caracter: ")


while caracter1 in palabra:
    pos = palabra.find(caracter1)
    print(palabra[0:pos]+caracter2+palabra[pos+1:])
    
