from turtle import pos


email = input("Ingrese su correo electronico: ")
posicionArroba = email.find("@")
print(str(email[0:posicionArroba])+"@miempresa.com.ar")