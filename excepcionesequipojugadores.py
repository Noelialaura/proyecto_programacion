equipos =[]
jugadores =[]
def agregar_equipo(nombre):
    
    for equipo in equipos:
        if equipo['nombre'].lower() == nombre.lower():
            print("❌ Ese equipo ya está cargado.")
            return
        
    try:
        while int(nombre):
            print("ERROR, solo se aceptan caracteres, NO NUMEROS")
            nombre = input("ingrese otro nombre: ")
    except ValueError:
        equipo = {
     'nombre': nombre,
        'pj': 0,
        'pg': 0,
        'pe': 0,
        'pp': 0,
        'puntos': 0
    }
        equipos.append(equipo)
        print("✅ Equipo agregado correctamente.")

def agregar_jugador(nombre, apellido):
    try:
        while int(nombre):
            print("ERROR, INGRESE UN NOMBRE")
            nombre = input("ingrese un nombre: ")
    except ValueError:
        jugador = {
        'nombre': nombre,
        }
    try:
         while int(apellido):
            print("ERROR, INGRESE UN APELLIDO")
            apellido = input("ingrese un apellido: ")
    except ValueError:
        jugador = {
        'apellido': apellido,
        'goles': 0,
        'asistencias': 0,
        'rojas': 0
    }
    jugadores.append(jugador)
        
    
    
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar equipo")
        print("2. Agregar jugador")

        opcion = input("Elegí una opción: ")
        
        match opcion:
            case '1':
                nombre = input("Nombre del equipo: ")
                agregar_equipo(nombre)
            case '2':
                nombre = input("Nombre del jugador: ")
                apellido = input("Apellido del jugador: ")
                agregar_jugador(nombre, apellido)
menu()