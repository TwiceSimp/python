"""
2.-pide un numero por teclado y guarda en una lista su tabla de multiplicar
hasta el 10.Por ejemplo si pide el 5 la lista tendra:5,10,15,20,30,35,40,45,50
"""
numero = int(input("Digite numero:"))
tabla = []
for i in range(1,11):
    multiplicacion = i * numero
    tabla.append(multiplicacion)
    multiplicacion = 0

print(tabla)