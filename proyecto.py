import random
def cantAsistencia():
    lista=[]
    for i in range(0,5):
        lista.append(random.randint(1,20))
    return lista
def cantGoles():
    lista=[]
    for i in range (0,5):
        lista.append(random.randint(1,30))
        lista.sort(reverse=True)
    return lista
def tarjetasRojas():
    lista=[]
    for i in range (0,5):
        lista.append(random.randint(1,10))
    return lista
def jugadores():
    nombresJugadores=["Carlos","antonio","luis","esteban","gustavo"]
    return nombresJugadores

def main():
    cantidad = cantAsistencia()
    nombres = jugadores()
    goles = cantGoles()
    tarjetas=tarjetasRojas()
    for i in range(len(nombres)):
        print (nombres[i],"  ","cant asistencia: ", cantidad[i]," ","cant goles: ", goles[i]," ","tarjetas rojas: ",tarjetas[i])
        

main()






