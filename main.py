import funciones as f
import time

tablero_jugador = f.crear_tablero()
tablero_jugador, barcos_jugador = f.colocar_barcos(tablero_jugador)

tablero_maquina = f.crear_tablero()
tablero_maquina, barcos_maquina  = f.colocar_barcos(tablero_maquina)

while "O" in tablero_jugador and "O" in tablero_maquina:

    tablero_jugador, tablero_maquina, barcos_jugador, barcos_maquina, repetir = f.sel_accion(tablero_jugador, tablero_maquina, barcos_jugador, barcos_maquina)
    
    while repetir:
        tablero_maquina,repetir = f.disparar(f.input1(tablero_maquina), tablero_maquina, repetir)
        tablero_maquina=f.verificar_hundidos(barcos_maquina,tablero_maquina)
        f.ocultar_tablero(tablero_maquina)
        time.sleep(0.3)
        if "O" not in tablero_maquina:
            break
        
    if "O" not in tablero_maquina:
        break
    
    repetir=True
    while repetir:
        tablero_jugador, repetir = f.disparo_random(tablero_jugador, repetir)
        tablero_jugador=f.verificar_hundidos(barcos_jugador,tablero_jugador)
        print("------------------------------------------------------------\n")
        time.sleep(0.3)

if "O" not in tablero_jugador:
    print("\n \n Has perdido")
    print("FIN DEL JUEGO")

elif "O" not in tablero_maquina:
    print("\n \n Has ganado")
    print("FIN DEL JUEGO")
else:
    print("FIN DEL JUEGO")


