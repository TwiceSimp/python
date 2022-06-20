#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


CLAVE_GUARDADA = "badboni"
clave = ""

while clave != CLAVE_GUARDADA:
    print("Ingrese su contraseña: ")
    clave = input("- ")

print("Contraseña correcta")