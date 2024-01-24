base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
area = (base*altura)/2

if area>1000:
    print("DATOS NO VALIDOS...")
else: print(F"El area es {round(area,2)}")