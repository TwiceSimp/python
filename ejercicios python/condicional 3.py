#Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
#Si el divisor es cero el programa debe mostrar un error.

n1=int(input("digite numero"))
n2=int(input("digite numero"))
if n2==0:
    print("error")
else:
    division = n1 / n2
    print(division)

   