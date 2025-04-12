from generador import generar_personas
from sistema_colas import simular
from metricas import calcular_metricas, imprimir_metricas

# Configuración
tiempo_total = 480
lambda_llegada = 1/2
lambda_servicio = 1/4
prob_prioridad = 0.3
num_estaciones = 3

personas = generar_personas(tiempo_total, lambda_llegada, prob_prioridad, lambda_servicio)

# Variante 1: Todas las estaciones genéricas
atendidos1, max_cola1, uso1 = simular(personas, num_estaciones, "generica", tiempo_total)
metricas1 = calcular_metricas(atendidos1, max_cola1, uso1, tiempo_total, num_estaciones)
imprimir_metricas("estaciones genericas", metricas1)

# Variante 2: Una estación exclusiva para prioridad
atendidos2, max_cola2, uso2 = simular(personas, num_estaciones, "exclusiva", tiempo_total)
metricas2 = calcular_metricas(atendidos2, max_cola2, uso2, tiempo_total, num_estaciones)
imprimir_metricas("1 estacion exclusiva para prioridad", metricas2)