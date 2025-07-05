#Llamada de bibliotecas
import random
import json
with open("equipos.json", "r", encoding="utf-8") as f:
    equipos = json.load(f)
from datetime import datetime, timedelta
import time
import sys #Permite el uso de str

# Inicialización de estructuras de datos
estadios = {
    "Estadio A": 50000,
    "Estadio B": 45000
}

jugadores = []
try:
    with open("jugadores.json", "r", encoding="utf-8") as f: #Abre archivo precargado de jugadores
        jugadores = json.load(f)
except (FileNotFoundError, json.JSONDecodeError): #Excepción si no encuentra el archivo
    jugadores = []

# Cargar partidos desde archivo si existe
try:
    with open("partidos.json", "r", encoding="utf-8") as f:
        partidos = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    partidos = []


#Excepciones en carga de jugador

def agregar_jugador(nombre, apellido):
    while True:
        try:
            int(nombre)
            raise ValueError
        except ValueError:
            if any(char.isdigit() for char in nombre):
                print("❌ El nombre no debe contener números.")
                nombre = input("Ingrese un nombre: ")
            else:
                break
    while True:
        try:
            int(apellido)
            raise ValueError
        except ValueError:
            if any(char.isdigit() for char in apellido):
                print("❌ El apellido no debe contener números.")
                apellido = input("Ingrese un apellido : ")
            else:
                break


    print("📋 Equipos disponibles:")
    for i, equipo in enumerate(equipos, start=1):
        print(f"{i}. {equipo['nombre']}")
    try:
        eleccion = int(input("Seleccione el número del equipo al que pertenece el jugador: "))
        if eleccion < 1 or eleccion > len(equipos):
            print("❌ Opción inválida.")
            return
        equipo_seleccionado = equipos[eleccion - 1]['nombre']
    except ValueError:
        print("❌ Entrada inválida.")
        return
    jugador = {
        'nombre': nombre,
        'apellido': apellido,
        'equipo': equipo_seleccionado,
        'goles': 0,
        'asistencias': 0,
        'rojas': 0
    }
    jugadores.append(jugador)
    try:
        with open("jugadores.json", "w", encoding="utf-8") as f:
            json.dump(jugadores, f, indent=4)
    except Exception as e:
        print(f"⚠️ Error al guardar el jugador: {e}")
    print("✅ Jugador agregado correctamente.")


def resetear_puntajes():
    global equipos
    confirmacion = input("⚠️ Esto reiniciará todos los puntajes. ¿Estás seguro? (s/n): ").strip().lower() #Evita errores (permite mayus o min)
    if confirmacion != 's':
        print("❌ Operación cancelada.")
        return

    with open("equipos.json", "r", encoding="utf-8") as f:
        equipos = json.load(f)

    for equipo in equipos:
        equipo["pj"] = 0
        equipo["pg"] = 0
        equipo["pe"] = 0
        equipo["pp"] = 0
        equipo["puntos"] = 0

    with open("equipos.json", "w", encoding="utf-8") as f:
        json.dump(equipos, f, indent=4)

    with open("equipos.json", "r", encoding="utf-8") as f:
        equipos = json.load(f)

    print("🔄 Puntajes reseteados.")

if not partidos:
    # Generar partidos aleatorios entre equipos sin repetir
    random.seed(datetime.now().timestamp())
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

    # Guardar los partidos generados en el archivo partidos.json
    if partidos:
        with open("partidos.json", "w", encoding="utf-8") as f:
            json.dump(partidos, f, indent=4)
    
def barra_de_carga(total=20, delay=0.1):
    for i in range(total + 1):
        porcentaje = int((i / total) * 100)
        barra = '=' * i + ' ' * (total - i)
        sys.stdout.write(f'\r[{barra}] {porcentaje}%') #Barra de carga al comprar entrada
        sys.stdout.flush()
        time.sleep(delay)
    print("\n✅ Proceso terminado.")


#Función que simula partidos
def simular_partidos():
    global equipos
    
    for equipo in equipos:
        resultado = random.choice(['G', 'E', 'P']) #Ganados, empatados y perdidos
        equipo['pj'] += 1
        
        if resultado == 'G':
            equipo['pg'] += 1
            equipo['puntos'] += 3
        elif resultado == 'E':
            equipo['pe'] += 1
            equipo['puntos'] += 1
        elif resultado == 'P':
            equipo['pp'] += 1

    # Aviso si no hay jugadores cargados
    if not jugadores:
        print("⚠️ No hay jugadores cargados. Se simularán solo los equipos.")

    # Simular estadísticas de jugadores
    for jugador in jugadores:
        jugador['goles'] += random.choices([0, 1, 2, 3], weights=[70, 20, 8, 2])[0] #weights para calcular probabilidades
        jugador['asistencias'] += random.choices([0, 1, 2], weights=[75, 20, 5])[0]
        jugador['rojas'] += random.choices([0, 1], weights=[99, 1])[0]

    # Guardar cambios en los jugadores
    with open("jugadores.json", "w", encoding="utf-8") as f:
        json.dump(jugadores, f, indent=4)

    with open("equipos.json", "w", encoding="utf-8") as f:
        json.dump(equipos, f, indent=4)

    # Recargar los datos de equipos desde el archivo para reflejar los cambios en memoria
    with open("equipos.json", "r", encoding="utf-8") as f:
        equipos = json.load(f)

    print("✅ Partidos simulados.\n")

def mostrar_partidos():
    resultado = "\n=== Lista de Partidos Disponibles ===\n"
    for p in partidos:
        fecha_fmt = datetime.strptime(p['fecha'], '%Y-%m-%d').strftime('%d de %B, %Y')
        resultado += f"ID: {p['id']}\n"
        resultado += f"Fecha: {fecha_fmt}\n"
        resultado += f"Estadio: {p['estadio']}\n"
        resultado += f"Equipos: {p['equipos']}\n"
        resultado += f"Capacidad: {p['capacidad']:,} personas\n"
        resultado += f"Entradas vendidas: {p['entradas_vendidas']}\n"
        resultado += f"Precio: ${p['precio']:,} ARS\n"
        resultado += "---------------------------\n"
    return resultado

#Funciones para imprimir datos

def mostrar_tabla():
    resultado = "\n🏆 Tabla de posiciones:\n"
    tabla = sorted(equipos, key=lambda x: x['puntos'], reverse=True)
    for i, e in enumerate(tabla, start=1):
        resultado += f"{i}. {e['nombre']}: {e['puntos']} pts (PJ: {e['pj']}, PG: {e['pg']}, PE: {e['pe']}, PP: {e['pp']})\n"
    return resultado

def mostrar_top5_consola(clave, titulo, emoji, unidad):
    resultado = f"\n{emoji} Ranking De {titulo}:\n"
    if not jugadores:
        resultado += "No hay jugadores cargados.\n"
        return resultado
    
    ordenado = sorted(jugadores, key=lambda x: x.get(clave, 0), reverse=True)
    for i, j in enumerate(ordenado[:5], start=1):
        resultado += f"{i}. {j['nombre']} {j['apellido']} ({j['equipo']}) - {j.get(clave,0)} {unidad}\n"
    return resultado

def ver_liga_completa():
    resultado = "\n📋 TODOS LOS EQUIPOS:\n"
    if not equipos:
        resultado += "No hay equipos cargados.\n"
    else:
        for e in equipos:
            resultado += f"{e['nombre']} - PJ: {e['pj']}, PG: {e['pg']}, PE: {e['pe']}, PP: {e['pp']}, Puntos: {e['puntos']}\n"
    
    resultado += "\n👥 TODOS LOS JUGADORES:\n"
    if not jugadores:
        resultado += "No hay jugadores cargados.\n"
    else:
        for j in jugadores:
            resultado += f"{j['nombre']} {j['apellido']} - Goles: {j['goles']}, Asistencias: {j['asistencias']}, Rojas: {j['rojas']}\n"
    return resultado

#Función para procesar pagos de las entradas
def procesar_pago():
    mostrar_partidos()
    opcion = input("\n¿Desea comprar una entrada? (s para sí, m para volver al menú): ").strip().lower() #Evita errores (permite mayus o min)
    if opcion != 's':
        print("🔙 Volviendo al menú principal...")
        return
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

            #Excepción para indicar cantidad de entradas compradas
            
            try:
                with open("pagos.json", "r", encoding="utf-8") as f: #Archivo que registra los pagos
                    pagos = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                pagos = []
            
            pagos.append(entrada)
            with open("pagos.json", "w", encoding="utf-8") as f:
                json.dump(pagos, f, indent=4)
            
            partido['entradas_vendidas'] += cantidad

            # Actualizar la lista de partidos con los datos del partido modificado
            for i, p in enumerate(partidos):
                if p['id'] == partido_id:
                    partidos[i] = partido
                    break

            # Guardar la lista de partidos actualizada
            try:
                with open("partidos.json", "w", encoding="utf-8") as f:
                    json.dump(partidos, f, indent=4)
            except Exception as e:
                print(f"⚠️ Error al guardar los partidos: {e}")
            barra_de_carga()
            print(f"✔ Compra registrada correctamente. {cantidad} entrada(s) vendida(s).")
        else:
            print("❌ Compra cancelada.")
            
    except ValueError:
        print("❌ Entrada inválida. Por favor ingrese un número.")

#Programa principal con función menú 

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
        print("10. Resetear puntajes")
        print("11. Salir")

        opcion = input("Seleccione una opción (1-11): ")

        if not opcion.isdigit() or not (1 <= int(opcion) <= 11):
            print("❌ Opción inválida. Por favor ingrese un número del 1 al 11.")
            continue

        #Aplicación de case para optimizar el código
        match opcion:
            case '1':
                # Confirmación simple, no utiliza pad
                nombre = input("Nombre del jugador: ")
                apellido = input("Apellido del jugador: ")
                agregar_jugador(nombre, apellido)
                print("Jugador agregado. Presione Enter para volver.")
                input()
            case '2':
                # Confirmación simple, no utiliza pad
                simular_partidos()
                print("Simulación completa. Presione Enter para volver.")
                input()
            case '3':
                # Scroll para mostrar_partidos()
                texto = mostrar_partidos()
                lines = texto.splitlines()
                pos = 0
                h = 20  # altura de ventana simulada
                w = 80  # ancho de ventana simulada
                while True:
                    print("\n".join(lines[pos:pos+h]))
                    print("↑↓ para desplazar, q para volver.".ljust(w-1))
                    key = input().lower()
                    if key == 'q':
                        break
                    elif key == '' or key == 's' or key == '↓':
                        if pos < len(lines) - h:
                            pos += 1
                    elif key == 'w' or key == '↑':
                        if pos > 0:
                            pos -= 1
            case '4':
                # Scroll para mostrar_tabla()
                texto = mostrar_tabla()
                lines = texto.splitlines()
                pos = 0
                h = 20
                w = 80
                while True:
                    print("\n".join(lines[pos:pos+h]))
                    print("↑↓ para desplazar, q para volver.".ljust(w-1))
                    key = input().lower()
                    if key == 'q':
                        break
                    elif key == '' or key == 's' or key == '↓':
                        if pos < len(lines) - h:
                            pos += 1
                    elif key == 'w' or key == '↑':
                        if pos > 0:
                            pos -= 1
            case '5':
                # Scroll para mostrar_top5_consola('goles', ...)
                texto = mostrar_top5_consola('goles', 'Goleadores', '⚽', 'goles')
                lines = texto.splitlines()
                pos = 0
                h = 20
                w = 80
                while True:
                    print("\n".join(lines[pos:pos+h]))
                    print("↑↓ para desplazar, q para volver.".ljust(w-1))
                    key = input().lower()
                    if key == 'q':
                        break
                    elif key == '' or key == 's' or key == '↓':
                        if pos < len(lines) - h:
                            pos += 1
                    elif key == 'w' or key == '↑':
                        if pos > 0:
                            pos -= 1
            case '6':
                # Scroll para mostrar_top5_consola('asistencias', ...)
                texto = mostrar_top5_consola('asistencias', 'Asistentes', '🎯', 'asistencias')
                lines = texto.splitlines()
                pos = 0
                h = 20
                w = 80
                while True:
                    print("\n".join(lines[pos:pos+h]))
                    print("↑↓ para desplazar, q para volver.".ljust(w-1))
                    key = input().lower()
                    if key == 'q':
                        break
                    elif key == '' or key == 's' or key == '↓':
                        if pos < len(lines) - h:
                            pos += 1
                    elif key == 'w' or key == '↑':
                        if pos > 0:
                            pos -= 1
            case '7':
                # Scroll para mostrar_top5_consola('rojas', ...)
                texto = mostrar_top5_consola('rojas', 'Expulsados', '🟥', 'rojas')
                lines = texto.splitlines()
                pos = 0
                h = 20
                w = 80
                while True:
                    print("\n".join(lines[pos:pos+h]))
                    print("↑↓ para desplazar, q para volver.".ljust(w-1))
                    key = input().lower()
                    if key == 'q':
                        break
                    elif key == '' or key == 's' or key == '↓':
                        if pos < len(lines) - h:
                            pos += 1
                    elif key == 'w' or key == '↑':
                        if pos > 0:
                            pos -= 1
            case '8':
                # Scroll para ver_liga_completa()
                texto = ver_liga_completa()
                lines = texto.splitlines()
                pos = 0
                h = 20
                w = 80
                while True:
                    print("\n".join(lines[pos:pos+h]))
                    print("↑↓ para desplazar, q para volver.".ljust(w-1))
                    key = input().lower()
                    if key == 'q':
                        break
                    elif key == '' or key == 's' or key == '↓':
                        if pos < len(lines) - h:
                            pos += 1
                    elif key == 'w' or key == '↑':
                        if pos > 0:
                            pos -= 1
            case '9':
                # Confirmación simple, no utiliza pad
                procesar_pago()
                print("Operación finalizada. Presione Enter para volver.")
                input()
            case '10':
                # Confirmación simple, no utiliza pad
                resetear_puntajes()
                print("Puntajes reseteados. Presione Enter para volver.")
                input()
            case '11':
                print("👋 ¡Hasta luego!")
                break
            case _:
                print("Opción inválida 🚫")

if __name__ == "__main__":
    menu()