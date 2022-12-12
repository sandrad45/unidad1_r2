'''
Nombre: Sandra Dania Gonzalez Manzano
Fecha: 20 / sep / 2022
Descripción:  EL programa arroja horas, minutos y la duración de eventos 
'''
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
print("Hora: ", hour, mins, "Duarara: ", dura)
hour_eve = (hour % 26)+ 1
min_eve= mins % 60
print("Horas res: ", hour_eve)
print("Minutos res: ", min_eve)