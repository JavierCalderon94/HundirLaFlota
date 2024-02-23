import numpy as np
import random
import time

def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, "_")

def ocultar_tablero(tablero):
    tab_oculto = tablero.copy()
    tab_oculto[(tablero == "_") | (tablero == "O")] = "░"
    print("\n",tab_oculto,"\n ------------------------------------------------------------\n")

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
    return tablero, barco

def colocar_barcos(tablero,eslora=[4,3,3,2,2,2,1,1,1,1]):
    lista_barcos =[]
    for i in eslora:
        tablero,barco = colocar_barco(crear_barco_random(i,tablero), tablero)
        lista_barcos.append(barco)
    return tablero, lista_barcos

def verificar_hundidos(lista_barcos,tablero):
    for eslora in lista_barcos:
        l_barco = len(eslora)

        for fila, columna in eslora:
            if tablero[fila,columna] == "X":
                l_barco -= 1

        if l_barco == 0:
            print("¡Barco hundido!")
            for fila, columna in eslora:
                tablero[fila,columna] = "■"

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
    fallo = True

    while fallo:
        fila_a = random.randint(0,len(tablero)-1)
        columna_a = random.randint(0,len(tablero)-1)
        casilla = (fila_a,columna_a)
    
        repetir = False
    
        if tablero[casilla] == "_":
            print("Máquina dispara en:",casilla)
            print("Agua")
            tablero[casilla] = "A"
            fallo = False

        elif tablero[casilla] == "O":
            print("Máquina dispara en:",casilla)
            print("Tocado, la máquina dispara de nuevo")
            tablero[casilla] = "X"
            repetir = True
            fallo = False

        else:
            continue

    return tablero, repetir

def evitar_errores_entrada(texto,variable_a_medir):
    entrada=True
    while entrada:
        try:
            entrada_jugador = int(input(str(texto)+"(Valores válidos: 0-"+str(len(variable_a_medir)-1)+")\n"))
            if entrada_jugador>=0 and entrada_jugador<=len(variable_a_medir)-1:
                entrada=False
            else:
                print("No es un valor válido, por favor vuelve a intentarlo","\n")
                time.sleep(0.3)
                continue
        except:
            print("No es un valor válido, por favor vuelve a intentarlo","\n")
            time.sleep(0.3)
            continue

    return entrada_jugador
def input1(tablero):
    fila = evitar_errores_entrada("Por favor, elige una fila",tablero)
    columna = evitar_errores_entrada("Por favor, elige una columna",tablero)
    return fila,columna

def hundir_barco(lista_barcos,tablero):
    print("Puedes hundir",len(lista_barcos),"barcos")

    barco_hundido = evitar_errores_entrada("Elige un barco para hundir",lista_barcos)

    for fila,columna in lista_barcos[barco_hundido]:

        if tablero[fila,columna]=="■":
            print("Ese barco ya está hundido, saliendo del modo hundir barco")
            break
        else:
            tablero[fila,columna] = "■"

    return tablero

def finalizar(tablero):
    tablero[tablero=="O"] = "■"
    return tablero

def sel_accion(tablero_1,tablero_2,lista_barcos_1,lista_barcos2):
    accion=""
    while accion=="" or (accion>0 and accion<5) :
        accion = evitar_errores_entrada("Seleccione una acción:\n  0- Atacar.\n  1- Ver tablero.\n  2- Ver tablero rival (Sin niebla).\n  3- Hundir un barco enemigo.\n  4- Hundir barco propio.\n  5- Ganar la partida.\n","hundir")
        match accion:
            case 0:
                repetir=True
                return tablero_1,tablero_2,lista_barcos_1,lista_barcos2, repetir
        
            case 1:
                print(tablero_1,"\n ------------------------------------------------------------\n")

            case 2:
                print(tablero_2,"\n ------------------------------------------------------------\n")

            case 3:
                hundir_barco(lista_barcos2,tablero_2)
                ocultar_tablero(tablero_2)

            case 4:
                hundir_barco(lista_barcos_1, tablero_1)
                print(tablero_1,"\n ------------------------------------------------------------\n")

            case 5:
                finalizar(tablero_2)
                repetir=False
                return tablero_1,tablero_2,lista_barcos_1,lista_barcos2, repetir
                


