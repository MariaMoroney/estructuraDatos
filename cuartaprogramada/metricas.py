def calcular_metricas(personas_atendidas, longitud_maxima_cola, ocupacion, tiempo_total, num_estaciones):
    tiempos_espera = [p.tiempo_inicio_servicio - p.tiempo_llegada for p in personas_atendidas]
    tiempo_espera_promedio = sum(tiempos_espera) / len(tiempos_espera) if tiempos_espera else 0
    uso_total = sum(ocupacion)
    tasa_utilizacion = (uso_total / (tiempo_total * num_estaciones)) * 100
    return {
        "tiempo_espera_promedio": tiempo_espera_promedio,
        "longitud_maxima_cola": longitud_maxima_cola,
        "utilizacion": tasa_utilizacion
    }

def imprimir_metricas(nombre, metricas):
    print(f"\nSimulación con {nombre}:")
    print(f"Tiempo de espera promedio: {metricas['tiempo_espera_promedio']:.2f} min")
    print(f"Longitud máxima de cola: {metricas['longitud_maxima_cola']}")
    print(f"Utilización: {metricas['utilizacion']:.2f}%")