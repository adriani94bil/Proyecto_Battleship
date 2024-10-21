
from inspect import ClassFoundException
# Zona del programa.
# El objetivo de esta clase es rehacer una vieja clase que use hace meses para el juego de Hundir la flota
# Con el que generar dos clases que hereden de la clase Tablero.
# La clase Tablero es el tablero básico que usa tanto la maquina como el jugador
# La clase TableroJugador tiene la puntación y el nombre del jugador
# La clase TableroOrdenador tiene el nombre y el path o url del bot
import numpy as np
import pandas as pd
import time

class Tablero:
    def __init__(self, id_user: int, tabla_op: np.array, tabla_visible: np.array):
        self.id_user = id_user
        self.tabla_op = tabla_op
        self.tabla_visible = tabla_visible

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, value):
        self._id_user = value

    @property
    def tabla_op(self):
        return self._tabla_op

    @tabla_op.setter
    def tabla_op(self, value):
        self._tabla_op = value

    @property
    def tabla_visible(self):
        return self._tabla_visible

    @tabla_visible.setter
    def tabla_visible(self, value):
        self._tabla_visible = value

class TableroJugador(Tablero):
    def __init__(self, id_user: int, tabla_op: np.array, tabla_visible: np.array, nombre_jugador: str):
        super().__init__(id_user, tabla_op, tabla_visible)
        self.nombre_jugador = nombre_jugador
        self.aciertos = 0

    #Getters y setters de Jugador
    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, value):
        self._nombre_jugador = value

    @property
    def aciertos(self):
        return self._aciertos

    @aciertos.setter
    def aciertos(self, value):
        self._aciertos = value

    #Función estado del jugador

    def player_show(self):
        print(f"{self._nombre_jugador}: con id{self.id_user} y tabla de juego {self.tabla_op} tiene {self.aciertos} aciertos")

class TableroOrdenador(Tablero):
    def __init__(self, id_user: int, tabla_op: np.array, tabla_visible: np.array, nombre_bot: str, url_bot: str):
        super().__init__(id_user, tabla_op, tabla_visible)
        self.nombre_bot = nombre_bot
        self.url_bot = url_bot

    @property
    def nombre_bot(self):
        return self._nombre_bot

    @nombre_bot.setter
    def nombre_bot(self, value):
        self._nombre_bot = value

    @property
    def url_bot(self):
        return self._url_bot

    @url_bot.setter
    def url_bot(self, value):
        self._url_bot = value
    # Funcion cargar bot
    def load_bot(self):
        try:
            bot=pd.read_pickle(self.url_bot)
            print(bot)
        except FileNotFoundError:
            print("Error: File not found.")

# Metodo auxliar que muestra los tableros
def mostrar_tablero(tablero: TableroJugador, tablero_pc: TableroOrdenador):
    print(f"""
    * * * * * {tablero.nombre_jugador} * * * * *
    """)
    print(tablero.tabla_op)

    # OJO, no mostrar la tabla de operaciones del pc, solo la de visibilidad
    print(f"""
          * * * * * {tablero_pc.nombre_bot} * * * * *
    """)
    print(tablero_pc.tabla_visible)

if __name__ == "__main__":

    tabla_op1 = np.array([[1, 0], [0, 1]])
    tabla_visible1 = np.array([['__', '__'], ['__', '__']])

    tabla_op2 = np.array([[1, 1], [0, 0]])
    tabla_visible2 = np.array([['__', '__'], ['__', '__']])

    # Crear objetos de cada clase con un try por si hay fallo
    try:
        tablero_jugador = TableroJugador(1, tabla_op1, tabla_visible1, "Adrian")
        tablero_ordenador = TableroOrdenador(2, tabla_op2, tabla_visible2, "DeepBlue", "htaaaaejemplo.com/bot1")
    except ClassFoundException:
        print("No se han cargado bien las clases ")
    # Mostrar información del objeto Jugador

    tablero_jugador.player_show()

    # Intento cargar bot, carga un pickle pero como no hay da error
    tablero_ordenador.load_bot()

    #Mostrar tablero para ver partida
    mostrar_tablero(tablero_jugador, tablero_ordenador)


