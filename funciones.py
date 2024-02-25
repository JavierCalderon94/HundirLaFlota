import numpy as np
import random
import time
import variables as var

def crear_tablero(tamaño:tuple = var.tam_tab):
    '''
        Args:
            tamaño (tuple): Por defecto tamaño = (10x10)

    Crea un array de "_" en función del tamaño indicado. 
    '''

    return np.full(tamaño, "_")

def ocultar_tablero(tablero):

    '''
        Args:
            tablero (Array): Array de "_" el que se ubican los barcos "O"
    
    Imprime por pantalla un array o tablero sustituyendo todos los valores iniciales del mismo por "░"
    para simular una niebla.
    '''

    tab_oculto = tablero.copy() #No se pretende modificar el tablero, únicamente mostrar las casillas que se han atacado.
    tab_oculto[(tablero == "_") | (tablero == "O")] = "░"

    print("\n",tab_oculto,"\n ------------------------------------------------------------\n")

def crear_barco_random(eslora:int,tablero):

    '''
        Args:
            eslora (int): longitud del barco a generar.
            tablero (Array): Array de "_" el que se ubican los barcos "O"

    Genera aleatoriamente una lista de tuplas con una longitud dada (eslora). Cada tupla hace referencia a la posición 
    (fila/columna) en la que se situará un barco. En caso de que se intente generar una tupla que exceda los límites
    del Array/tablero o en la casilla a la que hace la referencia la tupla ya exista un barco, la función comenzará
    de cero de nuevo.
    '''
    barco =[] #Se genera la lista de tuplas en blanco.
    while len(barco) < eslora: #Hasta que no se alcance la longitud facilitada, se seguirá ejecutando.
        fila_a = random.randint(0,len(tablero)-1) 
        columna_a = random.randint(0,len(tablero)-1) #Genera valor aleatorio

        if tablero[fila_a,columna_a]=="O": #Comprueba si ya hay un barco en la casilla seleccionada, si lo hay reinicia
                continue
        
        orientacion = random.choice(["S","O","E","N"]) 
        #Condicion para decidir en que sentido irán las siguientes casillas del barco.
        barco = [(fila_a, columna_a)]

        while len(barco) < eslora: #Hasta que no se alcance la longitud facilitada, se seguirá ejecutando.
            match orientacion:
                case "O":
                    columna_a -= 1
                case "E":
                    columna_a += 1
                case "S":
                    fila_a += 1
                case "N":
                    fila_a -= 1
            # Se suma/resta 1 a la fila/columna en función de la condicion anterior, así avanzamos en el tablero.
                    
            if columna_a<=0 or columna_a>len(tablero)-1 or fila_a<=0 or fila_a>len(tablero)-1 or tablero[fila_a,columna_a]=="O":
                #Si la posición se sale de los límites del tablero, se borra el barco e inicia de nuevo.
                barco=[]
                break
            
            elif tablero[fila_a,columna_a]=="O":
                #Si ya hay un barco en la posición, se borra el barco e inicia de nuevo
                barco=[]
                break
            else:
                barco.append((fila_a, columna_a))

    return barco

def colocar_barco(barco:list, tablero):
    '''
    Args:
        barco (list): lista de tuplas con las posiciones de todos los elementos del barco
        tablero (Array): Array de "_" el que se ubican los barcos "O"

    Tupla a tupla, sustituye el valor en esa posición del tablero por un "O"
    '''
    for casilla in barco:
        tablero[casilla] = "O"

    return tablero, barco

def colocar_barcos(tablero, eslora_barcos:list = var.esloras):
    '''
    Args:
        tablero (Array): Array de "_" el que se ubican los barcos "O"
        eslora_barcos (list): Lista de las esloras de todos los barcos de la partida.

    Genera y coloca uno a uno los barcos en el tablero y los va guardando en una lista de listas de tuplas.
    '''
    lista_barcos =[]
    for i in eslora_barcos:
        tablero,barco = colocar_barco(crear_barco_random(i,tablero), tablero)
        lista_barcos.append(barco)
    return tablero, lista_barcos

def verificar_hundidos(lista_barcos:list, tablero):
    '''
    Args:
        lista_barcos (list): lista con las listas de tuplas que representan cada barco
        tablero (Array): Array de "_" el que se ubican los barcos "O"

    Revisa posición a posición el valor de todas las listas de tuplas, si detecta que todos los valores son "X"
    los sustituye con "■".
    '''
    for eslora in lista_barcos: #itera en la lista de listas para acceder a cada barco
        l_barco = len(eslora) # Longitud del barco

        for fila, columna in eslora: #recorre todas las posiciones del barco
            if tablero[fila,columna] == "X": #si esa posición es "X", resta una unidad.
                l_barco -= 1

        if l_barco == 0: # Si al finalizar el reccorrido de todas las posiciones es 0, sustituirá "X" por "■"
            print("¡Barco hundido!")
            for fila, columna in eslora:
                tablero[fila,columna] = "■"

    return tablero

def disparar(casilla:tuple, tablero, repetir:bool):

    '''
    Args:
        casilla (tuple): Posición de un elemento del array/tablero
        tablero (Array): Array de "_" el que se ubican los barcos "O"
        repetir (bool): Boolean que se usará como condición para continuar un bucle.

    Revisa el valor inicial de la posición dada y sustituye el valor en función del valor original.
    '''
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

def disparo_random(tablero, repetir:bool):
    '''
    Args:
        tablero (Array): Array de "_" el que se ubican los barcos "O"
        repetir (bool): Boolean que se usará como condición para continuar un bucle.

    Genera una posición aleatoria del tablero/array, revisa el valor inicial de la posición dada y sustituye
    el valor en función del valor original. Si ese valor ya es igual a "X", repite el proceso.
    '''

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

def evitar_errores_entrada(texto:str,variable_a_medir:list):

    '''
    Args:
        texto (string): texto que se mostrará en pantalla.
        variable a medir (string/list): texto cuya longitud limitará el nº de entradas permitidas.

    Limita las entradas del usuario a enteros en función de la variable a medir, evitando que haya errores de entrada
    y haya que reiniciar.
    '''

    entrada=True # Hace que el siguiente bucle se repita hasta que el usuario no introduzca un valor válido.
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
    '''
    Args:
        tablero (Array): Array de "_" el que se ubican los barcos "O"

    Función que obliga al usuario a introducir un valor del 0 a la longitud del tablero para filas y columnas.
    Se genera la posición para un ataque.
    '''
    fila = evitar_errores_entrada("Por favor, elige una fila",tablero)
    columna = evitar_errores_entrada("Por favor, elige una columna",tablero)
    return fila,columna

def hundir_barco(lista_barcos:list,tablero):
    '''
    Args:
        lista_barcos (list): lista con las listas de tuplas que representan cada barco
        tablero (Array): Array de "_" el que se ubican los barcos "O"

    Permite eliminar directamente un barco del listado de barcos a través de un input.
    '''

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
    '''
    Args:
        tablero (Array): Array de "_" el que se ubican los barcos "O"

    Sustituye todas las posiciones de los barcos por "■" finalizando la partida.
    '''
    tablero[(tablero=="O") | (tablero=="X")] = "■"
    print(tablero)
    print("TODOS LOS BARCOS SE HAN HUNDIDO")
    return tablero

def sel_accion(tablero_1, tablero_2, lista_barcos_1:list, lista_barcos2:list):

    '''
    Args:
        tablero_1 (Array): Array de "_" el que se ubican los barcos "O" del jugador 1.
        tablero_2 (Array): Array de "_" el que se ubican los barcos "O" del jugador 2.
        lista_barcos_1 (list): lista con las listas de tuplas que representan cada barco del jugador 1.
        lista_barcos_2 (list): lista con las listas de tuplas que representan cada barco del jugador 2.

    Solicita un valor del 0 al 5, ofrece Atacar, Ver tablero, Ver tablero rival (Sin niebla), Hundir un barco enemigo,
    Hundir barco propio, Ganar la partida.
    '''
        
    accion=""

    while accion=="" or (accion>0 and accion<5) :
        accion = evitar_errores_entrada("Seleccione una acción:\n  0- Atacar.\n  1- Ver tablero.\n  2- Ver tablero rival (Sin niebla).\n  3- Hundir un barco enemigo.\n  4- Hundir barco propio.\n  5- Ganar la partida.\n","hundir")
        match accion:
            case 0: #Atacar
                repetir=True
                return tablero_1,tablero_2,lista_barcos_1,lista_barcos2, repetir
        
            case 1: #Ver tablero
                print(tablero_1,"\n ------------------------------------------------------------\n")

            case 2: #Ver tablero rival (Sin niebla)
                print(tablero_2,"\n ------------------------------------------------------------\n")

            case 3: #Hundir un barco enemigo
                hundir_barco(lista_barcos2,tablero_2)
                ocultar_tablero(tablero_2)

            case 4: #Hundir barco propio
                hundir_barco(lista_barcos_1, tablero_1)
                print(tablero_1,"\n ------------------------------------------------------------\n")

            case 5: #Ganar la partida
                finalizar(tablero_2)
                repetir=False
                return tablero_1,tablero_2,lista_barcos_1,lista_barcos2, repetir
                


