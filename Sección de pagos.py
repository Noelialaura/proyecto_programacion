# sistema_pagos.py
import json
import random
from datetime import datetime, timedelta
import time
import sys

estadios = {
    "Estadio A": 50000,
    "Estadio B": 45000
}

equipos = [
    "River Plate", "Boca Juniors", "Racing Club", "Independiente",
    "San Lorenzo", "Huracán", "Vélez Sarsfield", "Estudiantes",
    "Gimnasia", "Newell's Old Boys", "Rosario Central", "Argentinos Juniors"
]

# Generar partidos aleatorios entre equipos sin repetir
random.seed(datetime.now().timestamp())
partidos = []
usados = set()
fechas_base = datetime(2025, 6, 1)
dias_disponibles = list(range(1, 31))
while len(partidos) < 6 and len(usados) < 66:
    eq1, eq2 = random.sample(equipos, 2)
    key = tuple(sorted([eq1, eq2]))
    if key in usados:
        continue
    usados.add(key)
    if not dias_disponibles:
        dias_disponibles = list(range(1, 31))
    dia = dias_disponibles.pop(random.randint(0, len(dias_disponibles)-1))
    fecha = (fechas_base + timedelta(days=dia)).strftime("%Y-%m-%d")
    estadio = random.choice(list(estadios.keys()))
    precio = random.randint(20000, 50000)
    partidos.append({
        "id": len(partidos) + 1,
        "fecha": fecha,
        "estadio": estadio,
        "equipos": f"{eq1} vs {eq2}",
        "capacidad": estadios[estadio],
        "precio": precio
    })

def barra_de_carga(total=20, delay=0.1):
    for i in range(total + 1):
        porcentaje = int((i / total) * 100)
        barra = '=' * i + ' ' * (total - i)
        sys.stdout.write(f'\r[{barra}] {porcentaje}%')
        sys.stdout.flush()
        time.sleep(delay)
    print("\n✅ Proceso terminado.")

def mostrar_partidos():
    print("\n=== Lista de Partidos Disponibles ===")
    for p in partidos:
        fecha_fmt = datetime.strptime(p['fecha'], '%Y-%m-%d').strftime('%d de %B, %Y')
        print(f"ID: {p['id']}")
        print(f"Fecha: {fecha_fmt}")
        print(f"Estadio: {p['estadio']}")
        print(f"Equipos: {p['equipos']}")
        print(f"Capacidad: {p['capacidad']:,} personas")
        print(f"Precio: ${p['precio']:,} CLP")
        print("---------------------------")

import curses

def procesar_pago(stdscr):
    stdscr.clear()
    stdscr.addstr("=== Lista de Partidos Disponibles ===\n")
    for p in partidos:
        fecha_fmt = datetime.strptime(p['fecha'], '%Y-%m-%d').strftime('%d de %B, %Y')
        stdscr.addstr(f"ID: {p['id']} | {p['equipos']} | {fecha_fmt} | {p['estadio']} | ${p['precio']:,} CLP\n")
    stdscr.addstr("\nIngrese el ID del partido a pagar: ")
    stdscr.refresh()
    partido_id = stdscr.getstr().decode("utf-8").strip()
    if not partido_id.isdigit():
        stdscr.addstr("❌ Entrada inválida. Presione una tecla para volver.")
        stdscr.getch()
        return
    partido = next((p for p in partidos if p['id'] == int(partido_id)), None)
    if partido:
        stdscr.clear()
        stdscr.addstr(f"Procesando pago para: {partido['equipos']}\n")
        stdscr.addstr(f"Estadio: {partido['estadio']}, Fecha: {partido['fecha']}\n")
        stdscr.addstr(f"Precio: ${partido['precio']:,} CLP\n")
        stdscr.addstr("\nNombre del cliente: ")
        stdscr.refresh()
        nombre = stdscr.getstr().decode("utf-8").strip()
        stdscr.addstr("¿Confirmar pago? (s/n): ")
        stdscr.refresh()
        confirmacion = stdscr.getstr().decode("utf-8").strip().lower()
        if confirmacion == 's':
            entrada = {
                "cliente": nombre,
                "partido": partido['equipos'],
                "estadio": partido['estadio'],
                "fecha": partido['fecha'],
                "precio": partido['precio']
            }
            try:
                with open("pagos.json", "r") as f:
                    pagos = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                pagos = []
            pagos.append(entrada)
            with open("pagos.json", "w") as f:
                json.dump(pagos, f, indent=4)
            estadios[partido['estadio']] -= 1
            # Barra de carga
            for i in range(21):
                porcentaje = int((i/20)*100)
                barra = '='*i + ' '*(20 - i)
                stdscr.addstr(8,0,f'[{barra}] {porcentaje}%')
                stdscr.refresh()
                time.sleep(0.1)
            stdscr.addstr("\n✔ Pago registrado correctamente. Presione una tecla para continuar.")
            stdscr.getch()
        else:
            stdscr.addstr("❌ Pago cancelado. Presione una tecla para volver.")
            stdscr.getch()
    else:
        stdscr.addstr("❌ Partido no encontrado. Presione una tecla para volver.")
        stdscr.getch()

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
        print("10. Ver partidos disponibles")
        print("11. Salir")

        opcion = input("Elegí una opción: ")

        match opcion:
            case '1':
                print("[Funcionalidad pendiente: Agregar equipo]")
            case '2':
                print("[Funcionalidad pendiente: Agregar jugador]")
            case '3':
                print("[Funcionalidad pendiente: Simular partidos]")
            case '4':
                print("[Funcionalidad pendiente: Ver tabla de posiciones]")
            case '5':
                print("[Funcionalidad pendiente: Top 5 goleadores]")
            case '6':
                print("[Funcionalidad pendiente: Top 5 asistencias]")
            case '7':
                print("[Funcionalidad pendiente: Top 5 tarjetas rojas]")
            case '8':
                print("[Funcionalidad pendiente: Ver toda la liga]")
            case '9':
                curses.wrapper(procesar_pago)
            case '10':
                mostrar_partidos()
            case '11':
                print("👋 ¡Hasta luego!")
                break
            case _:
                print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()
