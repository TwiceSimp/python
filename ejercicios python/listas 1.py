lista_notas = [6.7,7,4.5,6.3,2]
print(lista_notas)
#Imprimir cada elemento
for cadanota in lista_notas:
    print(cadanota)
print()
#para imprimir cada elemento v2
for indice in range(len(lista_notas)):
    print(lista_notas[indice])
#para sacar el promedio de notas
suma=0
for cadanota in lista_notas:
    suma+=cadanota
prom=suma/lista_notas.__len__()
print("el promedio es: ", prom)

#para la nota mayor
mayor =0
for cadanota in lista_notas:
    if cadanota > mayor:
        mayor=cadanota
print("la nota mayor es: ",mayor)

#para encontrar la nota menor

menor=8
for cadanota in lista_notas:
    if cadanota<menor:
        menor=cadanota
print(menor)

#determinar cuantas notas sobre el promedio

cont=0
for cadanota in lista_notas:
    if cadanota >prom:
        cont+=1
print("notas sobre el promedio del curso: ",cont)



