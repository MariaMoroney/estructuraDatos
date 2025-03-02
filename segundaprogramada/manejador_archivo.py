import os
import pickle
from punt_play import PuntPlay  

NOMBRE_ARCHIVO_INFO = "info.dat"

def crear_info_dat_si_no_existe(ruta_directorio):
    """
    Si 'info.dat' no existe en 'ruta_directorio', lo crea con 750 espacios vacíos.
    Cada espacio inicialmente será None para indicar que está vacío.
    """
    ruta_archivo = os.path.join(ruta_directorio, NOMBRE_ARCHIVO_INFO)
    if not os.path.exists(ruta_archivo):
        print("Creando 'info.dat' con 750 registros vacíos...")
        espacios_vacios = [None] * 750
        with open(ruta_archivo, "wb") as archivo:
            pickle.dump(espacios_vacios, archivo)
    else:
        print(f"El archivo '{NOMBRE_ARCHIVO_INFO}' ya existe. No se creará un nuevo archivo.")

def cargar_info_dat(ruta_directorio):
    """
    Carga la lista de 750 registros desde 'info.dat' en 'ruta_directorio' y la devuelve.
    Si el archivo no existe, primero llama a crear_info_dat_si_no_existe.
    """
    crear_info_dat_si_no_existe(ruta_directorio)
    ruta_archivo = os.path.join(ruta_directorio, NOMBRE_ARCHIVO_INFO)
    with open(ruta_archivo, "rb") as archivo:
        lista_datos = pickle.load(archivo)
    return lista_datos

def guardar_info_dat(ruta_directorio, lista_datos):
    """
    Sobrescribe la lista completa de 750 registros en 'info.dat'.
    """
    ruta_archivo = os.path.join(ruta_directorio, NOMBRE_ARCHIVO_INFO)
    with open(ruta_archivo, "wb") as archivo:
        pickle.dump(lista_datos, archivo)

def insertar_registro(ruta_directorio, posicion, objeto_punt_play):
    """
    Inserta un objeto PuntPlay en 'info.dat' en la posición dada o 
    en un archivo de colisión si la ranura ya está ocupada.
    """
    lista_datos = cargar_info_dat(ruta_directorio)
    if lista_datos[posicion] is None:
        lista_datos[posicion] = objeto_punt_play
        guardar_info_dat(ruta_directorio, lista_datos)
    else:
        nombre_archivo_colision = f"{posicion}-col.dat"
        ruta_colision = os.path.join(ruta_directorio, nombre_archivo_colision)
        with open(ruta_colision, "ab") as archivo:
            pickle.dump(objeto_punt_play, archivo)

def leer_archivo_colision(ruta_directorio, posicion):
    """
    Lee TODOS los objetos PuntPlay almacenados en <posicion>-col.dat y los devuelve en una lista.
    Si el archivo no existe, devuelve una lista vacía.
    """
    nombre_archivo_colision = f"{posicion}-col.dat"
    ruta_colision = os.path.join(ruta_directorio, nombre_archivo_colision)
    if not os.path.exists(ruta_colision):
        return []
    
    registros_colision = []
    with open(ruta_colision, "rb") as archivo:
        while True:
            try:
                obj = pickle.load(archivo)
                registros_colision.append(obj)
            except EOFError:
                break
    return registros_colision

def encontrar_registros(ruta_directorio, posicion):
    """
    Devuelve una lista de todos los registros PuntPlay para la 'posicion' dada:
    - El registro principal de 'info.dat' (si existe).
    - Cualquier registro de colisión de <posicion>-col.dat (si existe).
    """
    lista_datos = cargar_info_dat(ruta_directorio)
    registro_principal = lista_datos[posicion]  
    lista_colision = leer_archivo_colision(ruta_directorio, posicion)
    
    resultados = []
    if registro_principal is not None:
        resultados.append(registro_principal)
    resultados.extend(lista_colision)
    return resultados