import funciones as f

class player:
    '''
    Attributes:
        tablero (Array): Array en el que se colocarán los barcos y realizarán las acciones de la partida
        lista_barcos (list): Lista de todos los barcos de la partida.
        repetir_turno (bool): Boolean que permitirá al jugador/máquina repetir su turno en caso de acierto.

    Clase que permitirá diferencia de los elementos del jugador y de la máquina.
    '''
    tablero = []
    lista_barcos = []
    repetir_turno=True

    def __init__(self, nombre):
        '''
        Args:
            nombre (String): Nombre del jugador
        '''
        self.nombre = nombre
    
    def crear_tablero(self):
        '''
        Crea el tablero llamando a la función crear_tablero
        '''
        self.tablero = f.crear_tablero()
        return self.tablero
    
    def colocar_barcos(self):
        '''
        Crea y coloca los barcos llamando a la función colocar_barcos
        '''
        self.tablero,self.lista_barcos = f.colocar_barcos(self.tablero)
        return self.tablero, self.lista_barcos
    
    def ocultar_tablero(self):
        '''
        Oculta los elementos llamando a la función ocultar_tablero
        '''
        return f.ocultar_tablero(self.tablero)
    
    def verificar_hundidos(self):
        '''
        Revisa posición a posición el valor de todas las listas de tuplas, si detecta que todos los valores son "X"
        los sustituye con "■" llamando a la función verificar_hundidos
        '''
        return f.verificar_hundidos(self.lista_barcos,self.tablero)
    
    def disparo_random(self):
        '''
        Genera una posición aleatoria del tablero/array, revisa el valor inicial de la posición dada y sustituye
        el valor en función del valor original. Si ese valor ya es igual a "X", repite el proceso.
        '''
        self.tablero, self.repetir_turno = f.disparo_random(self.tablero, self.repetir_turno)
        return self.tablero, self.repetir_turno
    
    def disparo(self, casilla):
        '''
        Args:
            casilla (tuple): Posición que se va a atacar

        Dada una tupla con la posición deseada, llama a la función disparar.
        '''
        self.tablero, self.repetir_turno = f.disparar(casilla, self.tablero, self.repetir_turno)
        return self.tablero, self.repetir_turno
    

        
