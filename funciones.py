import numpy as np
import random
import time

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
    repetir = True

    if tablero[casilla] == "_":
        print("Agua")
        tablero[casilla] = "A"
        repetir = False

    elif tablero[casilla] == "O":
        print("Tocado, vuelves a disparar")
        tablero[casilla] = "X"

    else:
        print("Ya has disparado aquí, vuelve a intentarlo")

    return tablero, repetir

def disparo_random(tablero):
    fila_a = random.randint(0,len(tablero)-1)
    columna_a = random.randint(0,len(tablero)-1)
    casilla = (fila_a,columna_a)
    fallo = True
    repetir = False

    while fallo:
        if tablero[casilla] == "_":
            print("Agua")
            tablero[casilla] = "A"
            fallo = False

        elif tablero[casilla] == "O":
            print("Tocado, la máquina dispara de nuevo")
            tablero[casilla] = "X"
            repetir = True
            fallo = False

        else:
            continue

    return tablero, repetir

def crear_barco_random(eslora,tablero):
    barco =[]
    while len(barco) < eslora:
        fila_a = random.randint(0,len(tablero)-1)
        columna_a = random.randint(0,len(tablero)-1)

        if tablero[fila_a,columna_a]=="O":
                continue
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

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def colocar_barcos(tablero,eslora=[4,3,3,2,2,2,1,1,1,1],):
    for i in eslora:
        tablero = colocar_barco(crear_barco_random(i,tablero), tablero)
    return tablero

def input1(tablero):
    entrada=True
    while entrada:
        try:
            fila=int(input("¿En qué fila vas a atacar? (Valores válidos: 0-"+str(len(tablero)-1)+")\n"))
            if fila>=0 and fila<=len(tablero)-1:
                entrada=False
                return fila
            else:
                print("No es un valor válido, por favor vuelve a intentarlo","\n")
                time.sleep(0.3)

        except:
            print("No es un valor válido, por favor vuelve a intentarlo","\n")
            time.sleep(0.3)
            continue
        
def input2(tablero):
    entrada=True
    while entrada:
        try:
            fila=int(input("¿En qué columna vas a atacar? (Valores válidos: 0-"+str(len(tablero)-1)+")\n"))
            if fila>=0 and fila<=len(tablero)-1:
                entrada=False
                return fila
            else:
                print("No es un valor válido, por favor vuelve a intentarlo","\n")
                time.sleep(0.3)
            
        except:
            print("No es un valor válido, por favor vuelve a intentarlo","\n")
            time.sleep(0.3)
            continue
