import curses
import json
from LigaConnect import (
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
    stdscr.keypad(True)
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
                stdscr.addstr(0,0,"Ingrese nombre del jugador: ")
                nombre = stdscr.getstr().decode("utf-8").strip()
                stdscr.addstr(1,0,"Ingrese apellido del jugador: ")
                apellido = stdscr.getstr().decode("utf-8").strip()
                agregar_jugador(nombre, apellido)
                stdscr.addstr(3,0,"Jugador agregado. Presione una tecla para volver.")
                stdscr.getch()
            case '2':
                stdscr.clear()
                simular_partidos()
                stdscr.addstr(0,0,"Simulación completa. Presione una tecla para volver.")
                stdscr.getch()
            case '3':
                stdscr.clear()
                texto = mostrar_partidos()
                # Create a pad for scrolling if content is longer than the screen
                pad = curses.newpad(len(texto.splitlines()) + 10, w)
                for i, line in enumerate(texto.splitlines()):
                    pad.addstr(i, 0, line)
                pos = 0
                while True:
                    pad.refresh(pos, 0, 0, 0, h-2, w-1)
                    stdscr.addstr(h-1, 0, "↑↓ para desplazar, q para volver.".ljust(w-1))
                    key = stdscr.getch()
                    if key == ord('q'):
                        break
                    elif key == curses.KEY_DOWN and pos < len(texto.splitlines()) - h + 2:
                        pos += 1
                    elif key == curses.KEY_UP and pos > 0:
                        pos -= 1
            case '4':
                stdscr.clear()
                texto = mostrar_tabla()
                pad = curses.newpad(len(texto.splitlines()) + 10, w)
                for i, line in enumerate(texto.splitlines()):
                    pad.addstr(i, 0, line)
                pos = 0
                while True:
                    pad.refresh(pos, 0, 0, 0, h-2, w-1)
                    stdscr.addstr(h-1, 0, "↑↓ para desplazar, q para volver.".ljust(w-1))
                    key = stdscr.getch()
                    if key == ord('q'):
                        break
                    elif key == curses.KEY_DOWN and pos < len(texto.splitlines()) - h + 2:
                        pos += 1
                    elif key == curses.KEY_UP and pos > 0:
                        pos -= 1
            case '5':
                stdscr.clear()
                texto = mostrar_top5_consola('goles', 'Goleadores', '⚽', 'goles')
                pad = curses.newpad(len(texto.splitlines()) + 10, w)
                for i, line in enumerate(texto.splitlines()):
                    pad.addstr(i, 0, line)
                pos = 0
                while True:
                    pad.refresh(pos, 0, 0, 0, h-2, w-1)
                    stdscr.addstr(h-1, 0, "↑↓ para desplazar, q para volver.".ljust(w-1))
                    key = stdscr.getch()
                    if key == ord('q'):
                        break
                    elif key == curses.KEY_DOWN and pos < len(texto.splitlines()) - h + 2:
                        pos += 1
                    elif key == curses.KEY_UP and pos > 0:
                        pos -= 1
            case '6':
                stdscr.clear()
                texto = mostrar_top5_consola('asistencias', 'Asistentes', '🎯', 'asistencias')
                pad = curses.newpad(len(texto.splitlines()) + 10, w)
                for i, line in enumerate(texto.splitlines()):
                    pad.addstr(i, 0, line)
                pos = 0
                while True:
                    pad.refresh(pos, 0, 0, 0, h-2, w-1)
                    stdscr.addstr(h-1, 0, "↑↓ para desplazar, q para volver.".ljust(w-1))
                    key = stdscr.getch()
                    if key == ord('q'):
                        break
                    elif key == curses.KEY_DOWN and pos < len(texto.splitlines()) - h + 2:
                        pos += 1
                    elif key == curses.KEY_UP and pos > 0:
                        pos -= 1
            case '7':
                stdscr.clear()
                texto = mostrar_top5_consola('rojas', 'Expulsados', '🟥', 'rojas')
                pad = curses.newpad(len(texto.splitlines()) + 10, w)
                for i, line in enumerate(texto.splitlines()):
                    pad.addstr(i, 0, line)
                pos = 0
                while True:
                    pad.refresh(pos, 0, 0, 0, h-2, w-1)
                    stdscr.addstr(h-1, 0, "↑↓ para desplazar, q para volver.".ljust(w-1))
                    key = stdscr.getch()
                    if key == ord('q'):
                        break
                    elif key == curses.KEY_DOWN and pos < len(texto.splitlines()) - h + 2:
                        pos += 1
                    elif key == curses.KEY_UP and pos > 0:
                        pos -= 1
            case '8':
                stdscr.clear()
                texto = ver_liga_completa()
                pad = curses.newpad(len(texto.splitlines()) + 10, w)
                for i, line in enumerate(texto.splitlines()):
                    pad.addstr(i, 0, line)
                pos = 0
                while True:
                    pad.refresh(pos, 0, 0, 0, h-2, w-1)
                    stdscr.addstr(h-1, 0, "↑↓ para desplazar, q para volver.".ljust(w-1))
                    key = stdscr.getch()
                    if key == ord('q'):
                        break
                    elif key == curses.KEY_DOWN and pos < len(texto.splitlines()) - h + 2:
                        pos += 1
                    elif key == curses.KEY_UP and pos > 0:
                        pos -= 1
            case '9':
                stdscr.clear()
                procesar_pago()
                stdscr.addstr(0,0,"Presione una tecla para volver.")
                stdscr.getch()
            case '10':
                stdscr.clear()
                resetear_puntajes()
                stdscr.addstr(0,0,"Puntajes reseteados. Presione una tecla para volver.")
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
