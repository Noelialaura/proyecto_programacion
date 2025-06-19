
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import json
from datetime import datetime, timedelta
import time
#import sys

# --------------------------------------------
# Datos iniciales (precargados)
# --------------------------------------------
estadios = {"Estadio A": 50000, "Estadio B": 45000}

jugadores = [
    {'nombre': 'Lionel', 'apellido': 'Messi', 'goles': 0, 'asistencias': 0, 'rojas': 0},
    {'nombre': 'Sergio', 'apellido': 'Agüero', 'goles': 0, 'asistencias': 0, 'rojas': 0},
    {'nombre': 'Ángel', 'apellido': 'Di María', 'goles': 0, 'asistencias': 0, 'rojas': 0},
    {'nombre': 'Paulo', 'apellido': 'Dybala', 'goles': 0, 'asistencias': 0, 'rojas': 0},
    {'nombre': 'Lautaro', 'apellido': 'Martínez', 'goles': 0, 'asistencias': 0, 'rojas': 0},
    {'nombre': 'Emiliano', 'apellido': 'Martínez', 'goles': 0, 'asistencias': 0, 'rojas': 0},
    {'nombre': 'Nicolás', 'apellido': 'Otamendi', 'goles': 0, 'asistencias': 0, 'rojas': 0},
    {'nombre': 'Rodrigo', 'apellido': 'De Paul', 'goles': 0, 'asistencias': 0, 'rojas': 0}
]

equipos = [
    {"nombre": "River Plate", "pj": 5, "pg": 3, "pe": 1, "pp": 1, "puntos": 10},
    {"nombre": "Boca Juniors", "pj": 5, "pg": 2, "pe": 2, "pp": 1, "puntos": 8},
    {"nombre": "Racing Club", "pj": 5, "pg": 2, "pe": 1, "pp": 2, "puntos": 7},
    {"nombre": "Independiente", "pj": 5, "pg": 1, "pe": 3, "pp": 1, "puntos": 6},
    {"nombre": "San Lorenzo", "pj": 5, "pg": 1, "pe": 2, "pp": 2, "puntos": 5},
    {"nombre": "Huracán", "pj": 5, "pg": 0, "pe": 4, "pp": 1, "puntos": 4}
]

partidos = [
    {"id": 1, "fecha": "2023-11-15", "estadio": "Estadio A", "equipos": "River Plate vs Boca Juniors", "capacidad": 50000, "precio": 25000, "entradas_vendidas": 0},
    {"id": 2, "fecha": "2023-11-18", "estadio": "Estadio B", "equipos": "Racing Club vs Independiente", "capacidad": 45000, "precio": 20000, "entradas_vendidas": 0},
    {"id": 3, "fecha": "2023-11-20", "estadio": "Estadio A", "equipos": "San Lorenzo vs Huracán", "capacidad": 50000, "precio": 18000, "entradas_vendidas": 0}
]

# --------------------------------------------
# Funciones del sistema
# --------------------------------------------
def barra_de_carga(total=20, ventana=None):
    popup = tk.Toplevel(ventana)
    popup.title("Procesando compra...")
    popup.geometry("300x100")
    
    progress = ttk.Progressbar(popup, orient='horizontal', length=200, mode='determinate', maximum=total)
    progress.pack(pady=20)
    
    for i in range(total + 1):
        progress['value'] = i
        popup.update_idletasks()
        time.sleep(0.05)
    
    popup.destroy()

def agregar_jugador():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    if nombre and apellido:
        jugador = {'nombre': nombre, 'apellido': apellido, 'goles': 0, 'asistencias': 0, 'rojas': 0}
        jugadores.append(jugador)
        actualizar_lista_jugadores()
        messagebox.showinfo("Éxito", f"Jugador {nombre} {apellido} agregado.")
        nombre_entry.delete(0, 'end')
        apellido_entry.delete(0, 'end')
    else:
        messagebox.showerror("Error", "Nombre y apellido son requeridos.")

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
        else:
            equipo['pp'] += 1
    
    for jugador in jugadores:
        jugador['goles'] += random.choices([0, 1, 2], weights=[70, 25, 5])[0]
        jugador['asistencias'] += random.choices([0, 1], weights=[80, 20])[0]
        jugador['rojas'] += random.choices([0, 1], weights=[95, 5])[0]
    
    actualizar_tabla_posiciones()
    actualizar_tops()
    messagebox.showinfo("Simulación", "Partidos y estadísticas actualizados!")

def procesar_venta():
    partido_seleccionado = partidos_combobox.current()
    cantidad = cantidad_entry.get()
    
    if partido_seleccionado == -1 or not cantidad.isdigit():
        messagebox.showerror("Error", "Seleccione un partido y cantidad válida")
        return
    
    partido = partidos[partido_seleccionado]
    cantidad = int(cantidad)
    
    if partido['entradas_vendidas'] + cantidad > partido['capacidad']:
        messagebox.showerror("Error", "No hay suficientes entradas disponibles")
        return
    
    partido['entradas_vendidas'] += cantidad
    total = cantidad * partido['precio']
    
    # Barra de carga
    barra_de_carga(ventana=root)
    
    messagebox.showinfo("Éxito", f"Compra realizada!\nTotal: ${total:,} ARS")
    cantidad_entry.delete(0, 'end')

def actualizar_lista_jugadores():
    for item in jugadores_tree.get_children():
        jugadores_tree.delete(item)
    
    for jugador in jugadores:
        jugadores_tree.insert('', 'end', values=(jugador['nombre'], jugador['apellido'], jugador['goles'], jugador['asistencias'], jugador['rojas']))

def actualizar_tabla_posiciones():
    for item in tabla_tree.get_children():
        tabla_tree.delete(item)
    
    equipos_ordenados = sorted(equipos, key=lambda x: x['puntos'], reverse=True)
    for i, equipo in enumerate(equipos_ordenados, 1):
        tabla_tree.insert('', 'end', values=(i, equipo['nombre'], equipo['puntos'], equipo['pj'], equipo['pg'], equipo['pe'], equipo['pp']))

def actualizar_tops():
    # Limpiar tops
    for item in top_goles_tree.get_children():
        top_goles_tree.delete(item)
    for item in top_asistencias_tree.get_children():
        top_asistencias_tree.delete(item)
    for item in top_rojas_tree.get_children():
        top_rojas_tree.delete(item)
    
    # Actualizar tops
    top_goles = sorted(jugadores, key=lambda x: x['goles'], reverse=True)[:5]
    top_asistencias = sorted(jugadores, key=lambda x: x['asistencias'], reverse=True)[:5]
    top_rojas = sorted(jugadores, key=lambda x: x['rojas'], reverse=True)[:5]
    
    for i, jugador in enumerate(top_goles, 1):
        top_goles_tree.insert('', 'end', values=(i, f"{jugador['nombre']} {jugador['apellido']}", jugador['goles']))
    
    for i, jugador in enumerate(top_asistencias, 1):
        top_asistencias_tree.insert('', 'end', values=(i, f"{jugador['nombre']} {jugador['apellido']}", jugador['asistencias']))
    
    for i, jugador in enumerate(top_rojas, 1):
        top_rojas_tree.insert('', 'end', values=(i, f"{jugador['nombre']} {jugador['apellido']}", jugador['rojas']))

# --------------------------------------------
# Interfaz Gráfica
# --------------------------------------------
root = tk.Tk()
root.title("Sistema de Liga de Fútbol ⚽")
root.geometry("1000x700")

# Notebook (pestañas)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Pestaña Jugadores
frame_jugadores = ttk.Frame(notebook)
notebook.add(frame_jugadores, text="👥 Jugadores")

# Formulario para agregar jugadores
ttk.Label(frame_jugadores, text="Agregar Jugador", font=('Arial', 14)).grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(frame_jugadores, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
nombre_entry = ttk.Entry(frame_jugadores, width=30)
nombre_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_jugadores, text="Apellido:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
apellido_entry = ttk.Entry(frame_jugadores, width=30)
apellido_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Button(frame_jugadores, text="Agregar", command=agregar_jugador).grid(row=3, column=0, columnspan=2, pady=10)

# Lista de jugadores
jugadores_tree = ttk.Treeview(frame_jugadores, columns=('Nombre', 'Apellido', 'Goles', 'Asistencias', 'Rojas'), show='headings')
jugadores_tree.heading('Nombre', text='Nombre')
jugadores_tree.heading('Apellido', text='Apellido')
jugadores_tree.heading('Goles', text='Goles')
jugadores_tree.heading('Asistencias', text='Asistencias')
jugadores_tree.heading('Rojas', text='Rojas')
jugadores_tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

# Scrollbar
scrollbar = ttk.Scrollbar(frame_jugadores, orient='vertical', command=jugadores_tree.yview)
scrollbar.grid(row=4, column=2, sticky='ns')
jugadores_tree.configure(yscrollcommand=scrollbar.set)

# Configurar expansión
frame_jugadores.grid_rowconfigure(4, weight=1)
frame_jugadores.grid_columnconfigure(1, weight=1)

# Pestaña Partidos
frame_partidos = ttk.Frame(notebook)
notebook.add(frame_partidos, text="📅 Partidos")

ttk.Button(frame_partidos, text="Simular Partidos", command=simular_partidos).pack(pady=10)

partidos_text = scrolledtext.ScrolledText(frame_partidos, width=80, height=15)
partidos_text.pack(padx=10, pady=10)

for p in partidos:
    fecha = datetime.strptime(p['fecha'], '%Y-%m-%d').strftime('%d/%m/%Y')
    partidos_text.insert('end', f"ID: {p['id']} - {p['equipos']}\n")
    partidos_text.insert('end', f"Fecha: {fecha} | Estadio: {p['estadio']}\n")
    partidos_text.insert('end', f"Precio: ${p['precio']:,} | Entradas disponibles: {p['capacidad'] - p['entradas_vendidas']}\n")
    partidos_text.insert('end', "-"*50 + "\n")

# Pestaña Estadísticas
frame_estadisticas = ttk.Frame(notebook)
notebook.add(frame_estadisticas, text="📊 Estadísticas")

# Notebook dentro de estadísticas (sub-pestañas)
sub_notebook = ttk.Notebook(frame_estadisticas)
sub_notebook.pack(fill='both', expand=True)

# Sub-pestaña Tabla de Posiciones
tab_posiciones = ttk.Frame(sub_notebook)
sub_notebook.add(tab_posiciones, text="🏆 Tabla")

tabla_tree = ttk.Treeview(tab_posiciones, columns=('Pos', 'Equipo', 'Puntos', 'PJ', 'PG', 'PE', 'PP'), show='headings')
tabla_tree.heading('Pos', text='Pos')
tabla_tree.heading('Equipo', text='Equipo')
tabla_tree.heading('Puntos', text='Puntos')
tabla_tree.heading('PJ', text='PJ')
tabla_tree.heading('PG', text='PG')
tabla_tree.heading('PE', text='PE')
tabla_tree.heading('PP', text='PP')
tabla_tree.pack(fill='both', expand=True, padx=10, pady=10)

# Sub-pestaña Top 5 Goleadores
tab_goles = ttk.Frame(sub_notebook)
sub_notebook.add(tab_goles, text="⚽ Goleadores")

top_goles_tree = ttk.Treeview(tab_goles, columns=('Pos', 'Jugador', 'Goles'), show='headings')
top_goles_tree.heading('Pos', text='Pos')
top_goles_tree.heading('Jugador', text='Jugador')
top_goles_tree.heading('Goles', text='Goles')
top_goles_tree.pack(fill='both', expand=True, padx=10, pady=10)

# Sub-pestaña Top 5 Asistencias
tab_asistencias = ttk.Frame(sub_notebook)
sub_notebook.add(tab_asistencias, text="🎯 Asistencias")

top_asistencias_tree = ttk.Treeview(tab_asistencias, columns=('Pos', 'Jugador', 'Asistencias'), show='headings')
top_asistencias_tree.heading('Pos', text='Pos')
top_asistencias_tree.heading('Jugador', text='Jugador')
top_asistencias_tree.heading('Asistencias', text='Asistencias')
top_asistencias_tree.pack(fill='both', expand=True, padx=10, pady=10)

# Sub-pestaña Top 5 Rojas
tab_rojas = ttk.Frame(sub_notebook)
sub_notebook.add(tab_rojas, text="🟥 Rojas")

top_rojas_tree = ttk.Treeview(tab_rojas, columns=('Pos', 'Jugador', 'Rojas'), show='headings')
top_rojas_tree.heading('Pos', text='Pos')
top_rojas_tree.heading('Jugador', text='Jugador')
top_rojas_tree.heading('Rojas', text='Rojas')
top_rojas_tree.pack(fill='both', expand=True, padx=10, pady=10)

# Pestaña Ventas
frame_ventas = ttk.Frame(notebook)
notebook.add(frame_ventas, text="💰 Ventas")

ttk.Label(frame_ventas, text="Seleccione un partido:").pack(pady=5)
partidos_combobox = ttk.Combobox(frame_ventas, values=[f"{p['id']} - {p['equipos']} ({p['fecha']})" for p in partidos])
partidos_combobox.pack()

ttk.Label(frame_ventas, text="Cantidad de entradas:").pack(pady=5)
cantidad_entry = ttk.Entry(frame_ventas)
cantidad_entry.pack()

ttk.Button(frame_ventas, text="Comprar", command=procesar_venta).pack(pady=10)

# --------------------------------------------
# Inicialización de datos
# --------------------------------------------
actualizar_lista_jugadores()
actualizar_tabla_posiciones()
actualizar_tops()

root.mainloop()