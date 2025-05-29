# sistema_pagos.py
import json
import random
from datetime import datetime, timedelta

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

def procesar_pago():
    mostrar_partidos()
    try:
        partido_id = int(input("Ingrese el ID del partido a pagar: "))
        partido = next((p for p in partidos if p['id'] == partido_id), None)
        if partido:
            print(f"Procesando pago para: {partido['equipos']}")
            print(f"Estadio: {partido['estadio']}, Fecha: {partido['fecha']}")
            print(f"Precio: ${partido['precio']:,} CLP")
            nombre = input("Nombre del cliente: ")
            confirmacion = input("¿Confirmar pago? (s/n): ").strip().lower()
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
                print("✔ Pago registrado correctamente.")
            else:
                print("❌ Pago cancelado.")
        else:
            print("❌ Partido no encontrado.")
    except ValueError:
        print("❌ Entrada inválida.")

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
                procesar_pago()
            case '10':
                mostrar_partidos()
            case '11':
                print("👋 ¡Hasta luego!")
                break
            case _:
                print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()
