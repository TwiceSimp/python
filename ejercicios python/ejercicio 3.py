#Modifique el algoritmo del problema anterior para que cuente las veces que ha leído un número de teclado y escriba el resultado por pantalla.


num=int(input("digite un numero"))
count=0
while True:
    if num >=0 and num <=20:
        print("valor correcto")
        break
    else:
        print("error,vuelva a digitar")
        num=int(input("ingrese numero"))
        count+=1

print(f"Escribio {count+1} Numeros")

