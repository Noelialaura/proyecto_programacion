import random
import json
from datetime import datetime
import time
import sys

equipos = []
jugadores = []
estadios = {
    "Estadio Monumental": 80000,
    "La Bombonera": 54000,
    "Estadio Único": 53000,
    "Cilindro de Avellaneda": 51000,
    "Nuevo Gasómetro": 47000
}
def agregar_equipo(nombre):
    
    for equipo in equipos:
        if equipo['nombre'].lower() == nombre.lower():
            print("❌ Ese equipo ya está cargado.")
            return
        
    try:
        while int(nombre):
            print("ERROR, solo se aceptan caracteres, NO NUMEROS")
            nombre = input("ingrese otro nombre: ")
    except ValueError:
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
    try:
        while int(nombre):
            print("ERROR, INGRESE UN NOMBRE")
            nombre = input("ingrese un nombre: ")
    except ValueError:
        jugador = {
        'nombre': nombre,
        }
    try:
         while int(apellido):
            print("ERROR, INGRESE UN APELLIDO")
            apellido = input("ingrese un apellido: ")
    except ValueError:
        jugador = {
        'apellido': apellido,
        'goles': 0,
        'asistencias': 0,
        'rojas': 0
    }
    jugadores.append(jugador)
    print("✅ Jugador agregado correctamente.")

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
        rojas = random.choices([0, 1], weights=[99, 1])[0]

        jugador['goles'] += goles
        jugador['asistencias'] += asistencias     
        jugador['rojas'] += rojas   
            
    print("✅ Partidos simulados.\n")

def mostrar_tabla():
    print("\n🏆 Tabla de posiciones:")
    tabla = sorted(equipos, key=lambda x: x['puntos'], reverse=True)
    for e in tabla:
        print(f"{e['nombre']}: {e['puntos']} pts (PJ: {e['pj']}, PG: {e['pg']}, PE: {e['pe']}, PP: {e['pp']})")

def mostrar_top5_consola(clave, titulo, emoji, unidad):
    print(f"\n{emoji} Ranking De {titulo}:")
    if not jugadores:
        print("No hay jugadores cargados.")
        return
    ordenado = sorted(jugadores, key=lambda x: x.get(clave, 0), reverse=True)
    for i, j in enumerate(ordenado[:5], start=1):
        print(f"{i}. {j['nombre']} {j['apellido']} - {j.get(clave, 0)} {unidad}")

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

def comprar_entrada(nombre_cliente):
    try:
        while int(nombre_cliente):
            print("ERROR, ingrese un nombre")
            nombre_cliente= input("Nombre del cliente: ")
    except ValueError:
        print("\nEstadios disponibles:")
    for estadio in estadios:
        print(f"- {estadio} (Capacidad disponible: {estadios[estadio]})")

    estadio_input = input("Estadio del partido: ")
    estadios_lower = {e.lower(): e for e in estadios}

    if estadio_input.lower() not in estadios_lower:
        print("❌ Estadio no válido.")
        return

    estadio = estadios_lower[estadio_input.lower()]

    if estadios[estadio] <= 0:
        print("❌ No hay capacidad disponible en este estadio.")
        return

    fecha = input("Fecha del partido (formato YYYY-MM-DD): ")
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        print("❌ Fecha no válida. Use el formato YYYY-MM-DD.")
        return

    precio = input("Precio de la entrada: ")
    if not precio.isdigit():
        print("❌ El precio debe ser numérico.")
        return

    entrada = {
        "cliente": nombre_cliente,
        "estadio": estadio,
        "fecha": fecha,
        "precio": precio
    }

    try:
        with open("entradas.json", "r") as file:
            entradas = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        entradas = []

    entradas.append(entrada)
    estadios[estadio] -= 1

    with open("entradas.json", "w") as file:
        json.dump(entradas, file, indent=4)

    print("✅ Entrada registrada correctamente.")

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar equipo")
        print("2. Agregar jugador")
        print("3. Simular partidos")
        print("4. Ver tabla de posiciones")
        print("5. Top 5 goleadores")
        print("6. Top 5 asistencias")
        print("7. Top 5 tarjetas rojas")
        print("8. Ver toda la liga (jugadores y equipos)")
        print("9. Comprar entrada")
        print("10. Salir")

        opcion = input("Elegí una opción: ")

        if not opcion.isdigit() or not (1 <= int(opcion) <= 10):
            print("❌ Opción inválida. Ingrese un valor correcto.")
            continue

        match opcion:
            case '1':
                nombre = input("Nombre del equipo: ")
                agregar_equipo(nombre)
            case '2':
                nombre = input("Nombre del jugador: ")
                apellido = input("Apellido del jugador: ")
                agregar_jugador(nombre, apellido)
            case '3':
                simular_partidos()
            case '4':
                mostrar_tabla()
            case '5':
                mostrar_top5_consola('goles', 'Goleadores', '⚽', 'goles')
            case '6':
                mostrar_top5_consola('asistencias', 'Asistentes', '🎯', 'asistencias')
            case '7':
                mostrar_top5_consola('rojas', 'Expulsados', '🟥', 'rojas')
            case '8':
                ver_liga_completa()
            case '9':
                nombre_cliente = input("Nombre del cliente: ")
                comprar_entrada(nombre_cliente)
            case '10':
                print("👋 ¡Hasta luego!")
                break

menu()
