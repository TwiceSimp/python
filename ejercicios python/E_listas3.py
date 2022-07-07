"""
Ejercicio 3
Escribe un programa que tome una lista con 25 datos ingresados en forma aleatoria y muestre “Verdadero”
si tiene algún elemento duplicado. No se debe modificar el contenido de la lista.

"""
lista = []
def duplicado(valor):
    if valor in lista:
        return print("Verdadero,elemento duplicado")

for i in range(24):
    valor = input("Ingrese un valor:")
    duplicado(valor)
    lista.append(valor)

print("Ya almaceno todos los valores")