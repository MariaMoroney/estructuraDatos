import os
import csv
from datetime import datetime
from jugada_despeje import Jugada_Despeje


class Lector_Datos:
    def __init__(self, ruta_carpeta='../dataprimeraprogramada'):
        self.ruta_carpeta = ruta_carpeta
        if not os.path.exists(ruta_carpeta):
            raise FileNotFoundError(
                f"El directorio {ruta_carpeta} no existe")

        self.columnas = {
            "desc": "desc",
            "fumble": "Fumble",
            "id_juego": "GameID",
            "equipo_visitante": "AwayTeam",
            "equipo_local": "HomeTeam",
            "yardas": "Yards.Gained",
            "trimestre": "qtr",
            "fecha": "Date",
            "tiempo": "time"
        }

    def _cumple_condiciones(self, desc, fumble):
        """Verifica si es un despeje sin fumble (sin distinción de mayúsculas/minúsculas)"""
        desc = desc.strip().lower()
        return "punt" in desc and fumble.strip() == "0"

    def leer_archivos(self, parte=1):
        """Lee y procesa todos los archivos CSV usando nombres de columnas"""
        jugadas_despeje = []
        print(f'\nLeyendo archivos desde: {os.path.abspath(self.ruta_carpeta)}')

        for nombre_archivo in os.listdir(self.ruta_carpeta):
            if not nombre_archivo.endswith(".csv"):
                continue

            ruta_completa = os.path.join(self.ruta_carpeta, nombre_archivo)
            print(f"\nProcesando: {nombre_archivo}")

            try:
                with open(ruta_completa, 'r', encoding='utf-8') as archivo:
                    lector = csv.DictReader(archivo)

                    columnas_faltantes = [
                        col for col in self.columnas.values() if col not in lector.fieldnames]
                    if columnas_faltantes:
                        print(
                            f"¡Advertencia! {nombre_archivo} no tiene las columnas requeridas: {columnas_faltantes}")
                        continue

                    for indice_fila, fila in enumerate(lector):
                        try:
                            desc = fila[self.columnas["desc"]]
                            fumble = fila[self.columnas["fumble"]]

                            if indice_fila < 3:
                                print(
                                    f"[Fila {indice_fila}] Desc: {desc[:30]}... | Fumble: {fumble}")

                            if self._cumple_condiciones(desc, fumble):
                                id_juego = fila[self.columnas["id_juego"]]
                                equipo_visitante = fila[self.columnas["equipo_visitante"]]
                                equipo_local = fila[self.columnas["equipo_local"]]
                                yardas = fila[self.columnas["yardas"]]
                                trimestre = fila[self.columnas["trimestre"]]

                                jugada = Jugada_Despeje(
                                    id_juego=id_juego,
                                    equipos=f"{equipo_visitante} @ {equipo_local}",
                                    yardas=yardas,
                                    trimestre=trimestre,
                                    fecha=fila[self.columnas["fecha"]
                                             ] if parte == 2 else None,
                                    tiempo_str=fila[self.columnas["tiempo"]
                                                 ] if parte == 2 else None
                                )

                                jugadas_despeje.append(jugada)
                                if len(jugadas_despeje) % 100 == 0:
                                    print(
                                        f"Jugadas cargadas: {len(jugadas_despeje)}")

                        except Exception as e:
                            print(f"Error en la fila {indice_fila}: {str(e)}")
                            continue

            except Exception as e:
                print(f"Error al abrir {nombre_archivo}: {str(e)}")
                continue

        print(f"\nTotal de jugadas válidas: {len(jugadas_despeje)}")
        return jugadas_despeje