import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog
import io
import sys
from functools import partial

# Importar el código original sin modificarlo
# [Todo el código original va aquí exactamente igual]
# ... (todo el código que proporcionaste)

# ==============================================
# Wrapper de Tkinter sin usar clases
# ==============================================

def create_main_window():
    root = tk.Tk()
    root.title("Sistema de Gestión de Fútbol")
    root.geometry("800x600")
    
    # Redirigir stdout a nuestro widget de texto
    output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
    output_text.pack(expand=True, fill='both')
    
    # Sobrescribir sys.stdout para redirigir la salida al widget de texto
    class StdoutRedirector:
        def __init__(self, text_widget):
            self.text_widget = text_widget
            
        def write(self, string):
            self.text_widget.insert(tk.END, string)
            self.text_widget.see(tk.END)
            
        def flush(self):
            pass
    
    sys.stdout = StdoutRedirector(output_text)
    
    # Frame para botones
    button_frame = ttk.Frame(root)
    button_frame.pack(fill='x', padx=5, pady=5)
    
    # Función para mostrar diálogos de entrada
    def show_input_dialog(title, prompt):
        return simpledialog.askstring(title, prompt, parent=root)
    
    # Función para mostrar diálogos de confirmación
    def show_confirm_dialog(title, message):
        return messagebox.askyesno(title, message, parent=root)
    
    # Wrappers para las funciones que necesitan entrada del usuario
    def agregar_jugador_wrapper():
        nombre = show_input_dialog("Agregar Jugador", "Nombre del jugador:")
        if nombre is None: return
        apellido = show_input_dialog("Agregar Jugador", "Apellido del jugador:")
        if apellido is None: return
        agregar_jugador(nombre, apellido)
    
    def resetear_puntajes_wrapper():
        if show_confirm_dialog("Confirmar", "⚠️ Esto reiniciará todos los puntajes. ¿Estás seguro?"):
            resetear_puntajes()
    
    def procesar_pago_wrapper():
        mostrar_partidos()
        if not show_confirm_dialog("Comprar entrada", "¿Desea comprar una entrada?"):
            print("🔙 Volviendo al menú principal...")
            return
        
        partido_id = show_input_dialog("Comprar entrada", "Ingrese el ID del partido a pagar:")
        if partido_id is None: return
        
        try:
            partido_id = int(partido_id)
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
            
            cantidad = show_input_dialog("Comprar entrada", "¿Cuántas entradas desea comprar?")
            if cantidad is None: return
            cantidad = int(cantidad)
            
            if cantidad <= 0:
                print("❌ Cantidad inválida.")
                return
            
            if partido['entradas_vendidas'] + cantidad > partido['capacidad']:
                print("❌ No hay suficientes entradas disponibles.")
                return
            
            total = cantidad * partido['precio']
            print(f"\nTotal a pagar: ${total:,} ARS")
            
            if show_confirm_dialog("Confirmar compra", "¿Confirmar compra?"):
                nombre = show_input_dialog("Comprar entrada", "Nombre del cliente:")
                if nombre is None: return
                
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
                    with open("pagos.json", "r", encoding="utf-8") as f:
                        pagos = json.load(f)
                except (FileNotFoundError, json.JSONDecodeError):
                    pagos = []
                
                pagos.append(entrada)
                with open("pagos.json", "w", encoding="utf-8") as f:
                    json.dump(pagos, f, indent=4)
                
                partido['entradas_vendidas'] += cantidad

                for i, p in enumerate(partidos):
                    if p['id'] == partido_id:
                        partidos[i] = partido
                        break

                try:
                    with open("partidos.json", "w", encoding="utf-8") as f:
                        json.dump(partidos, f, indent=4)
                except Exception as e:
                    print(f"⚠️ Error al guardar los partidos: {e}")
                
                # Mostrar barra de carga en la interfaz
                progress = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
                progress.pack(pady=10)
                
                for i in range(21):
                    progress['value'] = i * 5
                    root.update()
                    time.sleep(0.1)
                
                progress.pack_forget()
                print(f"✔ Compra registrada correctamente. {cantidad} entrada(s) vendida(s).")
            else:
                print("❌ Compra cancelada.")
                
        except ValueError:
            print("❌ Entrada inválida. Por favor ingrese un número.")
    
    # Crear botones para cada opción del menú
    options = [
        ("Agregar jugador", agregar_jugador_wrapper),
        ("Simular partidos", simular_partidos),
        ("Mostrar partidos", mostrar_partidos),
        ("Tabla de posiciones", mostrar_tabla),
        ("Top 5 goleadores", partial(mostrar_top5_consola, 'goles', 'Goleadores', '⚽', 'goles')),
        ("Top 5 asistencias", partial(mostrar_top5_consola, 'asistencias', 'Asistentes', '🎯', 'asistencias')),
        ("Top 5 tarjetas rojas", partial(mostrar_top5_consola, 'rojas', 'Expulsados', '🟥', 'rojas')),
        ("Ver toda la liga", ver_liga_completa),
        ("Comprar entrada", procesar_pago_wrapper),
        ("Resetear puntajes", resetear_puntajes_wrapper),
        ("Salir", root.quit)
    ]
    
    for text, command in options:
        btn = ttk.Button(button_frame, text=text, command=command)
        btn.pack(side='left', padx=2, pady=2)
    
    # Botón para limpiar la consola
    def clear_output():
        output_text.delete(1.0, tk.END)
    
    clear_btn = ttk.Button(root, text="Limpiar consola", command=clear_output)
    clear_btn.pack(pady=5)
    
    return root

# Ejecutar la aplicación
if __name__ == "__main__":
    root = create_main_window()
    print("=== Sistema de Gestión de Fútbol ===")
    print("Seleccione una opción del menú superior")
    root.mainloop()