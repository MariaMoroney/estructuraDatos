class Persona:
   def __init__(self, tiempo_llegada, prioridad, tiempo_servicio):
       self.tiempo_llegada = tiempo_llegada
       self.prioridad = prioridad  # 0: alta, 1: baja
       self.tiempo_servicio = tiempo_servicio
       self.tiempo_inicio_servicio = None
       self.tiempo_salida = None