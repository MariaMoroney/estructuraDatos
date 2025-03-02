def hash_personalizado(fecha, cuarto, equipo_local):
    """
    Función de hash para asignar (fecha, cuarto, equipo local) a un entero [0..749].
    Ajuste esta lógica según sea necesario, pero documente cómo funciona.

    Parámetros:
    fecha (datetime.date, opcional): Fecha del juego
    cuarto (int): Cuarto del juego
    equipo_local (str): Nombre del equipo local

    Retorna:
    int: Valor hash entre 0 y 749
    """
    if fecha is None:
        anio = mes = dia = 0
    else:
        anio = fecha.year
        mes = fecha.month
        dia = fecha.day
    
    valor_base = anio + mes + dia + cuarto + len(equipo_local or "")
    return valor_base % 750