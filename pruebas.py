import tkinter as tk
import LigaConnect


ventana = tk.Tk()
ventana.geometry("800x600")

ventana.title("Liga Connect")
etiqueta1 = tk.Label(ventana, text="Liga Connect", font=("Arial Bold", 20))
etiqueta1.pack()

botonMenu = tk.Button(ventana, text="Ver menu",command = LigaConnect.mostrar_menu, font=("Arial Bold", 15))
botonMenu.pack()


ventana.mainloop()




nombre = input("Ingresá el nombre del jugador que querés buscar: ")
jugador_encontrado = LigaConnect.buscar_jugador_por_nombre(jugadores, nombre)

if jugador_encontrado:
    print("Jugador encontrado:")
    print(jugador_encontrado)
else:
    print("No se encontró ningún jugador con ese nombre.")
    
nombre = input("Ingresá el nombre del jugador que querés buscar: ")
jugador_encontrado = LigaConnect.buscar_jugador_por_apellido(jugadores, apellido)

if jugador_encontrado:
    print("Jugador encontrado:")
    print(jugador_encontrado)
else:
    print("No se encontró ningún jugador con ese nombre.")



