#diccionarios
facundo = {
    "nombre":"Facundo",
    "apellido":"Rios",
    "edad":25
}

facundo["nombre"] = "Martin"
facundo ["direccion"] = "Calle falsa 123" #->agrega esta llave con su value. NO TIRA ERORR. ESTO SE PUEDE HACER.

print(facundo)

print(facundo.get("telefono","Error, no se encuentra ese dato"))
print(facundo.keys())
print(facundo.values())
mensajeError = "hola jeje"
d = facundo.pop("correo",mensajeError)
print(d)

#recorrer un diccionario
# for key, value in diccionario.items():
#     print(key,value)