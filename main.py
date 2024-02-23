import funciones as f
import time

tablero_jugador = f.crear_tablero()
tablero_jugador = f.colocar_barcos(tablero_jugador)

tablero_maquina = f.crear_tablero()
tablero_maquina = f.colocar_barcos(tablero_maquina)

while "O" in tablero_jugador and "O" in tablero_maquina:

    repetir=True
    while repetir:
        tablero_maquina,repetir = f.disparar((f.input1(tablero_maquina),f.input2(tablero_maquina)), tablero_maquina)
        print("\n",tablero_maquina,"\n")
        print("------------------------------------------------------------\n")
        time.sleep(0.3)

    repetir=True
    while repetir:
        tablero_jugador, repetir = f.disparo_random(tablero_jugador)
        print("\n",tablero_jugador,"\n")
        print("------------------------------------------------------------\n")
        time.sleep(0.3)


