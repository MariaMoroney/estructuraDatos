from jugada_despeje import Jugada_Despeje
from lector_datos import Lector_Datos
from ordenamiento import Ordenamiento
import time
import csv
import os


def ejecutar_algoritmo(algoritmo, lista_jugadas, nombre):
    inicio = time.time()

    if algoritmo == Ordenamiento.ordenamiento_por_mezcla:
        lista_ordenada, comparaciones, intercambios = algoritmo(lista_jugadas.copy(), count=True)
    else:
        comparaciones, intercambios = algoritmo(lista_jugadas.copy(), count=True)
        lista_ordenada = lista_jugadas.copy()

    fin = time.time()

    print(f"\n{algoritmo.__name__}:")
    print(f"Inicio: {time.ctime(inicio)}")
    print(f"Duración: {fin - inicio:.4f} seg")
    print(f"Comparaciones: {comparaciones}")
    print(f"Intercambios: {intercambios}")

    ruta_salida = f"../resultados/parte1-{nombre}-resultado.csv"
    os.makedirs('../resultados', exist_ok=True)

    with open(ruta_salida, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["ID Juego", "Equipos", "Yardas", "Trimestre"])
        for jugada in lista_ordenada:
            escritor.writerow(jugada.a_fila_csv()[:4])


if __name__ == "__main__":
    lector = Lector_Datos()
    jugadas = lector.leer_archivos(parte=1)
    print(f"Total de jugadas cargadas: {len(jugadas)}")
    if jugadas:
        print("Primer elemento:", jugadas[0].a_fila_csv())

    algoritmos = {
        "burbuja": Ordenamiento.ordenamiento_burbuja,
        "insercion": Ordenamiento.ordenamiento_por_insercion,
        "mezcla": Ordenamiento.ordenamiento_por_mezcla,
        "rapido": Ordenamiento.ordenamiento_rapido
    }

    for nombre, algo in algoritmos.items():
        copia = jugadas.copy()
        ejecutar_algoritmo(algo, copia, nombre)
