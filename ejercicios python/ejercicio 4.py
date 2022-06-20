#Modifique el algoritmo del problema anterior para que se realicen 5 lecturas por teclado como máximo.

num=int(input("digite un numero"))
count=0
countn=1
while True and countn < 5:
    countn+=1
    if num >=0 and num <=20:
        print("valor correcto")
        break
    else:
        print("error,vuelva a digitar")
        num=int(input("ingrese numero"))
        count+=1

print(f"Escribio {count+1} Numeros")