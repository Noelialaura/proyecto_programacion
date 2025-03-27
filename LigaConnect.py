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

def abrir_menu():
    while True:
        mostrar_menu()
        eleccion_menu = int(input("Ingrese una de las opciones: "))
        if eleccion_menu == 1:
            nombre = input("Ingrese el nombre del jugador: ")
            apellido = input("Ingrese el apellido del jugador: ")
            edad = int(input("Ingrese la edad del jugador: "))
            partidos_jugados = int(input("Ingrese los partidos jugados por el jugador: "))
            goles_totales = int(input("Ingrese los goles totales del jugador: "))
            asistencias = int(input("Ingrese las asistencias del jugador: "))
            tarjeta_amarilla = int(input("Ingrese las tarjetas amarillas del jugador: "))
            tarjeta_roja = int(input("Ingrese las tarjetas rojas del jugador: "))
            agregar_jugador(jugadores, nombre, apellido, edad, partidos_jugados, goles_totales, asistencias, tarjeta_amarilla, tarjeta_roja)
        elif eleccion_menu == 2:
            nombre = input("Ingrese el nombre del equipo: ")
            pais = input("Ingrese el país del equipo: ")
            perdidas = int(input("Ingrese las perdidas del equipo: "))
            ganadas = int(input("Ingrese las ganadas del equipo: "))
            empatadas = int(input("Ingrese las empatadas del equipo: "))
            goles_favor = int(input("Ingrese los goles a favor del equipo: "))
            goles_contra = int(input("Ingrese los goles en contra del equipo: "))
            agregar_equipo(equipos, nombre, pais, perdidas, ganadas, empatadas, goles_favor, goles_contra)
        elif eleccion_menu == 3:
            estadio = input("Ingrese el estadio: ")
            capacidad_total = int(input("Ingrese la capacidad total del estadio: "))
            entradas_disponibles = int(input("Ingrese las entradas disponibles: "))
            equipo_local = input("Ingrese el equipo local: ")
            equipo_visitante = input("Ingrese el equipo visitante: ")
            goles_local = int(input("Ingrese los goles del equipo local: "))
            goles_visitante = int(input("Ingrese los goles del equipo visitante: "))
            fecha = input("Ingrese la fecha del partido: ")
            agregar_partido(partidos, estadio, capacidad_total, entradas_disponibles, equipo_local, equipo_visitante, goles_local, goles_visitante, fecha)
        elif eleccion_menu == 4:
            ver_jugadores(jugadores)
        elif eleccion_menu == 5:
            print(equipos)
        elif eleccion_menu == 6:
            print(partidos)
        elif eleccion_menu == 7:
            break
        else:
            print("Opción no válida, intente de nuevo.")


def contar_puntos(equipos):
    for equipo in equipos:
        puntos = (equipo['ganadas'] * 3) + (equipo['empatadas'] * 1)
        print(f"El equipo {equipo['nombre']} tiene {puntos} puntos.")
        
        
def buscar_jugador_por_nombre(jugadores, nombre_buscado):
    for jugador in jugadores:
        if jugador['nombre'].lower() == nombre_buscado.lower():
            return jugador
    return None      


def buscar_jugador_por_apellido(jugadores, apellido_buscado):
    for jugador in jugadores:
        if jugador['apellido'].lower() == apellido_buscado.lower():
            return jugador
    return None

def top_5_goleadores (jugadores):
    goleador1=0
    goleador2=0
    goleador3=0
    goleador4=0
    goleador5=0
    for jugador in jugadores:
        if jugador['goles_totales'] > goleador1:
            goleador1 = jugador['goles_totales']
        elif jugador['goles_totales'] > goleador2:
            goleador2 = jugador['goles_totales']
        elif jugador['goles_totales'] > goleador3:
            goleador3 = jugador['goles_totales']
        elif jugador['goles_totales'] > goleador4:
            goleador4 = jugador['goles_totales']
        elif jugador['goles_totales'] > goleador5:
            goleador5 = jugador['goles_totales']
            return goleador1, goleador2, goleador3, goleador4, goleador5
        
        