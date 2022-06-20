#Usando funciones, Simula n intentos de un juego de dados con las siguientes reglas:
#Si sale:
#       6=Gana 100 pesos
#       3=gana 500 pesos
#		1=siga participando
#	    2,4 o 5	  =pierde 200 pesos

from random import randint


def lanzar_dado(lanzamiento):
    cont=0
    for i in range (0,lanzamiento):
        cara=randint(1,6)
        if cara == 6:
            cont+=100
        elif cara == 3:
            cont+= 500
        elif cara == 1:
            cont +=0
        elif cara == 2 or cara == 4 or cara== 5:
            cont-= 200
    return cont

n=int(input("cantidad de lanzamientos"))
pesos=lanzar_dado(n)
print(f"Total pesos: ${pesos}")
