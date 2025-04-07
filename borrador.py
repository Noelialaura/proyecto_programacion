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
            
def generar_asistentes():
    """Genera la lista de máximos asistentes si hay partidos jugados."""
    if partidos_jugados() == 0:
        print("\n❌ No hay partidos jugados, por lo que no hay asistencias.")
        return []

    mediocampistas = [
        ("Enzo Fernández", random.randint(0, 10)),
        ("Rodrigo De Paul", random.randint(0, 10)),
        ("Valverde", random.randint(0, 10)),
        ("James Rodríguez", random.randint(0, 10)),
        ("Lo Celso", random.randint(0, 10))
    ]

    return sorted(mediocampistas, key=lambda x: x[1], reverse=True)

def mostrar_asistentes():
    """Muestra la tabla de asistentes."""
    asistentes = generar_asistentes()
    if asistentes:
        print("\n🎯 Ranking de Asistentes:")
        for i, (jugador, asistencias) in enumerate(asistentes, start=1):
            print(f"{i}. {jugador} - {asistencias} asistencias")

def generar_rojas():
    """Genera la lista de defensores con más tarjetas rojas de forma coherente."""
    total_partidos = partidos_jugados()
    if total_partidos == 0:
        print("\n❌ No hay partidos jugados, por lo que no hay tarjetas rojas.")
        return []

    # Máximo realista de tarjetas rojas por jugador: 20% del total de partidos
    max_rojas = max(1, total_partidos // 5)

    defensores = [
        ("Otamendi", random.randint(0, max_rojas)),
        ("Gary Medel", random.randint(0, max_rojas)),
        ("Ronald Araujo", random.randint(0, max_rojas)),
        ("Davinson Sánchez", random.randint(0, max_rojas)),
        ("Carlos Zambrano", random.randint(0, max_rojas))
    ]

    return sorted(defensores, key=lambda x: x[1], reverse=True)

def mostrar_rojas():
    """Muestra la tabla de defensores con más tarjetas rojas."""
    rojas = generar_rojas()
    if rojas:
        print("\n🟥 Defensores con más Tarjetas Rojas:")
        for i, (jugador, tarjetas) in enumerate(rojas, start=1):
            print(f"{i}. {jugador} - {tarjetas} rojas")

# Ejemplo de uso
agregar_equipo("Argentina")
agregar_equipo("Brasil")
agregar_equipo("Colombia")
agregar_equipo("Uruguay")
agregar_equipo("Venezuela")
agregar_equipo("Peru")
agregar_equipo("Chile")
agregar_equipo("Ecuador")
agregar_equipo("Paraguay")
agregar_equipo("Mexico")

registrar_partido("Argentina", 'G')
registrar_partido("Brasil", 'P')
registrar_partido("Argentina", 'E')
registrar_partido("Brasil", 'E')
registrar_partido("Colombia", 'G')
registrar_partido("Uruguay",'P')
registrar_partido("Argentina","P")
registrar_partido("Venezuela","E")

#Mostrar tabla de la liga
mostrar_tabla()

# Mostrar la tabla de goleadores
mostrar_goleadores()

#Mostrar la tabla de asistidores
mostrar_asistentes()

#Mostrar la tabla de tarjetas rojas
mostrar_rojas()

