voltajes = []
for x in range(3):
    new_voltaje = float(input(f"Ingrese voltaje {x+1}: "))
    voltajes.append(new_voltaje)
promedio = sum(voltajes)/3

if promedio<115: print("VOLTAJE CORRECTO")
elif 115<promedio and 220>promedio: print("ALTO VOLTAJE")
else: print("PELIGRO")