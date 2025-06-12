import random
import json
with open("equipos.json", "r") as f:
    equipos = json.load(f)
from datetime import datetime, timedelta
import time
import sys

# Inicialización de estructuras de datos
estadios = {
    "Estadio A": 50000,
    "Estadio B": 45000
}

jugadores = []


def agregar_jugador(nombre, apellido):
    """Función corregida para agregar jugadores sin validación redundante"""
    jugador = {
        'nombre': nombre,
        'apellido': apellido,
        'goles': 0,
        'asistencias': 0,
        'rojas': 0
    }
    jugadores.append(jugador)
    print("✅ Jugador agregado correctamente.")

# Generar partidos aleatorios entre equipos sin repetir
random.seed(datetime.now().timestamp())
partidos = []
usados = set()
fechas_base = datetime(2025, 6, 1)
dias_disponibles = list(range(1, 31))

while len(partidos) < 6 and len(usados) < 66:
    eq1, eq2 = random.sample(equipos, 2)
    key = tuple(sorted([eq1['nombre'], eq2['nombre']]))
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
        "equipos": f"{eq1['nombre']} vs {eq2['nombre']}",
        "capacidad": estadios[estadio],
        "precio": precio,
        "entradas_vendidas": 0  # Contador de entradas vendidas
    })
    
def barra_de_carga(total=20, delay=0.1):
    for i in range(total + 1):
        porcentaje = int((i / total) * 100)
        barra = '=' * i + ' ' * (total - i)
        sys.stdout.write(f'\r[{barra}] {porcentaje}%')
        sys.stdout.flush()
        time.sleep(delay)
    print("\n✅ Proceso terminado.")

def simular_partidos():
    """Función corregida para simular partidos"""
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
    
    # Simular estadísticas de jugadores
    for jugador in jugadores:
        jugador['goles'] += random.choices([0, 1, 2, 3], weights=[70, 20, 8, 2])[0]
        jugador['asistencias'] += random.choices([0, 1, 2], weights=[75, 20, 5])[0]
        jugador['rojas'] += random.choices([0, 1], weights=[99, 1])[0]
    
    with open("equipos.json", "w") as f:
        json.dump(equipos, f, indent=4)

    # Recargar los datos de equipos desde el archivo para reflejar los cambios en memoria
    global equipos
    with open("equipos.json", "r") as f:
        equipos = json.load(f)

    print("✅ Partidos simulados.\n")

def mostrar_partidos():
    print("\n=== Lista de Partidos Disponibles ===")
    for p in partidos:
        fecha_fmt = datetime.strptime(p['fecha'], '%Y-%m-%d').strftime('%d de %B, %Y')
        print(f"ID: {p['id']}")
        print(f"Fecha: {fecha_fmt}")
        print(f"Estadio: {p['estadio']}")
        print(f"Equipos: {p['equipos']}")
        print(f"Capacidad: {p['capacidad']:,} personas")
        print(f"Entradas vendidas: {p['entradas_vendidas']}")
        print(f"Precio: ${p['precio']:,} ARS")
        print("---------------------------")

def mostrar_tabla():
    print("\n🏆 Tabla de posiciones:")
    tabla = sorted(equipos, key=lambda x: x['puntos'], reverse=True)
    for i, e in enumerate(tabla, start=1):
        print(f"{i}. {e['nombre']}: {e['puntos']} pts (PJ: {e['pj']}, PG: {e['pg']}, PE: {e['pe']}, PP: {e['pp']})")

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

def procesar_pago():
    mostrar_partidos()
    try:
        partido_id = int(input("Ingrese el ID del partido a pagar: "))
        partido = next((p for p in partidos if p['id'] == partido_id), None)
        
        if not partido:
            print("❌ Partido no encontrado.")
            return
        
        if partido['entradas_vendidas'] >= partido['capacidad']:
            print("❌ No hay entradas disponibles para este partido.")
            return
        
        print(f"\nProcesando pago para: {partido['equipos']}")
        print(f"Estadio: {partido['estadio']}, Fecha: {partido['fecha']}")
        print(f"Precio por entrada: ${partido['precio']:,} ARS")
        print(f"Entradas disponibles: {partido['capacidad'] - partido['entradas_vendidas']}")
        
        cantidad = int(input("¿Cuántas entradas desea comprar? "))
        if cantidad <= 0:
            print("❌ Cantidad inválida.")
            return
        
        if partido['entradas_vendidas'] + cantidad > partido['capacidad']:
            print("❌ No hay suficientes entradas disponibles.")
            return
        
        total = cantidad * partido['precio']
        print(f"\nTotal a pagar: ${total:,} ARS")
        
        confirmacion = input("¿Confirmar compra? (s/n): ").strip().lower()
        if confirmacion == 's':
            nombre = input("Nombre del cliente: ")
            
            entrada = {
                "cliente": nombre,
                "partido": partido['equipos'],
                "estadio": partido['estadio'],
                "fecha": partido['fecha'],
                "cantidad": cantidad,
                "precio_unitario": partido['precio'],
                "total": total
            }
            
            try:
                with open("pagos.json", "r") as f:
                    pagos = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                pagos = []
            
            pagos.append(entrada)
            with open("pagos.json", "w") as f:
                json.dump(pagos, f, indent=4)
            
            partido['entradas_vendidas'] += cantidad
            barra_de_carga()
            print(f"✔ Compra registrada correctamente. {cantidad} entrada(s) vendida(s).")
        else:
            print("❌ Compra cancelada.")
            
    except ValueError:
        print("❌ Entrada inválida. Por favor ingrese un número.")

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar jugador")
        print("2. Simular partidos")
        print("3. Mostrar partidos programados")
        print("4. Ver tabla de posiciones")
        print("5. Top 5 goleadores")
        print("6. Top 5 asistencias")
        print("7. Top 5 tarjetas rojas")
        print("8. Ver toda la liga (jugadores y equipos)")
        print("9. Comprar entrada")
        print("10. Salir")
        print("11. Reiniciar estadísticas de equipos")

        opcion = input("Seleccione una opción (1-11): ")

        # Validación modificada para incluir el número 11
        if not opcion.isdigit() or not (int(opcion) in [1,2,3,4,5,6,7,8,9,10,11]):
            print("❌ Opción inválida. Por favor ingrese un número del 1 al 11.")
            continue

        match opcion:
            case '1':
                nombre = input("Nombre del jugador: ")
                apellido = input("Apellido del jugador: ")
                agregar_jugador(nombre, apellido)
            case '2':
                simular_partidos()
            case '3':
                mostrar_partidos()
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
                procesar_pago()
            case '10':
                print("👋 ¡Hasta luego!")
                break
            case '11':
                for equipo in equipos:
                    equipo['pj'] = 0
                    equipo['pg'] = 0
                    equipo['pe'] = 0
                    equipo['pp'] = 0
                    equipo['puntos'] = 0
                with open("equipos.json", "w") as f:
                    json.dump(equipos, f, indent=4)
                with open("equipos.json", "r") as f:
                    equipos = json.load(f)
                print("🔄 Estadísticas de equipos reiniciadas.")
            case _:
                print("Opción inválida 🚫")

if __name__ == "__main__":
    menu()