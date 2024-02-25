import funciones as f

class player:
    tablero = []
    lista_barcos = []
    repetir_turno=True

    def __init__(self, nombre):
        self.nombre = nombre
    
    def crear_tablero(self):
        self.tablero = f.crear_tablero()
        return self.tablero
    
    def colocar_barcos(self):
        self.tablero,self.lista_barcos = f.colocar_barcos(self.tablero)
        return self.tablero, self.lista_barcos
    
    def ocultar_tablero(self):
        return f.ocultar_tablero(self.tablero)
    
    def verificar_hundidos(self):
        return f.verificar_hundidos(self.lista_barcos,self.tablero)
    
    def disparo_random(self):
        self.tablero, self.repetir_turno = f.disparo_random(self.tablero, self.repetir_turno)
        return self.tablero, self.repetir_turno
    
    def disparo(self, casilla):
        self.tablero, self.repetir_turno = f.disparar(casilla, self.tablero, self.repetir_turno)
        return self.tablero, self.repetir_turno
    

    