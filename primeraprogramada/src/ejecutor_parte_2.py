from comparador_jugada import Comparador_Jugada
from lector_datos import Lector_Datos
from ordenamiento import Ordenamiento
import time
import csv
import os


def ejecutar_algoritmo_p2(algoritmo, lista_jugadas, nombre):
    comparador = Comparador_Jugada()
    inicio = time.time()

    if algoritmo == Ordenamiento.ordenamiento_por_mezcla:
        lista_ordenada, _, _ = algoritmo(lista_jugadas.copy(), comparador=comparador)
    else:
        algoritmo(lista_jugadas.copy(), comparador=comparador)
        lista_ordenada = lista_jugadas.copy()

    fin = time.time()

    print(f"\n{algoritmo.__name__} (Parte 2):")
    print(f"Inicio: {time.ctime(inicio)}")
    print(f"Duración: {fin - inicio:.4f} seg")

    ruta_salida = f"../resultados/parte2-{nombre}-resultado.csv"
    os.makedirs('../resultados', exist_ok=True)

    with open(ruta_salida, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["ID Juego", "Equipos", "Yardas", "Trimestre", "Fecha", "Tiempo"])
        for jugada in lista_ordenada:
            escritor.writerow(jugada.a_fila_csv())


if __name__ == "__main__":
    lector = Lector_Datos()
    jugadas = lector.leer_archivos(parte=2)

    algoritmos = {
        "burbuja": Ordenamiento.ordenamiento_burbuja,
        "insercion": Ordenamiento.ordenamiento_por_insercion,
        "mezcla": Ordenamiento.ordenamiento_por_mezcla,
        "rapido": Ordenamiento.ordenamiento_rapido
    }

    for nombre, algo in algoritmos.items():
        copia = jugadas.copy()
        ejecutar_algoritmo_p2(algo, copia, nombre)