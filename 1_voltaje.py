voltajes = []
for x in range(5):
    new_voltaje = float(input(f"Ingrese voltaje {x+1}: "))
    voltajes.append(new_voltaje)
promedio = sum(voltajes)/5

if promedio>220:
    print("ALTO VOLTAJE")
else: print("VOLTAJE CORRECTO")
