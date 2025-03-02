import csv
import time
from datetime import datetime

class PuntPlay:
    def __init__(self, game_id, teams, yards, qtr, date=None, time_str=None):
        """
        Inicializa un objeto PuntPlay con información de un punt.

        Parámetros:
        game_id (str): Identificador del juego
        teams (str): Equipos involucrados
        yards (str/int): Yardas ganadas o perdidas
        qtr (str/int): Cuarto del juego
        date (str, opcional): Fecha del juego
        time_str (str, opcional): Hora del juego
        """
        self.game_id = game_id
        self.teams = teams
        self.yards = self._convertir_a_entero(yards)
        self.qtr = self._convertir_a_entero(qtr)
        self.date = self._parsear_fecha(date)
        self.time = self._parsear_hora(time_str)

    @staticmethod
    def _convertir_a_entero(valor, por_defecto=0):
        """
        Convierte un valor a entero, manejando valores vacíos o inválidos.

        Parámetros:
        valor: Valor a convertir
        por_defecto: Valor por defecto si la conversión falla

        Retorna:
        int: Valor convertido o valor por defecto
        """
        try:
            return int(valor) if valor else por_defecto
        except ValueError:
            return por_defecto

    @staticmethod
    def _parsear_fecha(cadena_fecha):
        """
        Convierte una cadena a una fecha (YYYY-MM-DD).

        Parámetros:
        cadena_fecha (str): Cadena de fecha a parsear

        Retorna:
        datetime.date o None: Fecha parseada o None si es inválida
        """
        try:
            return datetime.strptime(cadena_fecha, "%Y-%m-%d") if cadena_fecha else None
        except ValueError:
            print(f"Fecha inválida: {cadena_fecha}")
            return None

    @staticmethod
    def _parsear_hora(cadena_hora):
        """
        Convierte una cadena a un objeto de hora, manejando múltiples formatos.

        Parámetros:
        cadena_hora (str): Cadena de hora a parsear

        Retorna:
        datetime.time o None: Hora parseada o None si es inválida
        """
        if not cadena_hora:
            return None
        
        for formato in ("%H:%M:%S", "%M:%S"):
            try:
                return datetime.strptime(cadena_hora, formato).time()
            except ValueError:
                continue
        
        print(f"Formato de hora inválido: {cadena_hora}")
        return None

    def __eq__(self, otro):
        """
        Compara si dos objetos PuntPlay tienen las mismas yardas.

        Parámetros:
        otro (PuntPlay): Otro objeto PuntPlay a comparar

        Retorna:
        bool: True si las yardas son iguales, False en caso contrario
        """
        return self.yards == otro.yards

    def __lt__(self, otro):
        """
        Compara si las yardas de este objeto son menores que las del otro.

        Parámetros:
        otro (PuntPlay): Otro objeto PuntPlay a comparar

        Retorna:
        bool: True si las yardas son menores, False en caso contrario
        """
        return self.yards < otro.yards

    def __gt__(self, otro):
        """
        Compara si las yardas de este objeto son mayores que las del otro.

        Parámetros:
        otro (PuntPlay): Otro objeto PuntPlay a comparar

        Retorna:
        bool: True si las yardas son mayores, False en caso contrario
        """
        return self.yards > otro.yards

    def a_fila_csv(self):
        """
        Convierte el objeto PuntPlay a una fila de CSV.

        Retorna:
        list: Lista con los datos del objeto en formato para CSV
        """
        return [
            self.game_id,
            self.teams,
            str(self.yards),
            str(self.qtr),
            self.date.strftime("%Y-%m-%d") if self.date else "",
            self.time.strftime("%H:%M:%S") if self.time else "",
        ]