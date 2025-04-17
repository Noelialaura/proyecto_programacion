import random

equipos = []
jugadores = []

def agregar_equipo(nombre):
    for equipo in equipos:
        if equipo['nombre'].lower() == nombre.lower():
            print("❌ Ese equipo ya está cargado.")
            return
        
    equipo = {
        'nombre': nombre,
        'pj': 0,
        'pg': 0,
        'pe': 0,
        'pp': 0,
        'puntos': 0
    }
    equipos.append(equipo)
    print("✅ Equipo agregado correctamente.")

def agregar_jugador(nombre, apellido):
    jugador = {
        'nombre': nombre,
        'apellido': apellido,
        'goles': 0,
        'asistencias': 0,
        'rojas': 0
    }
    jugadores.append(jugador)

def simular_partidos():
    for equipo in equipos:
        resultado = random.choice(['G', 'E', 'P'])
        equipo['pj'] += 1
        if resultado == 'G':
            equipo['pg'] += 1
            equipo['puntos'] += 3
        elif resultado == 'E':
            equipo['pe'] += 1
            equipo['puntos'] += 1
        elif resultado == 'P':
            equipo['pp'] += 1
            
    for jugador in jugadores:
        goles = random.choices([0, 1, 2, 3], weights=[70, 20, 8, 2])[0]
        asistencias = random.choices([0, 1, 2], weights=[75, 20, 5])[0]

        jugador['goles'] += goles
        jugador['asistencias'] += asistencias        
            
    print("✅ Partidos simulados.\n")

def mostrar_tabla():
    print("\n🏆 Tabla de posiciones:")
    tabla = sorted(equipos, key=lambda x: x['puntos'], reverse=True)
    for e in tabla:
        print(f"{e['nombre']}: {e['puntos']} pts (PJ: {e['pj']}, PG: {e['pg']}, PE: {e['pe']}, PP: {e['pp']})")

def top5_goleadores():
    print("\n⚽ Ranking De Goleadores:")
    if not jugadores:
        print("No hay jugadores cargados.")
        return
    ordenado = sorted(jugadores, key=lambda x: x['goles'], reverse=True)
    for i, j in enumerate(ordenado[:5], start=1):
        print(f"{i}. {j['nombre']} {j['apellido']} - {j['goles']} goles")

def top5_asistencias():
    print("\n🎯 Ranking De Asistentes:")
    if not jugadores:
        print("No hay jugadores cargados.")
        return
    ordenado = sorted(jugadores, key=lambda x: x['asistencias'], reverse=True)
    for i, j in enumerate(ordenado[:5], start=1):
        print(f"{i}. {j['nombre']} {j['apellido']} - {j['asistencias']} asistencias")

def ver_liga_completa():
    print("\n📋 TODOS LOS EQUIPOS:")
    if not equipos:
        print("No hay equipos cargados.")
    else:
        for e in equipos:
            print(f"{e['nombre']} - PJ: {e['pj']}, PG: {e['pg']}, PE: {e['pe']}, PP: {e['pp']}, Puntos: {e['puntos']}")
    
    print("\n👥 TODOS LOS JUGADORES:")
    if not jugadores:
        print("No hay jugadores cargados.")
    else:
        for j in jugadores:
            print(f"{j['nombre']} {j['apellido']} - Goles: {j['goles']}, Asistencias: {j['asistencias']}, Rojas: {j['rojas']}")

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar equipo")
        print("2. Agregar jugador")
        print("3. Simular partidos")
        print("4. Ver tabla de posiciones")
        print("5. Top 5 goleadores")
        print("6. Top 5 asistencias")
        print("7. Ver toda la liga (jugadores y equipos)")
        print("8. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == '1':
            nombre = input("Nombre del equipo: ")
            agregar_equipo(nombre)
        elif opcion == '2':
            nombre = input("Nombre del jugador: ")
            apellido = input("Apellido del jugador: ")
            agregar_jugador(nombre, apellido)
        elif opcion == '3':
            simular_partidos()
        elif opcion == '4':
            mostrar_tabla()
        elif opcion == '5':
            top5_goleadores()
        elif opcion == '6':
            top5_asistencias()
        elif opcion == '7':
            ver_liga_completa()
        elif opcion == '8':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

menu()
        
        