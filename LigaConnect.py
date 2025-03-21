equipos = []
jugadores = []
partidos = []

def agregar_jugador(jugadores, nombre, apellido, edad, partidos_jugados, goles_totales, asistencias, tarjeta_amarilla, tarjeta_roja):
    jugador = {
        'nombre': nombre,
        'apellido': apellido,
        "edad": 0,
        "partidos_jugados": 0,
        'goles_totales': 0,
        'asistencias': 0,
        "tarjeta_amarilla": 0,
        "tarjeta_roja": 0
    }
    jugadores.append(jugador)
    return jugadores

def agregar_equipo(equipos, nombre, pais, perdidas, ganadas, empatadas, goles_favor, goles_contra):
    equipo = {
        'nombre': nombre,
        'pais': pais,
        'perdidas': 0,
        'ganadas': 0,
        'empatadas': 0,
        'goles_favor': 0,
        'goles_contra': 0
    }
    equipos.append(nombre)
    return equipos

def agregar_partido(partidos, estadio, capacidad_total, entradas_disponibles, equipo_local, equipo_visitante, goles_local, goles_visitante, fecha):
    partido = {
        "estadio": estadio,
        "capacidad_total": 0,
        "entradas_disponibles": 0,
        'equipo_local': equipo_local,
        'equipo_visitante': equipo_visitante,
        'goles_local': goles_local,
        'goles_visitante': goles_visitante,
        'fecha': fecha
    }
    partidos.append(partido)
    return partidos

def ver_jugadores(jugadores):
    for jugador in jugadores:
        print(f"Nombre: {jugador['nombre']}")
        print(f"Apellido: {jugador['apellido']}")
        print(f"Edad: {jugador['edad']}")
        print(f"Partidos jugados: {jugador['partidos_jugados']}")
        print(f"Goles totales: {jugador['goles_totales']}")
        print(f"Asistencias: {jugador['asistencias']}")
        print(f"Tarjetas amarillas: {jugador['tarjeta_amarilla']}")
        print(f"Tarjetas rojas: {jugador['tarjeta_roja']}")
        print("")

def mostrar_menu():
    print("1. Agregar jugador")
    print("2. Agregar equipo")
    print("3. Agregar partido")
    print("4. Ver jugadores")
    print("5. Ver equipos")
    print("6. Ver partidos")
    print("7. Salir")


probando


