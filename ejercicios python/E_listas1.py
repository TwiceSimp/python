"""
Ejercicio 1
Escriba programa en Python que tome una lista de números ingresados aleatoriamente y devuelva la suma acumulada,
es decir, una nueva lista donde el primer elemento es el mismo, el segundo elemento es la suma del primero con el segundo,
el tercer elemento es la suma del resultado anterior con el siguiente elemento y así sucesivamente.
Por ejemplo, la suma acumulada de [1,2,3] es [1, 3, 6].
"""

def lista_original():
    lista_origin = []
    for i in range(5):
        numeros = int(input("Ingrese un numero:"))
        lista_origin.append(numeros)
    return lista_origin


def lista_nueva(lista):

    lista_nuev = []
    suma = 0
    for i in lista:
        suma = suma + i
        lista_nuev.append(suma)
    return lista_nuev
lista=lista_original()
print("Lista original:",lista)
print("Lista nueva:",lista_nueva(lista))