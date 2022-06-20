#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.


numero = int(input("Por favor ingrese un número entero positivo: "))

for x in range(numero, -1, -1):
    print(x, end=", ")