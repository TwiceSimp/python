#Desarrolla una función que permita emular el lanzamiento de dos dados.
#y muestre la cantidad de veces que los dados tuvieron el mismo resultado.


print("---------GRACIANY---------")
from random import randint
def lanzar_dado(lanzamientos):
    contc=0
    for i in range (0,lanzamientos):
        cara1=randint(1,6)
        cara2=randint(1,6)
        print(cara1)
        print(cara2)
        if cara1 == cara2:
            contc+=1
    return contc

n=int(input("cantidad de lanzamientos:"))
contador_iguales=lanzar_dado(n)
print(f"la cantidad de veces que salio igual es {contador_iguales}")

print("---------EDI---------")
from random import randint

def lanzar_dado(lanzamiento):
    contc = 0
    for i in range (0,lanzamiento):
        cara1=randint(1,6)
        cara2=randint(1,6)
        if cara1 == cara2:
            contc+=1
    return contc

n=int(input("cantidad de lanzamientos"))
caras_iguales=lanzar_dado(n)
print(f"las veces iguales fueron{caras_iguales}")