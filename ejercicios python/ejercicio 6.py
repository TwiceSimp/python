#Escriba un algoritmo que sume los números ingresados por el usuario hasta que el usuario 
#ingrese el número 0 (detener las preguntas ante este escenario).

num=int(input("digite un numero"))
suma = 0

while num !=0:
    suma = num+suma
    num=int(input("ingrese un numero"))
print(f"la suma es {suma}")