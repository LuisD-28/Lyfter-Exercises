secodns = 0
minutes = 0
time_Calculated = 0
tenMinutes = 10 * 60
seconds_left = 0

secodns = int(input("Ingrese el tiempo en segundos a calcular: "))

minutes = secodns // 60

if minutes < 10:
    seconds_left = tenMinutes - secodns
    time_Calculated = f"Faltan {seconds_left} segundos para llegar a los 10 minutos"
else:
    if minutes == 10:
        time_Calculated = "El tiempo ingresado es exactamente 10 minutos"
    else:
        time_Calculated = "El tiempo ingresado es mayor a 10 minutos"

print(time_Calculated)