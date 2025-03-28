"""Matriz Jugador con mas goles""""

matrizEquipos = ['nombre', 'equipo', 'pais', 'perdidas', 'ganadas', 'empatadas', 'goles_favor', 'goles_contra']
matrizJugadores = [['nombre', 'apellido', 'edad', 'partidos_jugados', 'goles_totales', 'asistencias', 'tarjeta_amarilla', 'tarjeta_roja']]
matrizPartidos = [['estadio', 'capacidad_total', 'entradas_disponibles', 'equipo_local', 'equipo_visitante', 'goles_local', 'goles_visitante', 'fecha']]

def agregar_jugadorM(matrizJugadores):
    nombre = input("Ingrese el nombre del jugador: ")
    apellido = input("Ingrese el apellido del jugador: ")
    edad = int(input("Ingrese la edad del jugador: ")) 
    partidos_jugados = int(input("Ingrese los partidos jugados por el jugador: "))
    goles_totales = int(input("Ingrese los goles totales del jugador: "))
    asistencias = int(input("Ingrese las asistencias del jugador: "))
    tarjeta_amarilla = int(input("Ingrese las tarjetas amarillas del jugador: "))
    tarjeta_roja = int(input("Ingrese las tarjetas rojas del jugador: "))
    
    if edad < 18 or partidos_jugados < 0 or goles_totales < 0 or asistencias < 0 or tarjeta_amarilla < 0 or tarjeta_roja < 0:
        print("No puede haber números negativos o edad menor a 18. Intente de nuevo.")
        return agregar_jugadorM(matrizJugadores)
    
    jugador = [nombre, apellido, edad, partidos_jugados, goles_totales, asistencias, tarjeta_amarilla, tarjeta_roja]
    matrizJugadores.append(jugador)
    return matrizJugadores

def agregar_equipoM(matrizEquipos):
    nombre = input("Ingrese el nombre del equipo: ")
    pais = input("Ingrese el país del equipo: ")
    perdidas = int(input("Ingrese las perdidas del equipo: "))
    ganadas = int(input("Ingrese las ganadas del equipo: "))
    empatadas = int(input("Ingrese las empatadas del equipo: "))
    goles_favor = int(input("Ingrese los goles a favor del equipo: "))
    goles_contra = int(input("Ingrese los goles en contra del equipo: "))
    
    if perdidas < 0 or ganadas < 0 or empatadas < 0 or goles_favor < 0 or goles_contra < 0:
        print("No puede haber números negativos. Intente de nuevo.")
        return agregar_equipoM(matrizEquipos)

    equipo = [nombre, pais, perdidas, ganadas, empatadas, goles_favor, goles_contra]
    matrizEquipos.append(equipo)
    return matrizEquipos

def agregar_partidoM(matrizPartidos):
    estadio = input("Ingrese el estadio: ")
    capacidad_total = int(input("Ingrese la capacidad total del estadio: "))
    entradas_disponibles = int(input("Ingrese las entradas disponibles: "))
    equipo_local = input("Ingrese el equipo local: ")
    equipo_visitante = input("Ingrese el equipo visitante: ")
    goles_local = int(input("Ingrese los goles del equipo local: "))
    goles_visitante = int(input("Ingrese los goles del equipo visitante: "))
    fecha = input("Ingrese la fecha del partido: ")
    
    if capacidad_total < 0 or entradas_disponibles < 0 or goles_local < 0 or goles_visitante < 0:
        print("No puede haber números negativos. Intente de nuevo.")
        return agregar_partidoM(matrizPartidos)
    
    partido = [estadio, capacidad_total, entradas_disponibles, equipo_local, equipo_visitante, goles_local, goles_visitante, fecha]
    matrizPartidos.append(partido)
    return matrizPartidos
    
def buscar_jugador_mas_goles(matrizJugadores):
    mayor_goles = 0
    jugador = []
    for i in range(1, len(matrizJugadores)):
        if matrizJugadores[i][4] > mayor_goles:
            mayor_goles = matrizJugadores[i][4]
            jugador = matrizJugadores[i]
    return jugador
    
