import numpy as np
import random

def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, "_")

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def colocar_barcos(barcos, tablero):
    for barco in barcos:
        tablero = colocar_barco(barco, tablero)
    return tablero

def disparar(casilla, tablero):
    if tablero[casilla] == "_":
        print("Agua")
        tablero[casilla] = "A"
    elif tablero[casilla] == "O":
        print("Tocado")
        tablero[casilla] = "X"
    else:
        print("Ya has disparado aquí")
    return tablero

def crear_barco_random(eslora,tablero):
    barco =[]
    while len(barco) < eslora:
        fila_a = random.randint(0,9)
        columna_a = random.randint(0,9)

        orientacion = random.choice(["S","O","E","N"])

        barco = [(fila_a, columna_a)]

        while len(barco) < eslora:
            match orientacion:
                case "O":
                    columna_a -= 1 # columna_a = columna_a - 1
                case "E":
                    columna_a += 1
                case "S":
                    fila_a += 1
                case "N":
                    fila_a -= 1

            if columna_a<=0 or columna_a>len(tablero)-1 or fila_a<=0 or fila_a>len(tablero)-1:
                barco=[]
                break
            elif tablero[fila_a,columna_a]=="O":
                barco=[]
                break
            else:
                barco.append((fila_a, columna_a))

    return barco