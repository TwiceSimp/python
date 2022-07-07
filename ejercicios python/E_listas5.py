"""
Ejercicio 5
Pide una cadena por teclado, mete los caracteres en una lista sin espacios
"""
def list_cad(cadena):
    lista_cadena = []
    for i in cadena:
        lista_cadena.append(i)
    return lista_cadena
print(list_cad(cadena = input("Escriba una cadena:")))
