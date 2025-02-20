import csv
import time
from datetime import datetime

class Jugada_Despeje:
    def __init__(self, id_juego, equipos, yardas, trimestre, fecha=None, tiempo_str=None):
        self.id_juego = id_juego
        self.equipos = equipos
        self.yardas = self._convertir_a_entero(yardas)
        self.trimestre = self._convertir_a_entero(trimestre)
        self.fecha = self._analizar_fecha(fecha)
        self.tiempo = self._analizar_tiempo(tiempo_str)

    @staticmethod
    def _convertir_a_entero(valor, predeterminado=0):
        """Convierte un valor a entero, manejando valores vacíos o inválidos."""
        try:
            return int(valor) if valor else predeterminado
        except ValueError:
            return predeterminado

    @staticmethod
    def _analizar_fecha(texto_fecha):
        """Convierte una cadena a fecha (YYYY-MM-DD)."""
        try:
            return datetime.strptime(texto_fecha, "%Y-%m-%d") if texto_fecha else None
        except ValueError:
            print(f"Fecha inválida: {texto_fecha}")
            return None

    @staticmethod
    def _analizar_tiempo(texto_tiempo):
        """Convierte una cadena a objeto tiempo, manejando múltiples formatos."""
        if not texto_tiempo:
            return None
        for formato in ("%H:%M:%S", "%M:%S"):
            try:
                return datetime.strptime(texto_tiempo, formato).time()
            except ValueError:
                continue
        print(f"Formato de tiempo inválido: {texto_tiempo}")
        return None

    def __eq__(self, other):
        return self.yardas == other.yardas

    def __lt__(self, other):
        return self.yardas < other.yardas

    def __gt__(self, other):
        return self.yardas > other.yardas

    def a_fila_csv(self):
        return [
            self.id_juego,
            self.equipos,
            str(self.yardas),
            str(self.trimestre),
            self.fecha.strftime("%Y-%m-%d") if self.fecha else "",
            self.tiempo.strftime("%H:%M:%S") if self.tiempo else "",
        ]
