import os
import csv
from manejador_archivo import (
    insertar_registro,
    encontrar_registros,
    cargar_info_dat  
)
from funcion_hash import hash_personalizado
from punt_play import PuntPlay

def main():
    """
    Función principal que maneja el menú principal de la aplicación.
    """
    # Usar la ruta absoluta completa para evitar problemas con rutas relativas
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    directorio_datos = directorio_actual
    
    cargar_info_dat(directorio_datos)
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Cargar datos desde CSV (de resultados de primera tarea)")
        print("2. Buscar datos por posición de hash (0..749)")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cargar_datos_csv(directorio_datos)
        elif opcion == "2":
            buscar_datos(directorio_datos)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def cargar_datos_csv(directorio_datos):
    """
    Lee archivos CSV de la carpeta 'data/primeraprogramada/resultados',
    crea objetos PuntPlay, calcula su posición de hash 
    e inserta en info.dat.
    """
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    directorio_csv = os.path.join(directorio_actual, "..", "primeraprogramada", "resultados")
    
    # Líneas de depuración para verificar rutas
    print("Directorio actual:", directorio_actual)
    print("Ruta completa intentada:", directorio_csv)
    print("¿Existe directorio_csv?:", os.path.exists(directorio_csv))
    print("Contenido del directorio:", os.listdir(directorio_csv) if os.path.exists(directorio_csv) else "Directorio no existe")

    archivos_csv = [
        "parte1-burbuja-resultado.csv",
        "parte1-insercion-resultado.csv",
        "parte1-mezcla-resultado.csv",
        "parte1-rapido-resultado.csv",
    ]
    
    for archivo_csv in archivos_csv:
        ruta_csv = os.path.join(directorio_csv, archivo_csv)
        print(f"Verificando archivo: {ruta_csv}")
        print(f"¿Existe archivo?:", os.path.exists(ruta_csv))
        
        if not os.path.exists(ruta_csv):
            print(f"Archivo no encontrado: {ruta_csv}. Saltando.")
            continue
        
        with open(ruta_csv, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            next(lector, None)  
            
            for fila in lector:
                id_juego = fila[0]
                equipos = fila[1]
                yardas = fila[2]
                cuarto = fila[3]
                fecha_str = None  
                hora_str = None
                objeto_punt = PuntPlay(id_juego, equipos, yardas, cuarto, fecha_str, hora_str)
                
                equipo_local = obtener_equipo_local(equipos)
                
                posicion = hash_personalizado(objeto_punt.date, objeto_punt.qtr, equipo_local)
                
                insertar_registro(directorio_datos, posicion, objeto_punt)
    
    print("Carga de datos completada.")

def obtener_equipo_local(cadena_equipos):
    """
    Función de ejemplo para dividir 'EquipoVisitante@EquipoLocal' y devolver la parte del equipo local.
    Ajuste la lógica según sea necesario para su formato de datos.
    """
    if "@" in cadena_equipos:
        partes = cadena_equipos.split("@")
        if len(partes) == 2:
            return partes[1]
    return cadena_equipos

def buscar_datos(directorio_datos):
    """
    Solicita al usuario una posición [0..749], luego busca cualquier registro(s) en esa posición
    (incluyendo colisiones) y los muestra.
    """
    try:
        clave = int(input("Ingrese una posición (0..749): "))
        if clave < 0 or clave > 749:
            print("Fuera de rango. Debe estar entre 0 y 749.")
            return
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número.")
        return
    
    registros = encontrar_registros(directorio_datos, clave)
    if not registros:
        print(f"No se encontraron registros en la posición {clave}.")
    else:
        print(f"Registros encontrados en la posición {clave}:")
        for i, registro in enumerate(registros, start=1):
            print(f"\nRegistro #{i}")
            print(f"ID de Juego: {registro.game_id}")
            print(f"Equipos: {registro.teams}")
            print(f"Yardas: {registro.yards}")
            print(f"Cuarto: {registro.qtr}")
            if registro.date:
                print(f"Fecha: {registro.date.strftime('%Y-%m-%d')}")
            if registro.time:
                print(f"Hora: {registro.time.strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()