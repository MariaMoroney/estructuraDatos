import numpy as np
import random
from persona import Persona

def generar_personas(tiempo_total, lambda_llegada, prob_prioridad, lambda_servicio):
    personas = []
    tiempo_actual = 0.0
    while tiempo_actual < tiempo_total:
        tiempo_entre_llegadas = np.random.exponential(1 / lambda_llegada)
        tiempo_actual += tiempo_entre_llegadas
        if tiempo_actual >= tiempo_total:
            break
        prioridad = 0 if random.random() < prob_prioridad else 1
        tiempo_servicio = np.random.exponential(1 / lambda_servicio)
        personas.append(Persona(tiempo_actual, prioridad, tiempo_servicio))
    return personas