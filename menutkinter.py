import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import random
import json
with open("equipos.json", "r") as f:
    equipos = json.load(f)
from datetime import datetime, timedelta
import time
import sys

EQUIPOS_FILE = 'equipos.json'
JUGADORES_FILE = 'jugadores.json'

NOMBRES_EQUIPOS = [
    "Leones", "Tigres", "Águilas", "Búfalos", "Cuervos",
    "Panteras", "Toros", "Osos", "Lobos", "Halcones"
]

NOMBRES_JUGADORES = [
    "Juan", "Carlos", "Diego", "Luis", "Sergio", "Pablo", "Miguel",
    "Andrés", "Javier", "Fernando", "Alejandro", "Ricardo", "Héctor", "Manuel"
]

APELLIDOS_JUGADORES = [
    "Rodríguez", "González", "Pérez", "Martínez", "López", "Sánchez", "Ramírez",
    "Torres", "Flores", "Gómez", "Díaz", "Ramos", "Vargas", "Castillo"
]

def cargar_datos(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)

def generar_equipos():
    equipos = []
    for nombre in NOMBRES_EQUIPOS:
        equipo = {
            'nombre': nombre,
            'pj': 0,
            'pg': 0,
            'pe': 0,
            'pp': 0,
            'puntos': 0
        }
        equipos.append(equipo)
    guardar_datos(EQUIPOS_FILE, equipos)
    return equipos

def generar_jugadores():
    jugadores = []
    # 3 jugadores por equipo aprox
    for _ in range(len(NOMBRES_EQUIPOS)*3):
        nombre = random.choice(NOMBRES_JUGADORES)
        apellido = random.choice(APELLIDOS_JUGADORES)
        jugador = {
            'nombre': nombre,
            'apellido': apellido,
            'goles': 0,
            'asistencias': 0,
            'rojas': 0
        }
        jugadores.append(jugador)
    guardar_datos(JUGADORES_FILE, jugadores)
    return jugadores

def simular_partidos(equipos, jugadores):
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

    guardar_datos(EQUIPOS_FILE, equipos)
    guardar_datos(JUGADORES_FILE, jugadores)

class LigaAppConMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación Liga Con Menú")
        self.root.geometry("800x500")
        self.root.configure(bg="#212121")

        # estilo Treeview
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#2B2B2B",
                        foreground="white",
                        rowheight=30,
                        fieldbackground="#2B2B2B",
                        font=("Arial", 11))
        style.map('Treeview', background=[('selected', '#4A90E2')], foreground=[('selected', 'white')])

        self.tree = ttk.Treeview(root, show="headings", selectmode="browse")
        self.tree.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.95, relheight=0.85)

        # Menú
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        menu_opciones = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Opciones", menu=menu_opciones)
        menu_opciones.add_command(label="Ver Tabla de Posiciones", command=self.mostrar_tabla)
        menu_opciones.add_command(label="Ver Top 5 Goleadores", command=self.mostrar_top5_goleadores)
        menu_opciones.add_command(label="Ver Top 5 Asistencias", command=self.mostrar_top5_asistencias)
        menu_opciones.add_command(label="Ver Top 5 Tarjetas Rojas", command=self.mostrar_top5_rojas)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Simular Nueva Jornada", command=self.nueva_jornada)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Salir", command=root.quit)

        # Generar datos y simular resultados
        self.equipos = generar_equipos()
        self.jugadores = generar_jugadores()
        simular_partidos(self.equipos, self.jugadores)

        # Mostrar menú inicial
        self.mostrar_menu_inicial()

    def mostrar_menu_inicial(self):
        ventana_opciones = tk.Toplevel(self.root)
        ventana_opciones.title("Menú Inicial")
        ventana_opciones.geometry("300x300")
        ventana_opciones.configure(bg="#212121")

        def cerrar_y_ejecutar(func):
            ventana_opciones.destroy()
            func()

        opciones = [
            ("Ver Tabla de Posiciones", self.mostrar_tabla),
            ("Top 5 Goleadores", self.mostrar_top5_goleadores),
            ("Top 5 Asistencias", self.mostrar_top5_asistencias),
            ("Top 5 Tarjetas Rojas", self.mostrar_top5_rojas),
            ("Simular Nueva Jornada", self.nueva_jornada),
            ("Salir", self.root.quit)
        ]

        for texto, funcion in opciones:
            btn = tk.Button(ventana_opciones, text=texto, command=lambda f=funcion: cerrar_y_ejecutar(f),
                            bg="#4A90E2", fg="white", font=("Arial", 11), relief="flat", padx=10, pady=5)
            btn.pack(pady=5, fill="x", padx=20)

    def limpiar_tabla(self):
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = ()

    def mostrar_tabla(self):
        self.limpiar_tabla()
        columns = ("Pos", "Equipo", "PJ", "PG", "PE", "PP", "Puntos")
        self.tree["columns"] = columns
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "Equipo":
                self.tree.column(col, anchor="w", width=220)
            else:
                self.tree.column(col, anchor="center", width=70)
        tabla_ordenada = sorted(self.equipos, key=lambda x: x['puntos'], reverse=True)
        for i, equipo in enumerate(tabla_ordenada, start=1):
            self.tree.insert("", "end", values=(
                i,
                equipo['nombre'],
                equipo['pj'],
                equipo['pg'],
                equipo['pe'],
                equipo['pp'],
                equipo['puntos']
            ))

    def mostrar_top5_goleadores(self):
        self.mostrar_top5("goles", "Goleadores")

    def mostrar_top5_asistencias(self):
        self.mostrar_top5("asistencias", "Asistencias")

    def mostrar_top5_rojas(self):
        self.mostrar_top5("rojas", "Tarjetas Rojas")

    def mostrar_top5(self, clave, titulo):
        self.limpiar_tabla()
        columns = ("Pos", "Jugador", titulo.capitalize())
        self.tree["columns"] = columns
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "Jugador":
                self.tree.column(col, anchor="w", width=300)
            else:
                self.tree.column(col, anchor="center", width=150)
        jugadores_ordenados = sorted(self.jugadores, key=lambda x: x.get(clave, 0), reverse=True)
        top_jugadores = jugadores_ordenados[:5]
        for i, jugador in enumerate(top_jugadores, start=1):
            nombre_completo = f"{jugador['nombre']} {jugador['apellido']}"
            valor = jugador.get(clave, 0)
            self.tree.insert("", "end", values=(
                i,
                nombre_completo,
                valor
            ))

    def nueva_jornada(self):
        simular_partidos(self.equipos, self.jugadores)
        messagebox.showinfo("Simulación", "Se ha simulado una nueva jornada con resultados aleatorios.")
        self.mostrar_tabla()

if __name__ == "__main__":
    root = tk.Tk()
    app = LigaAppConMenu(root)
    root.mainloop()
