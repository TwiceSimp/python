import statistics

notas = [5.5, 4.7, 6.8, 6.5, 4.8]

promedio = statistics.mean(notas)
print(notas)
print(" el promedio es: ", promedio)
print(max(notas))
print(min(notas))

print("--------------------------------")

lista_notas = [6.7,7,4.5,6.3,2]
print(lista_notas)
#Imprimir cada elemento
for cadanota in lista_notas:
    print(cadanota)

#imprimir cada elemento recorriendo los indices
for indice in range(len(lista_notas)):
    print(lista_notas(indice))

