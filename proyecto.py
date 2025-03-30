import random
def cantAsistencia():
    lista=[]
    for i in range(0,5):
        lista.append(random.randint(1,20))
    return lista
def jugadores():
    nombresJugadores=["Carlos","antonio","luis","esteban","gustavo"]
    return nombresJugadores
def main():
    cantidad = cantAsistencia()
    nombres = jugadores()
    for i in range(len(nombres)):
        print (nombres[i],"  ", cantidad[i])
  
main()






