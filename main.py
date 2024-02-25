import funciones as f
import clases as cl
import time

#Se solicita el nombre al jugador y crea los tableros y barcos de jugador y máquina
jugador = cl.player(input("Hola jugador, por favor introduce tu nombre:\n"))
jugador.crear_tablero()
jugador.colocar_barcos()

maquina = cl.player("NPC")
maquina.crear_tablero()
maquina.colocar_barcos()

while "O" in jugador.tablero and "O" in maquina.tablero: #"O"= barco, mientras haya barcos se sigue jugando

    print("Turno de:",jugador.nombre)
    jugador.tablero, maquina.tablero, jugador.lista_barcos, maquina.lista_barcos, maquina.repetir_turno = f.sel_accion(jugador.tablero, maquina.tablero, jugador.lista_barcos, maquina.lista_barcos)
    #Cada turno del jugador inicia con una selección de acción.

    while maquina.repetir_turno: #Si el atributo repetir_turno=True, el jugador sigue disparando.
        maquina.disparo(f.input1(maquina.tablero))
        maquina.verificar_hundidos()
        f.ocultar_tablero(maquina.tablero)
        time.sleep(0.3)

        if "O" not in maquina.tablero: #En caso de que no queden barcos enemigos, el bucle termina
            break
        
    if "O" not in maquina.tablero: 
        #En caso de que no queden barcos enemigos, la máquina no juega y se termina la partida.
        break
    
    print("Turno de:", maquina.nombre)

    jugador.repetir_turno=True #Si el atributo repetir_turno=True, la máquina  sigue disparando.
    while jugador.repetir_turno:
        jugador.disparo_random()
        jugador.verificar_hundidos()
        print("------------------------------------------------------------\n")
        time.sleep(0.3)

if "O" not in jugador.tablero: 
    print("\n \n Has perdido")
    print("FIN DEL JUEGO")

elif "O" not in maquina.tablero:
    print("\n \n Has ganado")
    print("FIN DEL JUEGO")


