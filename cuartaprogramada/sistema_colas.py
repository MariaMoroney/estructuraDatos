def simular(personas, num_estaciones, tipo_sistema, tiempo_total):
    tiempo = 0
    cola_prioritaria = []
    cola_normal = []
    estaciones = [None] * num_estaciones
    ocupacion = [0.0] * num_estaciones
    longitud_maxima_cola = 0
    personas_atendidas = []
    personas.sort(key=lambda p: p.tiempo_llegada)
    pendientes = list(personas)
    
    while tiempo < tiempo_total or any(estaciones) or pendientes:
        while pendientes and pendientes[0].tiempo_llegada <= tiempo:
            persona = pendientes.pop(0)
            if persona.prioridad == 0:
                cola_prioritaria.append(persona)
            else:
                cola_normal.append(persona)
                
        for i in range(num_estaciones):
            if estaciones[i] is None:
                if tipo_sistema == "exclusivo" and i == 0:
                    if cola_prioritaria:
                        p = cola_prioritaria.pop(0)
                    elif cola_normal:
                        p = cola_normal.pop(0)
                    else:
                        continue
                else:
                    if cola_prioritaria:
                        p = cola_prioritaria.pop(0)
                    elif cola_normal:
                        p = cola_normal.pop(0)
                    else:
                        continue
                        
                p.tiempo_inicio_servicio = tiempo
                p.tiempo_salida = tiempo + p.tiempo_servicio
                estaciones[i] = p
                ocupacion[i] += p.tiempo_servicio
                
        for i in range(num_estaciones):
            p = estaciones[i]
            if p and p.tiempo_salida <= tiempo:
                personas_atendidas.append(p)
                estaciones[i] = None
                
        longitud_maxima_cola = max(longitud_maxima_cola, len(cola_prioritaria) + len(cola_normal))
        tiempo += 1
        
    return personas_atendidas, longitud_maxima_cola, ocupacion