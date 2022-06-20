#Escriba un algoritmo que calcule e imprima la suma de los n primeros números enteros positivos.
#El valor de n debe leerse del teclado y ser ingresado por el usuario.

n=int(input("ingrese un numero"))
suma=0

for i in range(n+1):
    suma = suma + i
print(f"la suma es {suma}")
