import curses
import json
from ligaconnect import (
    agregar_jugador,
    simular_partidos,
    mostrar_partidos,
    mostrar_tabla,
    mostrar_top5_consola,
    ver_liga_completa,
    procesar_pago,
    resetear_puntajes
)

def menu(stdscr):
    curses.curs_set(0)
    curses.echo()
    h, w = stdscr.getmaxyx()
    if h < 18:
        stdscr.clear()
        stdscr.addstr(0,0,"❗La ventana es demasiado pequeña. Agrándela y vuelva a ejecutar.")
        stdscr.refresh()
        stdscr.getch()
        return
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "LigaConnect - Menú Principal\n")
        stdscr.addstr(1, 0, "-----------------------------\n")
        stdscr.addstr(2, 0, "1. Agregar jugador\n")
        stdscr.addstr(3, 0, "2. Simular partidos\n")
        stdscr.addstr(4, 0, "3. Mostrar partidos programados\n")
        stdscr.addstr(5, 0, "4. Ver tabla de posiciones\n")
        stdscr.addstr(6, 0, "5. Top 5 goleadores\n")
        stdscr.addstr(7, 0, "6. Top 5 asistencias\n")
        stdscr.addstr(8, 0, "7. Top 5 tarjetas rojas\n")
        stdscr.addstr(9, 0, "8. Ver toda la liga\n")
        stdscr.addstr(10,0, "9. Comprar entrada\n")
        stdscr.addstr(11,0, "10. Resetear puntajes\n")
        stdscr.addstr(12,0, "11. Salir\n")
        stdscr.addstr(14,0, "Seleccione una opción (1-11): ")

        stdscr.refresh()
        opcion = stdscr.getstr().decode("utf-8").strip()

        if not opcion.isdigit() or not (1 <= int(opcion) <= 11):
            stdscr.addstr(16,0,"❌ Opción inválida. Presione una tecla para continuar.")
            stdscr.getch()
            continue

        match opcion:
            case '1':
                stdscr.clear()
                stdscr.addstr(0,0,"Función Agregar jugador aquí.")
                stdscr.addstr(2,0,"Presione una tecla para volver al menú.")
                stdscr.getch()
            case '2':
                stdscr.clear()
                stdscr.addstr(0,0,"Simular partidos.")
                stdscr.addstr(2,0,"Presione una tecla para volver al menú.")
                stdscr.getch()
            case '3':
                stdscr.clear()
                stdscr.addstr(0,0,"Mostrar partidos programados.")
                stdscr.addstr(2,0,"Presione una tecla para volver al menú.")
                stdscr.getch()
            case '4':
                stdscr.clear()
                stdscr.addstr(0,0,"Ver tabla de posiciones.")
                stdscr.addstr(2,0,"Presione una tecla para volver al menú.")
                stdscr.getch()
            case '5':
                stdscr.clear()
                stdscr.addstr(0,0,"Top 5 goleadores.")
                stdscr.addstr(2,0,"Presione una tecla para volver al menú.")
                stdscr.getch()
            case '6':
                stdscr.clear()
                stdscr.addstr(0,0,"Top 5 asistencias.")
                stdscr.addstr(2,0,"Presione una tecla para volver al menú.")
                stdscr.getch()
            case '7':
                stdscr.clear()
                stdscr.addstr(0,0,"Top 5 tarjetas rojas.")
                stdscr.addstr(2,0,"Presione una tecla para volver al menú.")
                stdscr.getch()
            case '8':
                stdscr.clear()
                stdscr.addstr(0,0,"Ver toda la liga.")
                stdscr.addstr(2,0,"Presione una tecla para volver al menú.")
                stdscr.getch()
            case '9':
                stdscr.clear()
                stdscr.addstr(0,0,"Comprar entrada.")
                stdscr.addstr(2,0,"Presione una tecla para volver al menú.")
                stdscr.getch()
            case '10':
                stdscr.clear()
                stdscr.addstr(0,0,"Resetear puntajes.")
                stdscr.addstr(2,0,"Presione una tecla para volver al menú.")
                stdscr.getch()
            case '11':
                stdscr.clear()
                stdscr.addstr(0,0,"👋 ¡Hasta luego!")
                stdscr.refresh()
                curses.napms(1500)
                break
            case _:
                stdscr.addstr(16,0,"Opción inválida 🚫")
                stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(menu)
