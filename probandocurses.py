import curses

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
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.curs_set(0)
    curses.noecho()
    stdscr.keypad(True)
    h, w = stdscr.getmaxyx()
    if h < 18:
        stdscr.clear()
        stdscr.addstr(0,0,"❗La ventana es demasiado pequeña. Agrándela y vuelva a ejecutar.")
        stdscr.refresh()
        stdscr.getch()
        return
    stdscr.border()

    menu_items = [
        "1️⃣  Agregar jugador",
        "🎲  Simular partidos",
        "🗓️  Mostrar partidos programados",
        "📊  Ver tabla de posiciones",
        "⚽  Top 5 goleadores",
        "🎯  Top 5 asistencias",
        "🟥  Top 5 tarjetas rojas",
        "🏟️  Ver toda la liga",
        "🎟️  Comprar entrada",
        "🔄  Resetear puntajes",
        "🚪  Salir"
    ]
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.border()
        stdscr.addstr(0, 0, "LigaConnect - Menú Principal", curses.color_pair(1) | curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(1, 0, "══════════════════════════════════════════════", curses.color_pair(1))
        for idx, item in enumerate(menu_items):
            x = 2 + idx
            if idx == current_row:
                stdscr.addstr(x, 0, item, curses.color_pair(2) | curses.A_REVERSE)
            else:
                stdscr.addstr(x, 0, item, curses.color_pair(2))
        stdscr.addstr(14,0, "Use ↑↓ para navegar y Enter para seleccionar.", curses.A_BOLD)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu_items) - 1:
            current_row += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            opcion = str(current_row + 1)
            match opcion:
                case '1':
                    stdscr.clear()
                    stdscr.addstr(0,0,"Ingrese nombre del jugador: ")
                    curses.echo()
                    nombre = stdscr.getstr().decode("utf-8").strip()
                    stdscr.addstr(1,0,"Ingrese apellido del jugador: ")
                    apellido = stdscr.getstr().decode("utf-8").strip()
                    curses.noecho()
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
                    procesar_pago(stdscr)
                    stdscr.addstr(0,0,"Presione una tecla para volver.")
                    stdscr.getch()
                case '10':
                    stdscr.clear()
                    resetear_puntajes()
                    stdscr.addstr(0,0,"Puntajes reseteados. Presione una tecla para volver.")
                    stdscr.getch()
                case '11':
                    for i in range(3):
                        stdscr.clear()
                        stdscr.border()
                        stdscr.addstr(0,0,"👋 ¡Hasta luego!", curses.color_pair(1) | curses.A_BOLD)
                        stdscr.refresh()
                        curses.napms(400)
                        stdscr.clear()
                        stdscr.refresh()
                        curses.napms(200)
                    break


# Ejecutar el menú principal si este archivo es el principal
if __name__ == "__main__":
    curses.wrapper(menu)
