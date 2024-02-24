import funciones as f
import clases as cl
import time

jugador = cl.player(input("Hola jugador, por favor introduce tu nombre:\n"))
maquina = cl.player("NPC")


while "O" in jugador.tablero and "O" in maquina.tablero:

    jugador.tablero, maquina.tablero, jugador.lista_barcos, maquina.lista_barcos, maquina.repetir_turno = f.sel_accion(jugador.tablero, maquina.tablero, jugador.lista_barcos, maquina.lista_barcos)
    
    while maquina.repetir_turno:
        maquina.disparo(f.input1(maquina.tablero))
        maquina.verificar_hundidos()
        f.ocultar_tablero(maquina.tablero)
        time.sleep(0.3)
        if "O" not in maquina.tablero:
            break
        
    if "O" not in maquina.tablero:
        break

    jugador.repetir_turno=True
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
else:
    print("FIN DEL JUEGO")


