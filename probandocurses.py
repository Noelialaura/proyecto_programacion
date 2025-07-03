import curses

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "¡Hola desde curses!")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
