tuple_meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
for i in tuple_meses:
    numero = int(input("Elije un numero:"))

    if numero == 0:
        print("Salio del programa")
        break
    else:
        if numero>= 1 and numero<=len(tuple_meses):
            print(tuple_meses[numero-1:])
        else:
            print("Digita un numero entre 1 y ",len(tuple_meses))