import random

liga = {}

def agregar_equipo(nombre):
    """Agrega un equipo a la liga si no existe."""
    if nombre not in liga:
        liga[nombre] = [0, 0, 0, 0, 0]  # [PJ, PG, PE, PP, Puntos]

def registrar_partido(equipo, resultado):
    """Actualiza las estadísticas de un equipo tras un partido."""
    if equipo in liga:
        liga[equipo][0] += 1  # Partidos jugados
        if resultado == 'G':   # Ganado
            liga[equipo][1] += 1
            liga[equipo][4] += 3
        elif resultado == 'E': # Empate
            liga[equipo][2] += 1
            liga[equipo][4] += 1
        elif resultado == 'P': # Perdido
            liga[equipo][3] += 1

def mostrar_tabla():
    """Muestra la tabla de posiciones ordenada por puntos."""
    print("\n🏆 Tabla de Posiciones:")
    tabla = sorted(liga.items(), key=lambda x: x[1][4], reverse=True)
    for equipo, stats in tabla:
        print(f"{equipo}: {stats[4]} pts (PJ: {stats[0]}, PG: {stats[1]}, PE: {stats[2]}, PP: {stats[3]})")

def partidos_jugados():
    """Devuelve el total de partidos jugados en la liga."""
    return sum(equipo[0] for equipo in liga.values())

def generar_goleadores():
    """Genera la lista de goleadores solo si hay partidos jugados."""
    if partidos_jugados() == 0:
        print("\n❌ No hay partidos jugados, por lo que no hay goles.")
        return []

    # Generamos los jugadores con goles aleatorios
    jugadores = [
        ("Lionel Messi", random.randint(0, 10)),
        ("Julian Alvarez", random.randint(0, 10)),
        ("Neymar", random.randint(0, 10)),
        ("Luis Suarez", random.randint(0, 10)),
        ("Borja", random.randint(0, 10))
    ]

    # Ordenamos la lista por goles (de mayor a menor)
    return sorted(jugadores, key=lambda x: x[1], reverse=True)

def mostrar_goleadores():
    """Muestra la tabla de goleadores."""
    goleadores = generar_goleadores()
    if goleadores:
        print("\n⚽ Ranking de Goleadores:")
        for i, (jugador, goles) in enumerate(goleadores, start=1):
            print(f"{i}. {jugador} - {goles} goles")

# Ejemplo de uso
agregar_equipo("Argentina")
agregar_equipo("Brasil")
agregar_equipo("Colombia")
agregar_equipo("Uruguay")

registrar_partido("Argentina", 'G')
registrar_partido("Brasil", 'P')
registrar_partido("Argentina", 'E')
registrar_partido("Brasil", 'E')
registrar_partido("Colombia", 'G')
registrar_partido("Uruguay",'P')

#Mostrar tabla de la liga
mostrar_tabla()

# Mostrar la tabla de goleadores
mostrar_goleadores()