#Escriba un algoritmo que sume los números ingresados por el usuario 
#y cuando la suma sea superior a 100 deje de pedir números y muestre el total.

suma=0
while suma<100:
    num=int(input("digite un numero"))
    suma = suma + num
print(f"la suma es {suma}")