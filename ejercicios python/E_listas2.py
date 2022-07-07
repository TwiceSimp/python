"""
Ejercicio 2
Escribe un programa en Python que tome una lista de números ingresados en forma aleatoria y elimine el primer
y último elemento de la lista y cree una nueva lista con los elementos que no fueron eliminados.
Luego, implementa lo necesario para que tome la lista y devuelva una nueva lista que contenga todos
los elementos de la lista anterior menos el primero y el último
"""
lista_original = []

def eliminar(lista):
    lista.pop(0)
    lista.pop()
    return print("Lista nueva:",lista)

print("Ingrese 5 numeros")
for i in range(5):
    num = input("Ingres un numero:")
    lista_original.append(num)

print("Lista original:",lista_original)
eliminar(lista_original)