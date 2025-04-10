import random

# Generar valores aleatorios para indicar la edad, cant de tarjetas rojas, asistencias y goles de los jugadores argentinos
jugadores = [
    {"nombre": "Lionel Messi", "edad": random.randint(30,35), "tarjetas_rojas": random.randint(0, 5), "asistencias": random.randint(10, 30), "goles": random.randint(5, 50)},
    {"nombre": "Lautaro Martinez", "edad": random.randint(30, 35), "tarjetas_rojas": random.randint(0, 5), "asistencias": random.randint(10, 30), "goles": random.randint(5, 50)},
    {"nombre": "Nahuel Molina", "edad": random.randint(30, 35), "tarjetas_rojas": random.randint(0, 5), "asistencias": random.randint(10, 30), "goles": random.randint(5, 50)},
    {"nombre": "Rodrigo De Paul", "edad": random.randint(30, 35), "tarjetas_rojas": random.randint(0, 5), "asistencias": random.randint(10, 30), "goles": random.randint(5, 50)},
    {"nombre": "Emiliano Martinez", "edad": random.randint(30, 35), "tarjetas_rojas": random.randint(0, 5), "asistencias": random.randint(10, 30), "goles": random.randint(5, 50)},
]

# Mostrar los valores generados
jugadores_Argentinos = [
    f"Nombre: {jugador['nombre']}, Edad: {jugador['edad']}, Tarjetas Rojas: {jugador['tarjetas_rojas']}, Asistencias: {jugador['asistencias']}, Goles: {jugador['goles']}"
    for jugador in jugadores
]

for jugador in jugadores_Argentinos:
    print(jugador)
